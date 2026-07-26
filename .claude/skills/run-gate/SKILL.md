---
name: run-gate
description: Run the Ges-Talt roster gate and record the result. Use when finishing substantial work, before committing a roster/docs change, or whenever the verdict loop needs the gate's PASS/FAIL — regenerates the derived files, runs every lint + the verifier registry, and writes the outcome into the sprint-log run-manifest.
---

# run-gate

The exact, repeatable procedure to gate a change in this repo. Not persona,
not knowledge — the steps. Run from the repo root.

## Steps

1. Run the whole pipeline in one command (issue #68):
   ```
   python3 scripts/gate.py          # regenerate (INDEX, personas, repo-map)
                                    # then lint + verifier registry, failures-first
   ```
   It regenerates the derived files in order, then runs `verify_comms`,
   `credit`, `audit_skills`, and `verify.py`; it prints failures first and
   exits non-zero if anything failed. Fail-fast on `build_index` (a red roster
   lint blocks the rest). A FAIL is a to-do, not noise — fix it and re-run
   (regeneration is often the fix). Use `python3 scripts/gate.py --check` to
   verify without regenerating (CI / clean-tree assertion).

2. Record the outcome in the current sprint-log entry's run-manifest header
   (`docs/templates/sprint-log-entry.md`): put the gate result in the
   `verdicts:` field — e.g. `verdicts: build_index PASS; verify.py N/N PASS`.
   An empty `verdicts:` field FAILs `verdict_recorded`; the gate result is
   exactly what belongs there.

## Done when

- Every generator exits 0 and leaves no diff on a second run (idempotent).
- `verify.py` reports all verifiers PASS (or SKIP), exit 0.
- The sprint-log run-manifest `verdicts:` field records the result.
