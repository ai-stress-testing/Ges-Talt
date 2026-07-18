# Ges-Talt — session operating manual

Agent org + docs conventions for this repo (and any repo adopting it).
Read `README.md` for philosophy; this file is what you *do*.

## On session start

1. Ensure the docs scaffold exists: `python3 scripts/init_docs.py .`
   (idempotent; safe to run every session). In a different target repo:
   `python3 scripts/init_docs.py /path/to/repo`.
2. Identify the current sprint folder: `docs/sprint-<m>-<y>-<dd>-<dd>/`
   (month, 2-digit year, start day, end day — e.g. `sprint-7-26-12-19`
   = 2026-07-12 → 07-19). If today falls outside every sprint window,
   scaffold the next one before starting work.

## Docs convention

- `docs/backlog.md` — one table row per issue; the spec-driven PM owns it.
- `docs/sprint-*/prd.md` — the sprint's requirements; issues cite `§n`.
- `docs/sprint-*/sprint-log/` — one dated entry per working session
  (template: `docs/templates/sprint-log-entry.md`). Write one before
  ending substantial work; decisions recorded there are not re-litigated.
- `docs/sprint-*/user-journeys/` — one file per journey
  (template: `docs/templates/user-journey.md`).

## Workflow (spec-driven)

A user goal enters through `agents/pm/project-manager` (opus,
spec-driven): it reads/drafts the PRD, writes an issue spec per
`docs/templates/issue-spec.md`, and cuts issues + granular sub-issues —
every sub-issue has one assignee from `agents/INDEX.md`, checkable
acceptance criteria, and a negative prompt. Implementation flows to the
assigned agents; static review is `agents/logicians/`, empirical
verification `agents/testing/`, security `agents/security/`. Don't hand
work to an agent outside its charter — check the index first. See
`agents/WORKFLOW.md` for the verdict loop (PASS/FAIL handback, retry
cap, escalation) and PM delegation rules.

## Roster rules

- Agents live in `agents/<team>/<role>/` as `agent.md` + `SPEC.md`
  (template: `agents/TEMPLATE/`).
- After adding/changing agents: `python3 scripts/build_index.py` must
  exit 0 (it regenerates `agents/INDEX.md` and lints the roster — opus
  never holds Edit/Bash; Write only via documented exception).
- Model policy: cheapest sufficient. Opus = reasoning-bound roles only.
