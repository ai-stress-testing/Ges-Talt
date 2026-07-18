# 2026-07-18 — platform/ dissolved; container agents added

**Session/agent**: main session (opus).
**Issues touched**: backlog GT-25, GT-26.

## Done
- Dissolved platform/ (not a coherent team). Moved all 6 roles to their
  natural homes, preserving each as a distinct role (not folded):
  identity-access-engineer → security; software-architect → logicians;
  i18n-engineer → frontend; codebase-onboarding-engineer → academic;
  technical-writer → design; lifecycle-manager → devops. git mv preserved
  history; frontmatter names + SPEC Team lines + all handoff references
  rewritten (16 files); build_index referential check confirms 0 broken.
- Added devops/containerization-engineer (Docker: parity, hardened images)
  and devops/kubernetes-engineer (probes, limits, rollout gating) — the
  container/orchestration depth the shift-left goal needs: staging parity
  and orchestration health gates catch failure before prod.
- Destination team READMEs updated; roster 78 agents / 14 teams.

## Decisions
- Roles moved, not folded: each platform role was a distinct subclass;
  folding would lose granularity. platform/ was the wrong *grouping*, not
  wrong roles.
- software-architect → logicians: it is the design-time counterpart to
  the review roles, same opus + read-only reasoning discipline.

## Blocked / carried
- None; migration self-contained and lint-verified.
