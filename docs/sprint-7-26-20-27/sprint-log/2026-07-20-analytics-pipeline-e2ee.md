# 2026-07-20 — Analytics/device-intelligence pipeline (#55) + E2EE protocol consultant (#57)

**Session/agent**: main session (orchestrator, direct).
**Issues touched**: #55, #57 (GitHub); GT-55, GT-57 (backlog).

```
run-id: 2026-07-20-analytics-pipeline-e2ee
prompt: "Implement issues 55 and 57."
agents: main session only (role authoring, direct; no measured subagent token cost to ledger)
specs: 3 new roles (agent.md + SPEC.md) + 1 DEPTH.md + team-README/ORCHESTRATION wiring
verdicts: build_index PASS (103 agents, 15 teams), verify.py 10/10 PASS, verify_comms/credit/audit_skills exit 0
commits: (see push)
```

## Done
- **#55 — advanced analytics pipeline v1**, two roles split client/server, with
  privacy guardrails as first-class (this is dual-use — device intelligence for
  fraud/bot detection is legitimate; covert tracking is not):
  - `frontend/client-telemetry-engineer` — consent-gated client collection:
    stateless + stateful IDs (cookies, IndexedDB/localStorage), the device-signal
    set (navigator/hardwareConcurrency/deviceMemory/OS, canvas text+polygon+CSS
    hash, WebGL `WEBGL_debug_renderer_info`, AudioContext oscillator→compressor
    floats) at ≥50% navigator coverage, and async encrypted transmission
    (sendBeacon/pixel, ECDH-to-collector).
  - `data/device-intelligence-engineer` — server side: stable device-ID
    resolution (stateful ⋈ stateless), IP intelligence (regional blocks,
    DNS-routing, datacenter/VPN detection → drop), and calibrated ML fraud
    scoring (canvas/WebGL-vs-UA mismatch flags). IP/PII encrypted at rest,
    fraud-scoped, retention-bounded.
- **#57 — crypto normalization**, one consultant:
  - `security/e2ee-protocol-consultant` — asynchronous E2EE to the Signal
    paradigm: X3DH/PQXDH handshake (identity + signed + one-time prekeys, DH
    mix), Double Ratchet (symmetric chain = forward secrecy; DH ratchet =
    post-compromise security), Sesame multi-device, HKDF discipline
    (salt→PRK→OKM with zeroization), and offline deniability. Carries a
    `DEPTH.md` (worked PQXDH handshake, ratchet transitions, deniability
    argument) — the depth-pack pattern's natural home for dense protocol detail.
- Wired `e2ee-protocol-consultant` into the ORCHESTRATION on-demand consultant
  list; updated frontend/data/security READMEs; refreshed tools-baseline;
  regenerated INDEX (100→103) + repo-map; bumped enterprise.md count.

## Decisions
- **#55 is built consent-first, not tracking-first.** Every collecting role is
  gated on a lawful basis that `legal/privacy-engineer` + `legal/data-protection-officer`
  own; fingerprinting is scoped to first-party analytics and fraud/bot
  detection. Explicit negative prompts forbid evercookie/respawn of deleted
  IDs, evading user privacy controls, and third-party cross-site tracking —
  the same "authorized-scope" bounding the pentester role uses. A fingerprinting
  role that ignores consent is scoped wrong, not under-powered.
- **#57 stays in its lane vs the existing crypto roles.** `pq-crypto-consultant`
  already owns hybrid *key exchange*; `secrets-crypto-engineer` owns key
  lifecycle + implementation. The new role owns only the *protocol* between
  them (handshake state machine, ratchet, session management, deniability) and
  calls into both — no duplication.
- **DEPTH.md for the protocol, not a bigger charter.** The Signal-suite detail
  is high-stakes but not every-call; it lives in L1, loaded on a depth trigger,
  keeping the resident charter lean (`docs/depth-packs.md`).
- **"repudiation for users, but not intercepted attackers"** is implemented as
  offline deniability (shared-key MAC auth, no content signature) with online
  authenticity from the handshake — captured in the DEPTH exemplars so a weaker
  pass doesn't "add a signature for authenticity" and destroy it.
- **No ledger rows** — orchestrator-direct work, no measured token cost.

## Blocked / carried
- Issue #56 not addressed (user scoped to 55 + 57).
- Natural follow-ups: a `reason`-method verifier asserting no fingerprint is
  computed pre-consent (#55), and the encryption hard-verifiers (nonce
  uniqueness, no banned primitive) run against any #57 implementation.
