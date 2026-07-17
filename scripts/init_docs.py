#!/usr/bin/env python3
"""Scaffold the Ges-Talt docs convention into a repo. Idempotent.

    python3 scripts/init_docs.py [target-repo-root] [--sprint M-Y-DD-DD]

Creates:
    docs/backlog.md                     — the backlog table
    docs/sprint-<m>-<y>-<dd>-<dd>/      — current sprint (default: today,
        prd.md                            7-day window)
        sprint-log/
        user-journeys/
    docs/templates/                     — copied from this repo if absent

Existing files are never overwritten.
"""
import argparse
import shutil
import sys
from datetime import date, timedelta
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
BACKLOG = """# Backlog

Rows are added by the spec-driven PM (`agents/pm/project-manager`); one row
per issue. Status: todo / in-progress / blocked / done.

| ID | Item | Assignee (agent) | Sprint | Status | Issue |
|---|---|---|---|---|---|
"""


def main():
    p = argparse.ArgumentParser()
    p.add_argument("root", nargs="?", default=".", help="target repo root")
    p.add_argument("--sprint", help="sprint name suffix M-Y-DD-DD; default: today + 7 days")
    args = p.parse_args()

    root = Path(args.root).resolve()
    if not (root / ".git").exists():
        sys.exit(f"{root} is not a git repo root")

    if args.sprint:
        suffix = args.sprint
    else:
        start = date.today()
        end = start + timedelta(days=7)
        suffix = f"{start.month}-{start.year % 100}-{start.day}-{end.day}"

    docs = root / "docs"
    sprint = docs / f"sprint-{suffix}"
    made = []

    for d in (sprint / "sprint-log", sprint / "user-journeys"):
        if not d.exists():
            d.mkdir(parents=True)
            (d / ".gitkeep").touch()
            made.append(str(d.relative_to(root)))

    backlog = docs / "backlog.md"
    if not backlog.exists():
        backlog.write_text(BACKLOG)
        made.append("docs/backlog.md")

    src_templates = HERE / "docs" / "templates"
    dst_templates = docs / "templates"
    if not dst_templates.exists() and src_templates.exists():
        shutil.copytree(src_templates, dst_templates)
        made.append("docs/templates/")

    prd = sprint / "prd.md"
    if not prd.exists():
        tpl = dst_templates / "prd.md"
        prd.write_text(tpl.read_text() if tpl.exists() else "# PRD\n")
        made.append(str(prd.relative_to(root)))

    print("created: " + ", ".join(made) if made else "nothing to do — scaffold already present")


if __name__ == "__main__":
    main()
