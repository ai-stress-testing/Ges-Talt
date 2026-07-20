# Hard verifiers — brainstorm

A different axis from the OPSEC tactic checklists. Those ask *does a control
exist* (presence), modeled as employee-personas. A **hard verifier** asks
*does the security property actually hold* (efficacy), modeled as a machine:

- **One property, one machine.** Single job. Composable like `verify_comms`.
- **Binary verdict + counterexample.** PASS, or FAIL with the exact input/
  state that broke it. No "looks fine."
- **Fail closed.** Absence of a PASS is a FAIL.
- **Deterministic > probe > judgment.** Prefer a static assertion or
  property test that always answers; fall back to a live probe; use an LLM
  (`logicians/falsifier`, `ai/model-evaluator`) only for properties code
  can't decide (business-logic invariants, novel threats).
- **The security team authors and owns verifiers — it is not the verifier.**
  A persona reasons and maintains; the machine gates. This is the shift.

Presence vs efficacy is the whole point: "a rate limit is configured" is a
checklist row; "I exceeded the limit and got a 429 on request N+1" is a
verifier. Only the second is falsifiable, so only the second is a gate.

Each verifier below reads: **assert P — [method] — owner**. Method:
`static` (code/config analysis), `ptest` (property/fuzz test), `probe`
(live attempt against a running target), `reason` (LLM verifier).

## Securing data

