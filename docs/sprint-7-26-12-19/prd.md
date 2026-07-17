# PRD — sprint-7-26-12-19

**User goal**: A personal staging environment of token-efficient,
project-subclass-driven subagents (brains) with the environment substrate
(hands) to run them — organized like enterprise teams, not features.
**Out of scope**: environments/ build-out (MCP tunnels, allowlists,
session reaping) — deferred to next sprint; hyper-specialized
critical-systems agents — owner will add them next.

## Requirements

1. Repo split into `agents/` and `environments/` with a per-role
   `agent.md` + `SPEC.md` convention and a template.
2. agency-agents divisions (academic, design, project-management,
   security, testing, engineering-split) converted into lean,
   enterprise-reframed teams.
3. Ponytail method baked into implementer roles; YAGNI phrasing in
   architecture/review roles; guardrail roles exempt.
4. Generated agent index with roster lint (pairs, frontmatter,
   opus-tool-boundary).
5. Docs convention: `docs/backlog.md` + `sprint-<m>-<y>-<dd>-<dd>/`
   containing `prd.md`, `sprint-log/`, `user-journeys/`; scaffolded by
   `scripts/init_docs.py`; templates in `docs/templates/`.
6. Spec-driven PM: opus-tier `pm/project-manager` that turns a user goal
   plus sprint docs into granular issues/sub-issues, each with an
   assigned subagent, checkable acceptance criteria, and a negative
   prompt, per `docs/templates/issue-spec.md`.

## Constraints

- Cheapest-sufficient model per role; opus never holds Edit/Bash (Write
  allowed only for the spec-driven PM, docs-scoped, as a documented lint
  exception).
- No install/CI tooling until the roster is big enough to drift (CI on
  the lint is now the next natural step — see AUDIT.md).

## Success criteria

- [ ] `python3 scripts/build_index.py` exits 0.
- [ ] `python3 scripts/init_docs.py .` reports nothing to do on this repo.
- [ ] Every requirement above traceable to committed files on the sprint
      branch.
