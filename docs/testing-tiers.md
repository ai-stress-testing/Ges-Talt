<!-- owner: testing/test-automation-engineer · last_validated: 2026-07-26 -->
# Testing tiers — risk-based, cost-aware (#87)

The testing team exists, but the *tiering* that makes CI cost-aware did not.
Testing effort follows **business risk**, not exhaustiveness (issue #77). Four
tiers, each with a time budget and a trigger, mapped onto `scripts/gate.py` /
CI. This is the policy the pipeline enforces (`ci/pipeline-engineer` wires it),
not a test runner.

| Tier | Purpose | Budget | Trigger | Owner |
|---|---|---|---|---|
| **T1 Smoke** | system starts, core workflows function | < 90 s | every commit | `ci/quality-gate-engineer` |
| **T2 Sanity** | the feature the PR changed works | < 5 min | every PR | `testing/test-automation-engineer` |
| **T3 Regression** | existing functionality protected | ~30 min | main branch only | `testing/test-automation-engineer` |
| **T4 Full** | complete platform verification (perf + security + integration + reliability) | daily | scheduled | `testing/reality-checker` |

**In this repo today**, T1 = `scripts/gate.py --check` (the verifier registry,
seconds, every change); the higher tiers are the convention a target repo's
Playwright/E2E suites fill (Playwright preferred wherever a UI/flow is
involved, per #74). The tiering is what the agency hands over; the suites are
built per target.

## Test selection — document what you will NOT test

Every project records its exclusions and the reason:

- Low business risk · Third-party ownership · Duplicate coverage · Excessive
  execution cost · Negligible customer impact.

An untested surface with no recorded reason is a gap; an untested surface with
a recorded reason is a decision. Testing effort follows business risk.

## Flake-budget policy

- **Maximum flake budget: 1%.** Above it, CI confidence is gone.
- A flaky test is **investigated → repaired → replaced → removed**, in that
  order, immediately — never muted and forgotten.
- A **deterministic** failure is a **release blocker** until resolved
  (`docs/templates/release-decision.md`).
- The flake **rate is measured** by `testing/test-results-analyzer`; where a
  target repo emits a machine-readable rate, a `scripts/verifiers/` property
  can assert it stays ≤1% (fitness function, GT-43 style).

## Why tiers and not "run everything"

Running the full suite on every commit burns compute and slows the loop until
people skip it — the opposite of confidence. Cheap high-signal checks gate
early (T1), expensive exhaustive checks run where their cost is justified (T3/
T4). Cost-awareness is the point, mirroring the risk-tiered *review* gate (#74).
