---
name: release-readiness
description: Run the go/no-go release gate before shipping a release. Use when cutting a release, tagging a version, promoting to production, or when asked whether something is ready to ship — walks the exit criteria, records a Release Decision + Risk Assessment + Vulnerability Assessments, and produces a GO/NO-GO with a named accountable owner. Owned by cd/release-engineer.
---

# release-readiness

The repeatable procedure that turns "is it ready?" into a recorded GO/NO-GO
(issues #77, #82). Not judgment freeform — a fixed sequence with a decision
artifact at the end. Owned/run by `cd/release-engineer`. Steps only; run from
the repo root.

## Steps

1. **Confirm the gate is green.** `python3 scripts/gate.py --check` must pass
   (lint + verifier registry). A red gate is an automatic NO-GO — stop here
   and fix it.

2. **Check the Definition of Done** (`docs/definition-of-done.md`). Every item
   applicable to this release is satisfied, at the review depth its risk tier
   demands (#74): critical-path systems (auth/API/payments/crypto/irreversible)
   needed the falsifier pass; everything else, the lint/test gate.

3. **Verify downstream traceability** (`docs/traceability.md`). No acceptance
   criterion is left without a passing test/metric. `scripts/verify.py
   traceability` is the machine check.

4. **Collect security findings.** One `docs/templates/vulnerability-assessment.md`
   per significant finding, each with severity, owner, and due date. A
   Critical/High on a critical-path system is a release blocker until mitigated.

5. **Write the Risk Assessment** (`docs/templates/risk-assessment.md`): overall
   risk, top remaining risks, accepted/deferred risks, rollback confidence, and
   the executive recommendation — every risk with a named accountable owner.

6. **Record the Release Decision** (`docs/templates/release-decision.md`): walk
   the blocker checklist, record each gate's result, and write **GO** or
   **NO-GO** with the accountable owner's name and date. A NO-GO names the
   single blocking condition and the issue that tracks clearing it.

7. **Ship or hold.** On GO, `python3 scripts/ship.py [--main]` (never
   force-pushes). On NO-GO, the decision artifact IS the deliverable — hand the
   blocking issue back to its owner.

## Done when

- `gate.py --check` is green and its result is recorded in the Release Decision.
- A Release Decision exists with an explicit GO/NO-GO and a named owner.
- Every significant security finding has a Vulnerability Assessment; every risk
  in the Risk Assessment has an accountable owner.
- The decision is traceable to the release's issue/PRD (SSOT, no re-litigation).
