# 2026-07-26 — Automation epic #67–72: five helper scripts, routed to the roster

**Session/agent**: main session (orchestrator) + `ci/pipeline-engineer` +
`data/data-engineer` (delegated, ledger-recorded).
**Issues touched**: #67 (epic), #68–#72; GT-76…GT-81.

```
run-id: 2026-07-26-automation-epic
prompt: "Proceed with #67-72: separate scripts, provision the environment for PDF extraction."
agents:
  - ci/pipeline-engineer (sonnet, 113,424 tok) — gate.py, ship.py, new_sprint_log.py, backlog.py, _cli.py
  - data/data-engineer (sonnet, 51,384 tok) — extract_text.py, setup-tools.sh
specs: scripts/{gate,ship,new_sprint_log,backlog,extract_text,_cli}.py, scripts/setup-tools.sh
verdicts: gate.py 7/7 PASS (full) + 4/4 (--check); each script self-tested by its author + re-verified inline by the orchestrator. Non-critical tooling → lint/test gate per #74, no falsifier.
commits: (see push)
```

## Done
- **First real fan-out through the now-live roster** (the payoff of #59–#66):
  two owning subagents built the epic in parallel, orchestrator reconciled.
  Owner's two calls honored — **separate scripts** (a minimal shared
  `scripts/_cli.py`, no unified CLI) and **provision the environment** (not
  vendoring a pure-python lib).
- **`gate.py` (#68)** — the marquee. One command regenerates INDEX + personas +
  repo-map, then runs every lint + the verifier registry, failures-first,
  fail-fast on `build_index`. `--check` verifies without regenerating. Collapses
  the ~7 hand-typed bash calls I ran every turn into one. Wired into the
  `run-gate` skill and CLAUDE session-start.
- **`extract_text.py` + `setup-tools.sh` (#69)** — PDF→text with provisioned
  `poppler-utils`/`pdfminer.six`, graceful degradation, actionable error if
  absent. Provisioning succeeded here; **verified live** extracting a real PDF
  (`--pages`/`--out` correct) — the exact failure that started the whole
  introspection (unreadable Rahman PDF) is fixed.
- **`new_sprint_log.py` (#70)** — stamps this very entry (dogfooded). **`ship.py`
  (#71)** — pushes dev + FF-guarded main, never force-pushes. **`backlog.py`
  (#72)** — added GT-76…81 and flipped them done (both verbs dogfooded).
- Wired the tools into `CLAUDE.md` session-start + the `run-gate`/`scaffold-sprint`
  skills so they replace the manual ceremony, not just sit in `scripts/`.

## Decisions
- **Routed, gated by lint/test not falsifier.** These are non-critical tooling,
  so per #74 the gate is each script's self-test + `gate.py`'s own run — I did
  *not* spend the opus falsifier. Two spawns (not five) to avoid cold-start
  cost and file collisions; strict file ownership (subagents wrote only their
  scripts, no git, no shared-file edits) let them run in parallel cleanly.
- **The delegation earned its keep — both agents caught real bugs in their own
  testing.** `data/data-engineer`: a broken `cryptography`/`_cffi_backend`
  raised a `BaseException`-subclass `PanicException` that would have crashed
  `extract_text.py` instead of degrading — fixed by catching `BaseException`
  per import. `ci/pipeline-engineer`: `ship.py` silently dropped the
  already-succeeded branch-push report on a `--main` refusal — fixed with a
  `report()` helper. That is the review discipline working at the subagent
  level, not just the orchestrator's.
- **Both runs recorded in the ledger with measured cost** (51,384 + 113,424
  tok) — the delegation is now a real, credited part of the feedback loop, not
  orchestrator-direct work with nothing to attribute.
- **Honest note on the total spend**: ~165k delegated tokens for five small
  scripts is *more* than inline would have cost — the caveat is real. The
  justification here is the owner's multi-turn intent to exercise the live
  roster plus five genuinely separable deliverables; it is not a template for
  fanning out every task.

## Blocked / carried
- `#67` epic + `#68–72` closed. The scripts now *are* the ceremony; future
  turns use `gate.py` / `new_sprint_log.py` / `backlog.py` / `ship.py` instead
  of hand-typed sequences.
- Still open and offered earlier: `#16` (enterprise-enhancements), `#11`
  (memory-safety), `#53`.
