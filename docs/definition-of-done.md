<!-- owner: pm/team-operations · last_validated: 2026-07-26 -->
# Definition of Done (#86)

The DoD was **real but distributed** — a reviewer had to reconstruct it from
`WORKFLOW.md`, the verifier registry, `reality-checker`, and the security/
accessibility consultation steps. This is the single named checklist. It
**cross-references** the existing gates; it does not re-implement or duplicate
them (SSOT — issue #76). Owned as an SOP by `pm/team-operations`.

A major output is **Done** when every applicable item holds:

- [ ] **Engineering complete** — the deliverable exists and does what the
      issue's acceptance criteria say (`docs/traceability.md`, forward half).
- [ ] **Code reviewed** — risk-appropriate depth (#74): the
      `logicians/falsifier` "presume wrong" pass for **critical-path** systems
      (auth, API, payments, crypto/secrets, irreversible/data-loss); the
      lint/test gate for everything else. Not both, not neither.
- [ ] **Tests pass** — at the tier the change warrants (`docs/testing-tiers.md`),
      `scripts/gate.py` green.
- [ ] **Traceability closed** — every acceptance criterion terminates in a
      test/metric (`scripts/verify.py traceability`), downstream half.
- [ ] **Docs updated** — and carrying `owner` + `last_validated` where the
      staleness verifier applies (`scripts/verify.py doc_freshness`).
- [ ] **Security consulted** — at spec time for anything consultation-proximate
      (`agents/ORCHESTRATION.md`); APIs ran `api-hardening-review`.
- [ ] **Accessibility verified** — where a UI/flow is involved
      (`testing/accessibility-auditor` / `frontend/section-508-specialist`).
- [ ] **Performance within budget** — where an NFR/SLA applies
      (`testing/performance-benchmarker`).
- [ ] **Verdict recorded** — a `COMMS.md` line + the run-manifest `verdicts:`
      field (`scripts/verify.py verdict_recorded`). Either tier of review
      satisfies this; *some* verdict must exist.
- [ ] **Deployment validated** — for a release, the go/no-go is recorded
      (`docs/templates/release-decision.md`, the `release-readiness` skill).

## Scope

The bar is a **major output** — the same threshold the review gate and the
comprehension quiz (#73) use. A docs typo or a mechanical rename is not gated
by the full list; a substantive change is. When in doubt, it's major.

## Why a checklist and not a new gate

Every item above already has an owner and an enforcement mechanism elsewhere.
This document's only job is to make the set **nameable and reviewable at once**
— so "is it done?" has one answer to point at, not four documents to
reassemble. Changing an item here means changing the gate it references, not
adding a parallel rule.
