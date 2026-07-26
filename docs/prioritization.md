<!-- owner: pm/project-manager · last_validated: 2026-07-26 -->
# Prioritization — a documented framework before sub-issues are cut (#85)

Intake was judgment-based with no documented framework. This names the
framework the spec-driven PM (`pm/project-manager`) applies to `docs/backlog.md`
rows **before** decomposing them into sub-issues, so priority is a recorded
score, not a vibe. Pick one framework per initiative and record the numbers.

## RICE (default — for a backlog of comparable items)

`score = (Reach × Impact × Confidence) / Effort`

- **Reach** — how many users/events per period.
- **Impact** — per-user effect (3 massive / 2 high / 1 medium / 0.5 low / 0.25 minimal).
- **Confidence** — % certainty in the estimates (100/80/50).
- **Effort** — person-weeks (or agent-token budget, this repo's real cost).

Higher score = higher priority. The score and its four inputs go in the
backlog row's context or the PRD.

## MoSCoW (for scoping one release)

Categorize each requirement: **Must** / **Should** / **Could** / **Won't
(this release)**. "Won't" is a decision, recorded, not an omission.

## Kano (for feature-set shaping)

Classify features as **Basic** (expected; absence hurts), **Performance**
(more is better), or **Delight** (unexpected upside). Balances the release so
it isn't all table-stakes or all novelty.

## The rule

- **One framework, recorded, per initiative.** The choice and the resulting
  scores/categories are written down (backlog context or PRD §), so a later
  session doesn't re-litigate priority (`docs/feedback-loop.md`).
- **Effort is measured in this repo's real currency** — agent tokens
  (`docs/agent-ledger.jsonl`, `docs/credit.md`) — not abstract story points,
  wherever the RICE Effort term applies to delegated work.
