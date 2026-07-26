"""Assert downstream traceability: a requirement/AC terminates in a test (#80).

The forward half of traceability is already enforced (an issue with no PRD
`§n` source isn't created — issue-spec template + WORKFLOW). This verifier
closes the DOWNSTREAM half (docs/traceability.md): a requirement or acceptance
criterion that has no verification link is unverifiable and fails the gate.

Two live checks, both fail-closed, over the CURRENT sprint only (so the
discipline binds going forward without failing pre-#80 history):

1. **Issue-spec files** — any file with a `## Sub-issues` section: every
   `### <n>. <title>` sub-issue block must carry a `**Verify**:` line (a
   command, a `testing/` role, or a `scripts/verifiers/` name). A sub-issue
   with acceptance criteria but no Verify line is the counterexample.
2. **Filled PRDs** — a `prd.md` whose Requirements section is real (not the
   `<placeholder>` template stub) must have at least one checkable `- [ ]`
   success criterion (the downstream "how the sprint is judged done" link).

SKIP when the current sprint has neither an issue-spec file nor a filled PRD
to gate — nothing downstream to trace yet. Distinct from `verdict_recorded`
(presence of a verdict) and `index_in_sync` (roster freshness): this is the
requirement→test coverage property.
"""
import datetime
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _lib  # noqa: E402

PROPERTY = "Every sub-issue in a current-sprint issue-spec has a Verify link; a filled PRD has a checkable success criterion."
METHOD = "static"
OWNER = "pm/project-manager"

SPRINT_RE = re.compile(r"sprint-(\d{1,2})-(\d{2})-(\d{1,2})-(\d{1,2})$")
SUBISSUE_RE = re.compile(r"^###\s+\d+\.\s+.+$", re.M)
VERIFY_RE = re.compile(r"^\s*[-*]?\s*\*\*Verify\*\*:", re.M)
# The unfilled template ships angle-bracket placeholders; a real PRD won't.
PLACEHOLDER_RE = re.compile(r"<requirement —|<title>|<sprint>")
CHECKBOX_RE = re.compile(r"^\s*[-*]\s*\[[ xX]\]\s*\S", re.M)


def current_sprint_dir(today):
    for d in glob.glob("docs/sprint-*/"):
        m = SPRINT_RE.search(d.rstrip("/"))
        if not m:
            continue
        month, yy, d1, d2 = (int(x) for x in m.groups())
        try:
            start = datetime.date(2000 + yy, month, d1)
            end = datetime.date(2000 + yy, month, d2)
        except ValueError:
            continue
        if start <= today <= end:
            return d.rstrip("/")
    return None


def split_subissues(text):
    """Yield each sub-issue block: from a `### n. title` heading to the next."""
    idxs = [m.start() for m in SUBISSUE_RE.finditer(text)]
    for i, start in enumerate(idxs):
        end = idxs[i + 1] if i + 1 < len(idxs) else len(text)
        yield text[start:end]


def check():
    _lib.in_repo_root()
    sprint = current_sprint_dir(datetime.date.today())
    if sprint is None:
        return _lib.SKIP, "no sprint window covers today (sprint_window_current owns that)"

    gated = 0
    problems = []

    # (1) issue-spec files — anything carrying a Sub-issues section.
    for path in sorted(glob.glob(f"{sprint}/**/*.md", recursive=True)):
        if "/sprint-log/" in path or path.endswith("prd.md"):
            continue
        text = open(path, encoding="utf-8").read()
        if "## Sub-issues" not in text:
            continue
        for block in split_subissues(text):
            gated += 1
            if not VERIFY_RE.search(block):
                head = block.splitlines()[0].strip()
                problems.append(f"{os.path.basename(path)} :: {head} — no **Verify** link")

    # (2) filled PRD — real requirements must have a checkable success criterion.
    for path in sorted(glob.glob(f"{sprint}/prd.md")):
        text = open(path, encoding="utf-8").read()
        if PLACEHOLDER_RE.search(text):
            continue  # still the template stub — nothing to trace yet
        gated += 1
        after = text.split("Success criteria", 1)
        if len(after) < 2 or not CHECKBOX_RE.search(after[1]):
            problems.append(f"{os.path.basename(path)} — filled PRD with no checkable success criterion")

    if gated == 0:
        return _lib.SKIP, f"no issue-spec or filled PRD in {sprint} to trace yet"
    if problems:
        return (_lib.FAIL,
                f"downstream trace missing: {problems} — every requirement/AC "
                "needs a test/metric link (docs/traceability.md)")
    return _lib.PASS, f"{gated} requirement/AC block(s) in {sprint} carry a downstream link"


if __name__ == "__main__":
    sys.exit(_lib.run_standalone(check))
