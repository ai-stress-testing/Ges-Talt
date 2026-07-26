# Risk Assessment Statement — <release / initiative>

**Owner (A)**: `pm/delivery-lead` · **Date**: YYYY-MM-DD ·
**Traces to**: issue #n · **Feeds**: `docs/risk-register.md`

The executive risk statement attached to a release (issue #77). Every risk
here has a named **accountable owner** — risk acceptance without one is not
acceptance, it's an unowned liability.

## Overall delivery risk

**LOW / MEDIUM / HIGH**, one sentence of why.

## Highest remaining risks

| Risk | Likelihood | Impact | Mitigation | Owner (A) |
|---|---|---|---|---|
| … | L/M/H | L/M/H | … | `team/role` |

## Accepted risks

Risks we ship with, consciously. Each: what it is, why acceptable, who
accepted it (name), and the trigger that would force a re-decision.

## Deferred risks

Risks pushed to a later release, with the issue that carries them.

## Rollback confidence

**HIGH / MEDIUM / LOW** — can we revert safely and fast? Names the mechanism
(`cd/gitops-engineer` revert, `cd/release-engineer` canary halt,
`cd/disaster-recovery-engineer` restore) and when it was last exercised.

## Executive recommendation

One paragraph to the accountable head (`docs/accountability.md`): ship /
ship-with-conditions / hold, and the single most important reason.
