"""Assert authored governance docs carry a fresh owner/last_validated marker (#89).

Generated files have freshness verifiers (index_in_sync, repo_map_fresh,
personas_installed); hand-authored convention docs did not, so one could rot
while claiming to be current (docs/doc-metadata.md). This closes that half.

Two fail-closed properties:

1. **Presence** — every GOVERNED doc (the convention/policy docs that steer
   behavior) carries a first-line marker:
       <!-- owner: <team/role> · last_validated: YYYY-MM-DD -->
   A governed doc missing the marker is the counterexample.
2. **Freshness** — every doc CARRYING the marker (governed or not) has a
   well-formed date no older than HORIZON_DAYS. A malformed or stale date is
   the counterexample.

Never SKIPs on an empty governed set — an empty match is a FAIL (the _lib
repo_root off-by-one class of bug that once produced a false PASS). Templates
(their own in-body 'Last validated' field), sprint-log entries (immutable
history), and generated files are exempt by construction: the governed set is
an explicit allow-list, so exemption is the default.
"""
import datetime
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _lib  # noqa: E402

PROPERTY = "Every governed doc carries an owner/last_validated marker no older than 180 days."
METHOD = "static"
OWNER = "pm/team-operations"
HORIZON_DAYS = 180

# The governed set (docs/doc-metadata.md). Explicit allow-list so exemption is
# the default: generated files, sprint logs, and templates are simply not here.
GOVERNED = [
    "docs/traceability.md",
    "docs/blueprinting.md",
    "docs/prioritization.md",
    "docs/definition-of-done.md",
    "docs/testing-tiers.md",
    "docs/risk-register.md",
    "docs/accountability.md",
    "docs/for-ai-agents.md",
    "docs/doc-metadata.md",
    "docs/model-tiers.md",
]

MARKER_RE = re.compile(
    r"<!--\s*owner:\s*(?P<owner>[^·|]+?)\s*[·|]\s*last_validated:\s*"
    r"(?P<date>\d{4}-\d{2}-\d{2})\s*-->"
)
# A marker whose date is malformed still needs to be caught, so match the
# whole comment loosely too.
LOOSE_MARKER_RE = re.compile(r"<!--\s*owner:.*?last_validated:\s*(\S+?)\s*-->")


def check():
    _lib.in_repo_root()
    today = datetime.date.today()
    horizon = today - datetime.timedelta(days=HORIZON_DAYS)
    problems = []
    checked = 0

    for rel in GOVERNED:
        if not os.path.exists(rel):
            problems.append(f"{rel} — governed doc missing (create it or drop it from GOVERNED)")
            continue
        head = open(rel, encoding="utf-8").read(400)
        m = MARKER_RE.search(head)
        if not m:
            if LOOSE_MARKER_RE.search(head):
                problems.append(f"{rel} — marker present but date is malformed (want YYYY-MM-DD)")
            else:
                problems.append(f"{rel} — no owner/last_validated marker (docs/doc-metadata.md)")
            continue
        checked += 1
        d = datetime.date.fromisoformat(m.group("date"))
        if d < horizon:
            age = (today - d).days
            problems.append(f"{rel} — last_validated {d} is {age}d old (> {HORIZON_DAYS}d); re-read and bump")

    if not GOVERNED:
        return _lib.FAIL, "governed set is empty — nothing is being checked (misconfiguration)"
    if problems:
        return _lib.FAIL, f"doc-freshness: {problems}"
    return _lib.PASS, f"{checked} governed doc(s) carry a fresh marker (<= {HORIZON_DAYS}d)"


if __name__ == "__main__":
    sys.exit(_lib.run_standalone(check))
