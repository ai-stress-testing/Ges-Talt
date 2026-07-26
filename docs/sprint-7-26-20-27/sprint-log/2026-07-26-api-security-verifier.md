# 2026-07-26 — Dedicated API-security verification (#7, #56)

**Session/agent**: main session (orchestrator) + `security/red-team-critic`
(delegated adversarial review — the roster's first genuinely-delegated,
ledger-recorded run this session).
**Issues touched**: #7, #56 (GitHub); GT-75.

```
run-id: 2026-07-26-api-security-verifier
prompt: "APIs are highly critical — dedicated skill/agent that acts like a verification; reflect #7 and #56's API requirements in the agency."
agents:
  - main session (authoring: agent + skill + README + reconcile)
  - security/red-team-critic (opus, 12,557 tok) — red-teamed the checklist
specs: agents/security/api-security-verifier/{agent.md,SPEC.md}; .claude/skills/api-hardening-review/SKILL.md
verdicts: red-team-critic FAIL on first draft → 17 gaps incorporated → verify.py 14/14 PASS + verify_comms/build_index/audit_skills PASS (APIs are critical, so this got the adversarial gate per #74 — correctly, not over-firing)
commits: (see push)
```

## Done
- **New role `security/api-security-verifier`** (sonnet, read-only Read/Grep/
  Glob/Write) — the dedicated API verification the owner asked for. Runs the
  checklist item-by-item, returns PASS/FAIL/N-A with evidence, hands runtime
  probes to `testing/api-tester` and fixes to the owning implementer. Distinct
  from `appsec-engineer` (SDLC/SAST), `api-platform-engineer` (builds it),
  `senior-secops` (general PR gate).
- **New skill `.claude/skills/api-hardening-review/`** — the checklist itself,
  runtime-fireable at the discovery path. Seeded from #7 (deception/canary,
  8 canary surfaces, polymorphic honeytokens, mTLS+HMAC notary, rolling keys,
  DTOs, BOLA, headers/MOTD, CORS, rate limiting) and #56 (GPS+IP threat
  scoring, ip2location fallback, AES floor, meaningful telemetry) — every
  concrete requirement from both issues is now a checklist item.
- **Red-team pass strengthened it materially.** `security/red-team-critic`
  FAILed the first draft — the checklist was rich where #7/#56 were and blind
  where they were silent (a provenance-shaped gap). Incorporated all 17 gaps:
  rescoped section C to **token validation & revocation** (alg-allowlist /
  `alg:none` / RS256→HS256, `aud`/`iss`/`exp`, `jti`/refresh-reuse — not just
  key custody), added new sections **I (SSRF)**, **J (business-logic/
  concurrency)**, **K (credential endpoints)**, plus mass-assignment,
  request-smuggling, cache poisoning, ReDoS/decompression, prototype pollution,
  SCA, trusted-client-IP, batch/GraphQL cost limits, inbound-webhook + replay
  verification, enumeration-safe responses, and static-CORS. Now targets full
  OWASP-API-Top-10 coverage.

> "an API can PASS every A–H item and still be trivially owned" — `security/red-team-critic` (opus), 12,557 tokens ✓

## Decisions
- **This is the routing model working as designed.** APIs are critical (#74),
  so the checklist — a security control guarding a critical system — earned an
  adversarial review; `red-team-critic`'s literal charter ("presume a
  blue-team control is beaten, find the bypass") fit exactly. That is *not* the
  over-firing #74 flags (a checklist that guards APIs is a critical artifact),
  and it's the first delegated run recorded to the ledger with a measured cost.
- **Agent = who, skill = procedure.** Per skills-policy: the checklist is a
  repeatable procedure (a skill at the runtime discovery path), the verifier is
  the persona that runs it. The agent's coverage enumeration and the skill move
  in lockstep (the red-team's structural note).
- **Reflected, not just filed.** Both issues' concrete requirements are now
  checklist items; #56's geo/telemetry hands implementation to the existing
  `data/device-intelligence-engineer`. Closing both with a requirement→item map.
- **Carried to `pm/project-manager`** (red-team's root-cause note): the
  checklist's coverage claim now outruns its two source issues by design — the
  I/J/K sections are OWASP categories #7/#6 that #7/#56 never mentioned.

## Blocked / carried
- Statically-checkable items (token `alg` allowlist, key-not-in-URL, DTO,
  no-blank-error, static CORS, SSRF egress deny) should become
  `scripts/verifiers/` in a *target* repo (fitness-function pattern) — N/A for
  this meta-repo which has no API.
- #67–72 automation epic: strategies proposed to the owner this turn (not built).
