# Enterprise Doc — Ges-Talt

This doc UPDATES OVER TIME. The spec-driven PM (`agents/pm/project-manager`)
classifies new work against it during decomposition and extends it when a
decomposition reveals a concept, tier, class, or term that isn't here yet.
Stale entries are deleted, not preserved — this is a living reference, not
an append-only log.

## Tiering

- **Strategic** — the repo owner (human), plus `AUDIT.md` and each sprint's
  `prd.md`: sets direction, names weaknesses/invariants to hold, states
  what a sprint will and won't do.
- **Tactical** — the `pm/` team, specifically `pm/project-manager`
  (spec-driven decomposition into issues/sub-issues) governed by
  `agents/WORKFLOW.md`'s verdict loop (PASS/FAIL, retry cap, escalation)
  and its delegation rules (route by altitude: `delivery-lead` for
  portfolio tradeoffs, `program-tracker` for multi-sprint milestones).
- **Operational** — the implementer teams (backend, frontend, data,
  ci, cd, ai, mobile, networking, security-implementers) plus
  `logicians/` (static review) and `testing/` (empirical verification),
  each executing against acceptance criteria a sub-issue already fixed.

## Ontology

- goal —(enters through)→ `pm/project-manager`
- goal —(is stated by)→ PRD (`docs/sprint-*/prd.md`)
- PRD —(is decomposed into)→ issue (`docs/templates/issue-spec.md`)
- issue —(is decomposed into)→ sub-issue (one deliverable, one owner)
- sub-issue —(is assigned to)→ agent (one, from `agents/INDEX.md`)
- implementer agent —(produces)→ diff/artifact
- `logicians/*` —(statically reviews)→ diff/artifact
- `testing/*` —(empirically verifies)→ diff/artifact
- `testing/reality-checker` —(re-verifies)→ other testing agents' evidence
  —(issues)→ verdict (final gate)
- attempt 4 FAIL —(escalates to)→ `pm/project-manager`
- agent —(belongs to)→ team —(is bound by)→ charter (`agent.md` + `SPEC.md`)
- agent —(is scoped by)→ tool boundary (its `tools:` frontmatter list)
- `agents/` (brains: personas, models, prompts) —(is distinct from)→
  `environments/` (hands: where an agent runs, what it can reach —
  deferred past Sprint0)

## Taxonomy

- Teams (15): academic, ai, backend, cd, ci, data, design, frontend,
  legal, logicians, mx, networking, pm, security, testing
  — see `agents/INDEX.md` (generated, 100 agents total).
- Role kinds (by tool grant, not team):
  - **implementer** — Read/Edit/Write/Bash(+Grep/Glob); ships diffs
    (e.g. `backend/backend-dev`, `frontend/react-dev`, `cd/sre`).
  - **advisory-read-only** — Read/Grep/Glob only, no Write/Edit/Bash;
    reviews or consults without blast radius (e.g. all of `academic/`,
    `security/architect`, `legal/general-counsel`).
  - **opus-reasoning** — the 7 opus-model roles, reasoning depth over
    tool breadth: `academic/statistician`, `logicians/code-reviewer`,
    `logicians/logician`, `legal/general-counsel`, `security/architect`,
    `logicians/software-architect`, `pm/project-manager` (the one opus
    role with a documented Write exception, docs-only).
- Artifact types: `agent.md` (loadable subagent contract), `SPEC.md`
  (human-readable role card), PRD (`docs/sprint-*/prd.md`), issue-spec
  (`docs/templates/issue-spec.md`), sprint-log entry
  (`docs/templates/sprint-log-entry.md`), threat model
  (`environments/THREAT-MODEL.md`).

## Semantics

- **Negative prompt** — the explicit "do NOT" list on a sub-issue: files/
  systems it must not touch, abstractions/dependencies it must not
  introduce, scope it must not absorb. Mandatory on every sub-issue the
  PM cuts.
- **Verdict** — the outcome of the review→verify cycle. Exactly PASS or
  FAIL, never a score or "PASS with notes" (`agents/WORKFLOW.md` §1).
- **Ladder / Method** — the implementer's stop-at-the-first-rung-that-
  holds sequence: (1) does this need to exist? (2) reuse what's already
  in the codebase (3) stdlib/native/already-installed dependency before
  new code (4) only then the shortest working diff. Baked into every
  implementer `agent.md`.
- **"True to code"** — a claim (privacy, compliance, docs) is verified
  against what the codebase actually does, with file:line evidence —
  never accepted on the strength of a policy doc or stated intent alone.
- **Cheapest-sufficient** — model policy: pick the cheapest model tier
  that can do the role's job; opus is reserved for reasoning-bound roles,
  not handed out by default (`CLAUDE.md`).
- **Granularity rule** — a sub-issue is one deliverable, one owner,
  independently verifiable. If it needs two agents or two deliverables,
  split it again.
- **Tool boundary** — the least-privilege tool list in an agent's
  frontmatter; an agent only gets Edit/Write/Bash if its job requires
  producing or running something, never by default.
