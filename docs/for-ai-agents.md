<!-- owner: design/technical-writer · last_validated: 2026-07-26 -->
# README for AI agents + operational readiness (#88)

`CLAUDE.md` is the operating manual (what you *do* each session). `README.md`
is the philosophy. This is the **third surface the audits found missing**: how
the system is built, how to set it up, and what to do when something breaks —
for a human contributor *or* an AI agent landing in the repo cold. It links
the other two; it does not duplicate them (SSOT).

## Architecture in one screen

- **`agents/`** — the brains. `<team>/<role>/{agent.md,SPEC.md}` (+ optional
  `DEPTH.md`). `agents/INDEX.md` is generated. ~106 roles across 15 teams.
- **`.claude/agents/`** — the generated, runtime-loadable personas
  (`build_personas.py`). This is what makes a role a callable `subagent_type`.
- **`.claude/skills/`** — repeatable procedures (rare; `agents/skills-policy.md`).
- **`.claude/{settings.json,hooks/}`** — the SessionStart routing hook.
- **`scripts/`** — the automation: `gate.py` (the one-command gate),
  `build_*.py` (generators), `verifiers/` (the fitness-function registry),
  and the operator tools (`ship.py`, `new_sprint_log.py`, `new_adr.py`,
  `backlog.py`, `extract_text.py`).
- **`docs/`** — conventions, templates, the backlog, sprints, and the ledger.
  `docs/repo-map.md` is the generated where-is-everything index — read it
  before grepping.

## Environment setup

```
python3 scripts/init_docs.py .     # idempotent docs scaffold
bash scripts/setup-tools.sh        # PDF-extraction toolchain (poppler/pdfminer)
python3 scripts/gate.py            # regenerate + lint + verify (must be green)
```

Stdlib-only Python 3; no third-party runtime deps for the core scripts (that
is the dependency-health posture — a deliberately small surface).

## Common commands

| Do this | Run |
|---|---|
| Full gate (regenerate + verify) | `python3 scripts/gate.py` |
| Verify only (CI / clean-tree) | `python3 scripts/gate.py --check` |
| One verifier | `python3 scripts/verify.py <name>` |
| Start a sprint-log entry | `python3 scripts/new_sprint_log.py <slug>` |
| Record a decision | `python3 scripts/new_adr.py "<title>"` |
| Add/close a backlog row | `python3 scripts/backlog.py add\|done …` |
| Push (dev + guarded main) | `python3 scripts/ship.py [--main]` |

## Troubleshooting

| Symptom | Cause → fix |
|---|---|
| `gate.py` fails on `build_index` | a roster lint (bad model id, tool widening, broken `team/role` handoff). Read the message; fix the `agent.md`; re-run. |
| A verifier FAILs | it's a to-do, not noise. Often regeneration is the fix — run `gate.py` (not `--check`) to regenerate, then re-verify. |
| `verdict_recorded` FAILs | a run-manifest has an empty `verdicts:` — fill it with the gate result. |
| `index_in_sync` / `repo_map_fresh` FAILs | a generated file is stale — `gate.py` regenerates it. |
| `verify_comms` FAILs | an attribution `✓` line's token count doesn't match `docs/agent-ledger.jsonl`, or the line wrapped (it must be one line). |
| `extract_text.py` errors on a PDF | run `bash scripts/setup-tools.sh` to provision poppler/pdfminer. |
| A persona isn't callable | run `gate.py`; `build_personas.py` (re)writes `.claude/agents/`. |

## Repository health

Build/verify status is the `gate` workflow badge in `README.md`; it runs
`gate.py --check` on every push/PR (`docs/testing-tiers.md` T1). License:
MIT (`LICENSE`). Dependency health: stdlib-only core, so the third-party
attack/rot surface is near-zero by construction.
