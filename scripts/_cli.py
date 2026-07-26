"""Shared plumbing for the scripts/*.py operator tools (issue #67 epic).

Deliberately tiny and stdlib-only, mirroring `scripts/verifiers/_lib.py`'s
shape but for the top-level CLI scripts rather than the verifier registry.
These are SEPARATE tools (gate.py / ship.py / new_sprint_log.py /
backlog.py) by explicit owner choice, not a unified dispatcher — this
module exists only to avoid re-deriving the two bits of plumbing every one
of them needs: where the repo root is, and which sprint folder covers
today.

Sprint-window detection reuses the regex from
`scripts/verifiers/sprint_window_current.py` (loaded, not copied) rather
than re-deriving the `sprint-<m>-<yy>-<dd>-<dd>` parsing a second time —
the folder-name grammar is the one thing here worth not getting slightly
wrong twice.
"""
import datetime
import glob
import importlib.util
import os

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))


def repo_root():
    """Absolute path to the repo root. This file is scripts/_cli.py, so the
    root is one directory up."""
    return os.path.dirname(SCRIPTS_DIR)


def in_repo_root():
    """chdir to the repo root so relative paths (docs/…, agents/…) resolve
    the same no matter where the script was invoked from."""
    os.chdir(repo_root())


def _load_verifier(name):
    """Load scripts/verifiers/<name>.py by path, the same mechanism
    scripts/verify.py already uses — no package __init__ required."""
    path = os.path.join(SCRIPTS_DIR, "verifiers", f"{name}.py")
    spec = importlib.util.spec_from_file_location(f"verifiers.{name}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def current_sprint_dir(today=None):
    """The repo-root-relative `docs/sprint-<m>-<yy>-<dd>-<dd>` folder whose
    window covers `today` (default: real today), or None if none does.

    Uses sprint_window_current.SPRINT_RE (imported) to parse folder names,
    then picks the one window that covers the date — the same check that
    verifier performs, exposed here as a reusable value instead of a
    PASS/FAIL message.
    """
    today = today or datetime.date.today()
    swc = _load_verifier("sprint_window_current")
    root = repo_root()
    for d in sorted(glob.glob(os.path.join(root, "docs", "sprint-*/"))):
        name = os.path.basename(d.rstrip("/"))
        m = swc.SPRINT_RE.search(name)
        if not m:
            continue
        month, yy, d1, d2 = (int(x) for x in m.groups())
        try:
            start = datetime.date(2000 + yy, month, d1)
            end = datetime.date(2000 + yy, month, d2)
        except ValueError:
            continue
        if start <= today <= end:
            return f"docs/{name}"
    return None
