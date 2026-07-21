# 2026-07-21 — Issues: make the roster executable, not decorative (#59 epic + #60–#66)

**Session/agent**: main session (orchestrator, direct).
**Issues touched**: created #59 (epic) + #60–#66 (sub-issues); GT-59..GT-66 (backlog).

```
run-id: 2026-07-21-roster-executable-issues
prompt: "Generate granular issues from the diagnosis of why none of the agents are being spawned (the framework is decorative in practice)."
agents: main session only (issue authoring; no measured subagent token cost to ledger)
specs: 8 GitHub issues (1 epic + 7 leverage-ordered sub-issues) per docs/templates/issue-spec.md
verdicts: n/a (this run *creates* the verdict-recording infra it can't yet require of itself — see below)
commits: (see push)
```

## Done
- Filed the owner's diagnosis as a decomposed epic. **#59** captures the core
  finding: the org-authoring half works, the org-*orchestration* half is
  bypassed — the roster is documentation about how work should flow while work
  flows straight through the orchestrator, i.e. **decorative in practice**.
- Seven granular sub-issues, leverage-ordered, each with acceptance criteria +
  negative prompt + a narrowest-fit assignee, linked under #59:
  - **#60** install personas as subagents (`scripts/build_personas.py` →
    `.claude/agents/`) + `personas_installed` verifier — the structural
    root cause: this repo has no `.claude/` dir, so 0/105 roles are
    registerable `subagent_type` values.
  - **#61** trigger-oriented `description` frontmatter + lint + roster rewrite.
  - **#62** `CLAUDE.md` routing directive overriding the don't-spawn default.
  - **#63** SessionStart hook injecting the role-routing reminder.
  - **#64** `verdict_recorded` verifier — a major output must record a
    consultation/verdict.
  - **#65** real skills at `.claude/skills/` (run-gate; scaffold-sprint),
    honest YAGNI.
  - **#66** the behavioral fix + the caveat: run the review/adversarial gate
    (`logicians/falsifier`, consultation-proximity, COMMS) as a *real* gate
    even when implementation stays inline — the narrowest, cheapest gap that
    actually cost quality.
- Verified this is not a duplicate (open issues were #56/#16/#11/#7).

## Decisions
- **Epic + linked sub-issues**, not a flat list — matches the PM decomposition
  model (`ORCHESTRATION.md`) and the `issue-spec.md` template (one deliverable,
  one owner, independently verifiable).
- **The caveat is load-bearing, not a footnote.** #59 and #66 both state
  explicitly: the goal is *not* "spawn everything" (cold subagents cost tokens
  and collide on files); it's make the roster *reachable* and the review gate
  *non-skippable*. Framed that way so the fix doesn't read as overreach and get
  ignored — the same failure mode the diagnosis describes.
- **Assignees are real roster roles** so the issues are themselves routable
  once #60 lands: `ci/pipeline-engineer` (build/hook/tooling),
  `ai/multi-agent-systems-architect` (delegation triggering), `pm/*` and
  `logicians/falsifier` (the gate).

## Blocked / carried
- Honest note, and the point of the epic: this very run produced a substantial
  output (8 issues) with **no recorded falsifier verdict / COMMS attribution** —
  because the infra to require it (#64) doesn't exist yet. That's #59 in
  miniature. Implementing #60–#66 is what closes the loop; until then the gate
  stays a discipline, not a mechanism.
- #56 (owner still interpreting data) and #53 remain open and untouched.
