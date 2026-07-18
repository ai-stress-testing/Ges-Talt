# 2026-07-18 — solutions to the Nous-lens review

**Session/agent**: main session (opus).
**Issues touched**: follow-up to #30; backlog GT-32..GT-39.

## Done
- docs/reviews/nous-research-mcp-solutions.md: one solution per finding.
  Shared spine: externalize what's costly to keep resident, load on
  demand, let it compound. #9 (depth×economy) solved as a joint optimum,
  not a tradeoff: L0 terse charter + on-demand L1 DEPTH.md (depth trigger),
  exemplar-encoded depth, compounding external memory — Pareto-superior on
  both axes for a mostly-easy-with-rare-hard workload; self-corrects via
  ledger depth-load frequency.
- Backlog GT-32..GT-39 recorded; cost-triaged (cheap conventions vs real
  builds vs rules riding on the tier mapping).

## Decisions
- Nothing implemented — user asked for solution design, not the build.
- #9's tradeoff dissolved by decoupling depth from per-call residency.

## Blocked / carried
- All GT-32..GT-39 await owner scheduling; PM flow cuts specs on request.
