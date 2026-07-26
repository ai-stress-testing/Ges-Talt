---
name: scaffold-sprint
description: Identify or scaffold the current Ges-Talt sprint and open its log entry. Use at session start or when today falls outside every existing sprint window — ensures the docs scaffold exists, finds the sprint folder covering today (creating the next one if none does), and starts a dated sprint-log entry from the template.
---

# scaffold-sprint

The exact, repeatable procedure to make sure the current sprint exists before
working. Steps only. Run from the repo root.

## Steps

1. Ensure the docs scaffold exists (idempotent):
   ```
   python3 scripts/init_docs.py .
   ```
   In a different target repo: `python3 scripts/init_docs.py /path/to/repo`.

2. Identify the current sprint folder. Sprint folders are named
   `docs/sprint-<m>-<yy>-<dd>-<dd>/` (month, 2-digit year, start day, end day;
   e.g. `sprint-7-26-20-27` = 2026-07-20 → 07-27). Find the one whose window
   covers today:
   ```
   python3 scripts/verify.py sprint_window_current
   ```
   - PASS → today is covered; use that folder.
   - FAIL → today falls outside every window. `init_docs.py` scaffolds the
     next window; re-run step 1 if needed, then confirm `sprint_window_current`
     PASSes before starting work.

3. Open a sprint-log entry for this session from the template:
   ```
   python3 scripts/new_sprint_log.py <slug> [--prompt "..."]   # issue #70
   ```
   This stamps `docs/sprint-<current>/sprint-log/<yyyy-mm-dd>-<slug>.md` from
   the template with the run-manifest header prefilled (run-id, prompt, current
   sprint auto-detected), leaving `verdicts:`/`commits:` as placeholders for
   you to fill. It refuses to overwrite an existing entry. Then write the prose
   (Done / Decisions / Blocked) and fill `verdicts:` before ending substantial
   work.

## Done when

- `scripts/verify.py sprint_window_current` PASSes (a sprint covers today).
- A dated sprint-log entry exists for this session with a run-manifest header.