- Assert every store (DB/volume/bucket) has encryption-at-rest enabled — static — `security/cloud-security-architect`.
- Assert no PII-typed value reaches a log/analytics sink (taint from PII source to sink; the path is the counterexample) — static — `legal/privacy-engineer`.
- Assert every schema field carries a data-classification tag; untagged = FAIL (forces classification to exist) — static — `legal/data-protection-officer`.
- Assert deletion actually deletes: request erasure, then confirm the record is unrecoverable across **primary, replicas, backups, cache, and search index** — probe — `legal/privacy-engineer`. (The common gap: gone from Postgres, still in Elasticsearch.)
- Assert retention deletes: insert a record older than its policy, confirm the reaper removed it — probe — `data/data-engineer`.
- Assert cross-tenant isolation: tenant A's credential returns zero of tenant B's rows under fuzzed tenant IDs — ptest — `backend/backend-dev`.
- Assert backups restore: periodic restore drill with checksum match — probe — `cd/sre`. (A backup you've never restored is a hope, not a backup.)
- Assert the audit log is append-only *and* hash-chained (each entry commits the prior) so deletion/tampering is detectable — probe — `security/threat-detection-engineer`.

## Securing APIs

- Assert every route has an auth guard except an explicit allowlist; an unlisted unauthenticated route = FAIL — static from the route table — `security/senior-secops`. (Catches the endpoint shipped without auth.)
- Assert object-level authorization (BOLA/IDOR, OWASP API #1): identity A cannot reach B's object via any endpoint under fuzzed object IDs — ptest — `backend/backend-dev`.
- Assert responses match their declared schema — no field the contract didn't promise (the "returned the whole user row including password_hash") — static/ptest — `backend/api-platform-engineer`.
- Assert no endpoint binds request fields to protected model attributes (mass assignment) — static — `backend/backend-dev`.
- Assert money/mutation endpoints honor an idempotency key: replay the same request, exactly one effect — probe — `backend/payments-billing-engineer`.
- Assert error responses never leak stack traces / internal hostnames / SQL — probe with malformed input, scan response — `security/senior-secops`.
- Assert every list endpoint caps page size (no unbounded scrape) — probe — `backend/api-platform-engineer`.
- Assert no route past its sunset date is still live — static — `cd/lifecycle-manager`.
- Assert a token's *used* scope ≤ *granted* scope ≤ *needed* scope (confused-deputy / scope creep) — static+probe — `security/identity-access-engineer`.

## Securing inputs

- Assert no user input concatenates into a SQL/shell/HTML/LDAP/template sink — parameterization taint check, the flow is the counterexample — static — `security/appsec-engineer`.
- Assert output encoding matches the *sink context* (HTML body vs attribute vs JS vs URL) — static — `frontend/react-dev`.
- Assert canonicalization happens **before** any authz decision (path traversal, unicode confusables, RTLO) — the validate-then-canonicalize ordering bug — static — `security/appsec-engineer`.
- Assert every input has a max size, and structured input a max depth/nesting (billion-laughs, zip-bomb, JSON-depth DoS) — static+probe — `backend/backend-dev`.
- Assert no regex has catastrophic backtracking (ReDoS) — static analysis of the pattern — `security/appsec-engineer`.
- Assert validation is allowlist and rejects unknown fields (fail closed, not denylist) — static — `backend/backend-dev`.
- Assert no untrusted input reaches an unsafe deserializer (pickle, native Java, YAML unsafe_load) — static — `security/appsec-engineer`.
- Assert uploads are content-sniffed by magic bytes (not extension), stored outside web root, never executable — probe — `security/senior-secops`.

## Networks

- **Egress allowlist**: assert no service reaches a destination off its declared allowlist — probe a non-allowlisted host, expect blocked — `networking/network-engineer`. (The exfil path — the single highest-value network verifier, ties to `environments/THREAT-MODEL.md`.)
- Assert every network policy defaults deny; no `0.0.0.0/0` ingress; only declared ports open — static — `networking/network-engineer`.
- Assert SSRF-reachability is zero: server-side fetchers cannot reach internal/RFC1918/`169.254.169.254` metadata — probe — `security/appsec-engineer`. (Cloud-metadata SSRF.)
- Assert service-to-service is mutually authenticated (mTLS); no plaintext internal traffic — probe — `networking/network-engineer`.
- Assert every TLS listener negotiates only 1.2+, strong ciphers, valid non-expired cert, HSTS — static scan — `networking/network-engineer`.
- Assert no cert is within N days of expiry — static — `cd/sre`. (The recurring self-inflicted outage.)
- Assert DNS query volume/entropy per host stays under threshold (tunneling/exfil) — probe/detect — `security/threat-detection-engineer`.

## Encryption

- Assert no banned primitive in use: MD5, SHA1, DES, RC4, ECB mode, static IV — static scan of crypto calls — `security/appsec-engineer`.
- Assert key/IV/nonce/token generation uses a CSPRNG, never `Math.random`/seeded PRNG — static — `security/appsec-engineer`. (The token-predictability classic.)
- Assert nonce uniqueness per key (reuse is catastrophic for GCM/CTR): log `(key, nonce)` pairs, assert no repeat — probe — `security/appsec-engineer`.
- Assert secret comparisons are constant-time, not `==` (timing oracle) — static — `security/appsec-engineer`.
- Assert every key has a max age and rotation *actually changed the material* within it — static+probe — `security/cloud-security-architect`.
- Assert data-encryption keys are never stored beside ciphertext and are wrapped by a KMS (envelope) — static — `security/cloud-security-architect`.
- Assert forward secrecy (ephemeral ECDHE) so one key compromise can't decrypt captured past traffic — static — `networking/network-engineer`.
- Assert the three states are *separately* enforced: at-rest, in-transit, **in-use** (secrets absent from heap/core dumps, swap, CI logs, container layers) — probe a memory/core dump + CI logs for secret patterns, expect zero — `security/senior-secops`. (In-use is the usually-forgotten third.)

## Gaps not considered in the checklists

The tactic checklists are attacker-technique-shaped and control-presence-
shaped. These classes fall through:

- **Efficacy over presence** (the meta-gap): every checklist row should have
  a paired verifier that *exercises* the control, or it's unproven.
- **Business-logic invariants** — no scanner catches "balance never goes
  negative", "an order can't ship before payment clears", negative-quantity/
  price manipulation, TOCTOU double-spend. These need property/invariant
  verifiers and model-checking of the state machine for reachable bad states
  — `reason` (`logicians/falsifier`) + ptest. The richest unguarded surface.
- **Revocation propagation** — a token/session still works after its
  permission was revoked ("the fired employee's token"). Assert access is
  lost within N seconds of revocation — probe — `security/identity-access-engineer`.
- **Supply-chain provenance** beyond SBOM — assert each artifact has a
  signed attestation binding it to a reviewed source commit + builder
  (SLSA), and that an independent rebuild is bit-identical (reproducible).
  SBOM lists deps; it doesn't prove the binary came from the source.
- **Dependency confusion** — assert every dependency resolves to the
  intended registry/namespace (no internal name shadowed by a public
  package) — static — `security/appsec-engineer`.
- **Denial-of-wallet** — assert every autoscaling / pay-per-call / AI-
  inference path has a hard budget cap (financial DoS, not traffic DoS) —
  static+probe — `cd/finops-engineer`.
- **Detection of absence** (dead-man's switch) — assert every expected
  security-telemetry source emitted within its heartbeat window; silence is
  the alert ("we stopped getting logs from that host and didn't notice") —
  probe — `security/threat-detection-engineer`.
- **Config drift as a security event** — assert deployed config still
  matches reviewed git (any drift = ungoverned change) — `cd/gitops-engineer`.
- **Side-channel indistinguishability** — assert auth-failure responses are
  identical in time and body ("user not found" vs "wrong password" oracle) —
  probe — `security/appsec-engineer`.
- **Clock trust** — assert no security decision (token expiry, replay
  window) trusts client-supplied time — static — `security/appsec-engineer`.
- **The agent org as target** — assert no agent mutated a file outside its
  declared tool scope; assert external issue/PR text never became an executed
  instruction (threat-model C7); assert an ephemeral agent passed the tool-
  boundary check before spawn — static/reason — `security/architect`. Secure
  the machine that secures the machines.
- **Ransomware resilience** — assert backups are immutable/WORM *and* a
  restore drill passed within N days (not just "backups exist") — probe —
  `cd/sre`.
- **AI/ML input surface** — assert RAG-retrieved content is handled as data
  not instructions; assert output filtering on model responses; membership-
  inference resistance — `reason` (`ai/model-evaluator`).

## How this plugs in

Verifiers are the security arm of the verdict loop (`agents/WORKFLOW.md`):
a major output doesn't PASS until the verifiers for the properties it
touches are green — the same way `build_index.py`/`verify_comms.py` already
gate the roster. Most belong in CI as deterministic checks; the `reason`
ones are the falsifier/model-evaluator doing what code can't. The security
team's job shifts accordingly: **write and own verifiers**, don't be the
verifier.

**Built (GT-43).** The registry exists: `scripts/verifiers/`, one
single-property machine per file (`PROPERTY`/`METHOD`/`OWNER`/`check()`),
composed by `scripts/verify.py` — failures first, fail-closed, exit non-zero
on any FAIL (`WORKFLOW.md §5`). The seed set secures the **agent org
itself** (the "org as target" class above): roster pairing, reason-tier
read-only boundary, handoff-reference resolution, INDEX + repo-map
freshness, ledger well-formedness, tools-baseline containment, current
sprint window, and branch taxonomy. The security/domain verifiers listed in
the sections above (egress allowlist, BOLA/IDOR, banned crypto primitives,
…) are the same shape — a target repo drops them into the same
`scripts/verifiers/` directory and the runner picks them up. Run
`python3 scripts/verify.py --list` to see the registered machines.
