# Write permissions — path scoping

THREAT-MODEL C3. Tool grants (in each `agent.md`) say *whether* a role can
write; this says *where*. The point: make "the PM writes `docs/` only"
mechanical, not a promise. A role that holds `Write`/`Edit` is still bounded
to its declared paths by the runtime.

Owner: `security/architect` (review), enforced by the runtime harness
permission system + the `build_index.py` tool-boundary lint (C6).

| Role(s) | Writable paths | Notes |
|---|---|---|
| pm/project-manager | `docs/**` only | The documented opus-Write exception in `build_index.py` is *path*-scoped here: specs, backlog, PRD, issue drafts — never code. |
| pm/* (others) | `docs/**` | Plans and records, not code. |
| frontend/*, backend/*, mx/*, ai/* (implementers) | their product source + tests | Not `environments/`, not `scripts/` security tooling, not another team's roster. |
| ci/*, cd/*, networking/* | infra/config + `environments/**` (networking only) | `environments/` is writable by `networking/network-engineer`; changes reviewed by `security/architect`. |
| data/* | pipelines, schemas/migrations | Not app source. |
| logicians/*, academic/*, testing/reality-checker-style reviewers | **none** (read-only) | Findings are returned, not written into the target. Enforced by having no `Edit/Write/Bash` at all (the lint checks this for opus). |
| security/secrets-crypto-engineer | secrets-injection config, crypto config | Never writes secret *material* into the repo (see `secrets.md`). |

Rules:
- `agents/*/agent.md` frontmatter (tools/model) and `scripts/` are writable
  only via a reviewed change — a diff touching them is roster/tooling
  integrity (C6, the tool-widening lint).
- No role writes another team's roster or `environments/`; that's a
  privilege boundary, not a convenience.
- The falsifier/logician finding a bug never edits the fix in — it hands
  back (their charters already say this; this makes it a runtime boundary).
