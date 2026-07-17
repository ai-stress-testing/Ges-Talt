# Journey: developer — ship a feature through the agent org

**Actor**: the repo owner (or a session acting for them).
**Trigger**: a feature/goal stated in one or two sentences.
**Outcome**: merged work whose issues trace to a PRD, with evidence.

## Steps

| # | Actor does | System responds | Failure mode to design for |
|---|---|---|---|
| 1 | States a goal | Session ensures docs scaffold exists (`init_docs.py`), PM reads `prd.md` + journeys | No PRD yet — PM drafts one from the goal and asks, not assumes |
| 2 | Approves scope | Spec-driven PM writes issue spec (template), cuts issues + granular sub-issues with assignee, AC, negative prompt | Sub-issue too broad — split until one owner, one deliverable |
| 3 | — | Assigned subagents implement per their `agent.md` + the ladder | Agent drifts outside negative prompt — reviewer flags against spec |
| 4 | — | logicians review statically; testing verifies empirically; reality-checker gates | Green-washed "done" without evidence — reality-checker re-runs it |
| 5 | Reviews outcome | Sprint-log entry written; backlog rows flipped to done | Log skipped — next session loses decisions; steward flags |

## Notes

Exercises `prd.md` §5–6. Open question: verdict/retry protocol between
testing and implementers is still convention-by-prose (AUDIT.md gap #1).
