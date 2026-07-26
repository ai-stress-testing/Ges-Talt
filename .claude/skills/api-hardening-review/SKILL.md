---
name: api-hardening-review
description: Verify an API against the org's hardening checklist before it ships. Use when reviewing, verifying, or signing off an API surface (APIs are critical-path per issue #74) — authorization/BOLA, transport/crypto, token validation & revocation, input/output hygiene, headers & routing, rate limiting, geo threat-scoring, deception/canary, SSRF, and business-logic/concurrency. Seeded from issues #7 and #56, extended to full OWASP-API coverage by a red-team pass. Run it item by item; each item gets PASS / FAIL / N-A with file:line or probe evidence.
---

# API hardening review

The repeatable verification an API passes before it ships. APIs are a
critical system (issue #74), so this checklist is a required gate, not
advice. Owned/run by `security/api-security-verifier`.

Seeded from owner issues #7 (deception/canary) and #56 (geo/telemetry), then
extended by a `security/red-team-critic` pass that FAILed the first draft for
a provenance-shaped blind spot — it was strong where those issues were and
silent where they weren't. Sections I–K and the token-validation / smuggling /
cache / mass-assignment items below close that gap toward full OWASP-API-Top-10
coverage.

## How to run

- Walk every item. Mark each **PASS** (with file:line or a probe result as
  evidence), **FAIL** (with the concrete gap), or **N-A** (with why). A PASS
  with no evidence is not a PASS.
- **Static items** you check by reading code/config. **Probe items** (⟿)
  require hitting a running endpoint — hand those to `testing/api-tester` and
  record its result here.
- Report failures first, each with the owning fix role (see the verifier
  charter). Adversarial depth on one control → `security/red-team-critic` /
  `logicians/falsifier`.

## A. Authorization — the core (OWASP API #1/#5)

- [ ] **Object-level authz (BOLA/IDOR)**: an identity cannot reach another's
      object by changing an id in path/body — "user calls for 101, edits URL
      to 102" is denied. ⟿ fuzz object ids across identities.
- [ ] **Function-level authz**: privileged routes reject non-privileged
      callers; no route ships without an auth guard except an explicit allowlist.
- [ ] **Least privilege, no privilege creep**: tokens carry minimum scope;
      scope is re-checked per request, not just at login.
- [ ] **Allowlist over denylist** for what a caller/route may do.

## B. Transport & inter-service trust

- [ ] **mTLS > TLS, always** service-to-service; no plaintext internal
      traffic. ⟿ confirm mutual auth on internal calls.
- [ ] **Cipher floor**: AES-256 preferred, **AES-128 minimum**; TLS 1.2+ only.
- [ ] **Cryptographic notary**: a receiving service verifies an **HMAC** (+ OPA
      policy) signed with a shared secret — the "passport" — instead of
      trusting forwarded data. Don't over-send data to every service.
- [ ] **Replay resistance on the notary**: signed inter-service messages carry
      a **nonce + timestamp inside the signed payload**; the receiver rejects
      stale (outside a small window) or already-seen nonces. (Signing without
      freshness = a captured request is replayable forever.)
- [ ] **Inbound webhook/callback verification**: webhooks the API *receives*
      are authenticated by HMAC over the **raw body + timestamp**, constant-time
      compared, replay-windowed. (Unverified inbound = forged "payment succeeded".)

## C. Token issuance, validation & revocation

*(Key custody is section B/`secrets-crypto-engineer`; this is the token itself.)*

- [ ] **Signature validation**: token verified against a **pinned algorithm
      allowlist** — reject `alg:none`, reject RS256→HS256 confusion (public key
      as HMAC secret); `kid`/`jku`/`x5u` are **not** attacker-controllable.
- [ ] **Claim validation**: `aud`, `iss`, `exp`, `nbf`, and signature are all
      checked server-side (not just decoded).
- [ ] **Placement**: key/token rides in `X-API-Key` or `Authorization: Bearer`
      — **never** in URL/query or logs.
- [ ] **Rolling over static**: short-lived OAuth (~5 min/as-needed), automatic
      rotation, **overlapping validity windows** for blue/green rollouts.
- [ ] **Revocation**: a compromised token can be killed **before expiry**
      (denylist/`jti` or short session ref-check); refresh tokens are
      single-use with **reuse detection** that revokes the token family.
- [ ] **No secret to the client**: no key/secret shipped in the client bundle
      (e.g. a var that lands in the Next.js client build).

## D. Input / output hygiene

- [ ] **Output DTOs**: return only contract-promised fields — never the whole
      row (no leaked `password_hash`, internal flags, PII).
- [ ] **Mass-assignment / writable-field allowlist**: input binding uses an
      explicit *writable* allowlist per role; **privileged/ownership fields**
      (`role`, `isAdmin`, `*_id` FKs, balances, status flags) are non-bindable
      from the body. (Rejecting *unknown* fields does not stop binding a known
      privileged one.)
- [ ] **No verbose error leakage**: a 5xx never returns stack trace, internal
      hostname, SQL, or PII. ⟿ send malformed input, scan the body.
- [ ] **Input validation is allowlist**, rejects unknown fields, caps size and
      **nesting depth**; no injection sink takes raw input.
- [ ] **Algorithmic-DoS**: no user-influenced input hits a
      catastrophic-backtracking regex (ReDoS); decompressed bodies are
      size-capped (gzip/zip bomb); XML external-entity expansion disabled.
- [ ] **Deserialization / prototype pollution**: JSON merges reject
      `__proto__`/`constructor`/`prototype`; no native/polymorphic
      deserialization of untrusted input.
- [ ] **Enumeration-safe responses**: auth and existence-revealing endpoints
      return a **uniform response and timing** whether or not the subject
      exists ("user not found" vs "wrong password" is an oracle) — reconciles
      the "contextful error" rule (E) with no-leak.
- [ ] **SAST + SCA in CI**: static analysis on own code **and** a
      software-composition gate on dependencies (known-CVE + lockfile
      integrity + provenance). Hand to `ci/code-security-analyst` /
      `ci/supply-chain-engineer`.
- [ ] **Consistent, minimal responses**: consistent envelope, bounded
      pagination, RESTful endpoints, explicit **versioning**, **idempotency
      keys** on mutations, webhooks where async.

## E. Errors, headers & routing

- [ ] **No blank/empty responses or headers** — "a smoke alarm that beeps once
      is no good": every error carries **concise, contextful** info the caller
      can act on. Never a bare status with no context.
- [ ] **Correct status codes**: contextful **400** on bad input, **401/403** on
      authz, **402** on billing/limit, **429** on rate — code matches cause.
- [ ] **Request-smuggling / desync**: the gateway (which enforces A's auth) and
      the origin **agree on message framing** — reject ambiguous/duplicate
      `Content-Length`+`Transfer-Encoding`. (Disagreement smuggles a request
      *past* every authz guard.)
- [ ] **Cache safety**: authenticated/personalized responses are
      `Cache-Control: private/no-store`; cache keys include all
      response-affecting inputs; no static-suffix path confusion
      (`/account/x.css` served as `/account`).
- [ ] **CORS is a static whitelist**: never reflect `Origin` into
      `Access-Control-Allow-Origin`, never allow `null`, never combine
      credentials with a wildcard/reflected origin.
- [ ] **Header discipline**: headers/extended/URL headers used deliberately;
      **header routing** where it applies; **MOTD** channel; no
      traditionally-blank HEAD requests; security headers present.

## F. Rate limiting & abuse

- [ ] **Rate limiting** with an **allowlist-vs-denylist** model and proper
      **402/429** throws; per-identity and per-route caps; no unbounded scrape.
- [ ] **Trusted client-IP**: client-supplied `X-Forwarded-For`/`X-Real-IP` are
      stripped/overwritten at the trust boundary; rate-limit **and** geo (G)
      identity derive only from the connection peer or a trusted proxy chain.
      (Otherwise header rotation resets limits and spoofs geo.)
- [ ] **Batch/GraphQL cost limits**: batched requests (op arrays, GraphQL
      aliasing/depth) are cost-limited and rate-limited **per operation**, not
      per HTTP call; introspection disabled in prod. (One batched call
      otherwise defeats per-request rate *and* BOLA counting.)
- [ ] **Meaningful telemetry** (#56): the API emits data rich enough that
      anomalous/abusive call patterns are visible, not silent.

## G. Geo threat-scoring (#56)

- [ ] **GPS + IP threat scoring**: score/ban on geo; compare browser GPS to the
      IP's location and flag mismatch. Impl → `data/device-intelligence-engineer`.
- [ ] **Fallback**: GPS unavailable → **ip2location / ipapi**.
- [ ] **Datacenter/VPN/proxy** IPs detected and de-prioritized/banned
      (owned by `data/device-intelligence-engineer`).

## H. Deception & canary layer (#7)

- [ ] **Canary/honey tokens** across the 8 surfaces — **file, credential, API,
      DNS, cloud, email, database, network** — with **alerting on any access**
      ("canary + coal mine").
- [ ] **Probabilistic + deterministic = full coverage**: ML anomaly detection
      *and* binary canary tripwires; the tripwire removes ambiguity.
- [ ] **Polymorphic honeytokens** with organization-mimicry (plausible names/
      hashes/directories) so decoys aren't obvious.
- [ ] **Sentinel-monitored deception segment**; alerts route to
      `security/threat-detection-engineer` → `security/incident-responder`.

## I. Server-side fetch & SSRF (OWASP API #7)

- [ ] **Egress allowlist on user-driven fetches**: any endpoint fetching a
      caller-supplied URL (webhook target, image/PDF/link-preview, import-from-URL)
      resolves against an allowlist; **deny link-local / RFC1918 /
      `169.254.169.254` metadata**; block redirect-to-internal; disable unused
      URL schemes. (SSRF pivots *through* the trusted B mesh — the fetcher
      already holds the mTLS cert / HMAC secret.)

## J. Business-logic & concurrency (OWASP API #6)

- [ ] **Atomic state changes**: operations on funds/quotas/coupons/one-time
      resources are **atomic** (row lock / conditional update / compare-and-swap),
      safe under concurrent identical requests. (Rate limits and idempotency
      keys do **not** stop a distinct-key parallel race → double-spend,
      coupon re-redemption, limit bypass.)
- [ ] **Multi-step flow integrity**: a business flow can't be completed out of
      order or with a step skipped (ship-before-pay, etc.).

## K. Credential & auth endpoints

*(The whole checklist verifies token auth; this verifies the endpoints that MINT tokens.)*

- [ ] **Anti-automation on credential endpoints**: login/reset/OTP have
      dedicated brute-force/credential-stuffing throttling (distinct from F).
- [ ] **Reset/OTP tokens**: high-entropy, single-use, short-expiry.
- [ ] **Step-up / MFA** on privileged or sensitive operations.

## Verdict

A critical API is signed off only when every applicable item is PASS or a
justified N-A, with FAILs handed to their fix roles. Statically-checkable
items (token `alg` allowlist, key-not-in-URL, DTO present, no-blank-error,
CORS static whitelist, SSRF egress deny) should be promoted to
`scripts/verifiers/` in a target repo so the gate runs every build, not just
on review (the fitness-function pattern, `docs/fitness-functions.md`).
