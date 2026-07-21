# 2026-07-21 — Introspection → issues: automate the mechanical ceremony (#67 + #68–#72)

**Session/agent**: main session (orchestrator, direct).
**Issues touched**: created #67 (epic) + #68–#72; GT-67..GT-72.

```
run-id: 2026-07-21-automate-ceremony-issues
prompt: "Run introspection — what am I doing that a script could do / that wastes tokens? Generate issues."
agents: main session only (introspection + issue authoring; no measured subagent token cost to ledger)
specs: 6 GitHub issues (epic + 5 leverage-ordered children) per docs/templates/issue-spec.md
verdicts: falsification pass on the candidate list (below); gate PASS (see commits)
commits: (see push)
```

## Done
- Introspected this session's recurring token sinks and filed the real ones as
  an epic + 5 children:
  - **#68** `scripts/gate.py` — the marquee: the end-of-turn pipeline is ~7
    hand-typed bash calls in a fixed order, *every turn*. One command collapses
    it. The `run-gate` skill documents the steps; nothing executes them.
  - **#69** `scripts/extract_text.py` — PDF→text (the owner's example, hit live
    this session on the Rahman PDF: `pdftoppm`/`pdfminer` absent → a WebFetch +
    failed Read + failed extraction + memory fallback).
  - **#70** `scripts/new_sprint_log.py` — the run-manifest header boilerplate,
    retyped each substantial turn.
  - **#71** `scripts/ship.py` — the push retry-loop + `main` fast-forward,
    retyped each turn.
  - **#72** `scripts/backlog.py` — row add / status flip (filed honestly as the
    weakest: the row *content* is prose, so the savings are marginal).

## Decisions
- **Ran the adversarial pass on my own candidate list** ("presume this is
  padded — which of these aren't real waste?"). Survivors and why:
  - gate.py, extract_text: strong — observed directly, high frequency /
    high-severity failure mode. Kept.
  - new_sprint_log, ship: medium — identical boilerplate every turn, mechanical
    scaffold vs. prose content. Kept.
  - backlog.py: weakest — only saves table formatting, not the prose. Kept but
    labeled lowest-priority in the issue title itself, rather than dropped or
    dressed up.
  This is the falsification the #66 discipline requires, applied to an
  introspection instead of code.
- **Scoped out the judgment.** Non-goals in the epic: do not script issue
  decomposition, sprint-log/COMMS prose, or the review reasoning itself — a
  script that needs per-call judgment to drive it saves nothing.
- **A meta-observation worth its own note (not filed):** the GitHub
  `sub_issue_write` MCP tool returns the entire repository object on every
  call — ~1.5 KB of irrelevant JSON × 5 links this turn. That's a real token
  sink I *can't* script away (it's the tool's response), but future GitHub
  reads should pass `minimal_output: true` where supported.

## Blocked / carried
- These are `todo` — filed, not implemented (the ask was to generate issues).
  #68 is the highest-leverage first build (every turn pays for its absence).
- #56 (owner still interpreting data) and #53 remain open.
