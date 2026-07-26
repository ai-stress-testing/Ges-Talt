# PRD — <sprint>

**User goal**: the outcome the user wants, in their words, one paragraph max.
**Out of scope**: named explicitly — what this sprint will not do.

## Business case (#85)

- **Customer problem** — the problem being solved, backed by evidence
  (`docs/templates/customer-feedback.md`), not asserted.
- **Expected outcome** — the business result if this ships.
- **Success metrics / ROI** — the numbers that will say it worked, and the
  cost (agent tokens / effort) weighed against them.
- **Strategic alignment** — the direction (`AUDIT.md`) this serves.

## Requirements

Numbered, so issues can cite `prd.md §n`. Each must be **falsifiable** (a
reviewer can check it) and **traceable downstream** to a test/metric
(`docs/traceability.md`).

1. <requirement — falsifiable, not aspirational>
2. …

## Prioritization (#85)

The framework applied (`docs/prioritization.md`: RICE / MoSCoW / Kano) and the
resulting scores/categories — recorded, so priority isn't re-litigated.

## Stakeholder 2×2 (#85)

Classify by Interest × Importance and record the engagement strategy:

| | High importance | Low importance |
|---|---|---|
| **High interest** | Protect & involve | Keep engaged |
| **Low interest** | Keep satisfied | Monitor |

Name who sits in each quadrant for this sprint.

## Risks & assumptions (#85)

- **Risks** — what could make this fail; each links to `docs/risk-register.md`
  with an owner.
- **Assumptions** — what we're taking as true; if one is wrong, which
  requirement breaks.

## Constraints

Technical, timeline, or policy constraints the spec-driven PM must honor when
decomposing (e.g. "no new dependencies", "must stay backward compatible with
X").

## Success criteria

How the sprint as a whole is judged done — checkable, like everything else.
- [ ] …
