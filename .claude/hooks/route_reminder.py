#!/usr/bin/env python3
"""SessionStart hook (GT-63): reinject the roster-routing discipline.

Claude Code adds this script's stdout to the session context at start, making
the routing directive a runtime event instead of a CLAUDE.md line the session
can quietly skip (issue #59). No network, no deps — stdlib print only. The
authority is CLAUDE.md's "Routing" section; this is the nudge that points at
it every session.
"""
print(
    "Roster-routing check (Ges-Talt): before acting on a non-trivial task, "
    "name which roster role owns it (agents/INDEX.md, docs/repo-map.md) and "
    "route to that subagent unless it's a single-file/tightly-coupled change. "
    "Before shipping a major output, record a RISK-APPROPRIATE verdict (#74): "
    "the logicians/falsifier disproof pass for CRITICAL systems only (auth, "
    "API, payments, crypto/secrets, irreversible/data-loss ops); for "
    "lower-risk work the lint/test gate stands in (scripts/verify.py + "
    "testing/, Playwright E2E for UI/flows — use it in more cases). Either "
    "way write a COMMS.md line + the run-manifest verdicts: field. Don't spend "
    "the opus falsifier on a routine change a linter covers; don't ship a "
    "major output with no verdict. See CLAUDE.md 'Routing'."
)
