run-id: 2026-07-18-grader-topology
prompt: "Continue — take the now-unblocked backlog (GT-34/35/36)."
agents:
  - logicians/falsifier (opus)         # GT-34 grader independence (self-edit of charter)
  - ai/model-evaluator (sonnet)        # GT-35 grader red-team
  - main/orchestrator (opus)           # GT-36 mesh topology
specs: backlog GT-34/35/36 (from #30 review findings 4/5/6)
verdicts: PASS (build_index/verify_comms/credit all exit 0)
commits: this commit

# 2026-07-18 — grader independence, anti-gaming, mesh topology

**Session/agent**: orchestrator, inline (interrelated convention edits on
shared files — subagents would have collided, so no spawn).

## Done
- GT-34 (#30 finding 4): falsifier grades at arm's length — resolves to a
  different model family than the author, or stamps a correlated-grader
  warning; charter + acceptance criterion.
- GT-35 (#30 finding 5): ai/model-evaluator red-teams the grader on a
  cadence with known-bad/known-good plants, measures false-negative rate;
  charter + criterion + routine row.
- GT-36 (#30 finding 6): ORCHESTRATION topology section — peer handoff
  default, orchestrator only for the arbitration set, measure fan-through.

## Decisions
- Done inline, not via subagents: three small interrelated edits to
  shared files (falsifier, model-evaluator, ORCHESTRATION, routines) —
  parallel agents would have conflicted; the token-cheaper path was one
  orchestrator pass.

## Blocked / carried
- Remaining #30 follow-ups (traces/memory build, tier swap-eval) are real
  builds under GT-32/33 follow-through; GT-6/7/23 still need owner input.
