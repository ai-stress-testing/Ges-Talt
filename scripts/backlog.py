#!/usr/bin/env python3
"""Add or flip a row in docs/backlog.md, byte-precise (issue #72).

    python3 scripts/backlog.py add "<item>" "<assignee>" [--issue N]
    python3 scripts/backlog.py done GT-<n> [--status <state>]

`add` appends a well-formed row with the next `GT-<n>` id (max existing +
1), the current sprint (auto-detected the same way scripts/_cli.py detects
it elsewhere), status `todo`, and the issue link if `--issue` is given.

`done GT-<n>` flips ONLY that row's Status cell in place — every other
row, and every other cell of that row, is left byte-identical. `--status
<state>` sets any status value, not just `done` (the subcommand name is
the common case, not the only one).

Malformed input (missing assignee, unknown GT-<n>, a `|` in free text that
would corrupt the table) errors clearly on stderr and changes nothing —
this script never partially writes the file.

docs/backlog.md is a summary view; GitHub issues remain canonical
(CLAUDE.md "Docs convention"). This script only ever touches that one
table, in that one file, and preserves its exact column/pipe format.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _cli  # noqa: E402

BACKLOG = "docs/backlog.md"
ISSUE_URL = "https://github.com/ai-stress-testing/Ges-Talt/issues/{n}"
ROW_RE = re.compile(r"^\|\s*GT-(\d+)\s*\|")


def load(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def save(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def existing_ids(text):
    """[(n, line)] for every `| GT-<n> | ...` row, in file order."""
    return [(int(m.group(1)), line) for line in text.splitlines()
            if (m := ROW_RE.match(line))]


def build_row(gt_id, item, assignee, sprint, status, issue):
    for field, name in ((item, "item"), (assignee, "assignee"), (sprint, "sprint")):
        if "|" in field:
            raise ValueError(f"{name} must not contain '|' (would corrupt the table): {field!r}")
    issue_cell = ISSUE_URL.format(n=issue)
    issue_cell = f"[#{issue}]({issue_cell})" if issue else "—"
    return f"| GT-{gt_id} | {item} | {assignee} | {sprint} | {status} | {issue_cell} |"


def add_row(text, item, assignee, sprint, issue=None, status="todo"):
    """Return new_text with one appended row. Raises ValueError on
    malformed input; never mutates its argument."""
    if not item or not item.strip():
        raise ValueError("item must be non-empty")
    if not assignee or not assignee.strip():
        raise ValueError("assignee must be non-empty")
    ids = existing_ids(text)
    next_id = (max((n for n, _ in ids), default=0)) + 1
    row = build_row(next_id, item.strip(), assignee.strip(), sprint, status, issue)
    sep = "" if text.endswith("\n") else "\n"
    return f"{text}{sep}{row}\n", next_id


def flip_status(text, gt_id, new_status):
    """Return new_text with GT-<gt_id>'s Status cell set to new_status.
    Raises KeyError if gt_id doesn't exist. Every other row, and every
    other cell of the matched row, is byte-identical to the input."""
    n = int(gt_id.split("-", 1)[1]) if gt_id.upper().startswith("GT-") else None
    if n is None:
        raise ValueError(f"'{gt_id}' is not a GT-<n> id")

    lines = text.split("\n")
    target = f"GT-{n}"
    found = False
    out = []
    for line in lines:
        m = ROW_RE.match(line)
        if m and int(m.group(1)) == n:
            found = True
            cells = line.split("|")
            if len(cells) != 8:  # '', ID, Item, Assignee, Sprint, Status, Issue, ''
                raise ValueError(f"row for {target} is not a 6-column table row: {line!r}")
            cells[5] = f" {new_status} "
            out.append("|".join(cells))
        else:
            out.append(line)
    if not found:
        raise KeyError(target)
    return "\n".join(out)


def cmd_add(args):
    text = load(BACKLOG)
    sprint = _cli.current_sprint_dir()
    sprint_name = os.path.basename(sprint) if sprint else None
    if sprint_name is None:
        print("backlog.py: no sprint window covers today — scaffold the next "
              "sprint first: `python3 scripts/init_docs.py .`", file=sys.stderr)
        return 1
    try:
        new_text, gt_id = add_row(text, args.item, args.assignee, sprint_name,
                                   issue=args.issue)
    except ValueError as e:
        print(f"backlog.py add: {e}", file=sys.stderr)
        return 1
    save(BACKLOG, new_text)
    print(f"added GT-{gt_id} to {BACKLOG} (sprint {sprint_name})")
    return 0


def cmd_done(args):
    text = load(BACKLOG)
    try:
        new_text = flip_status(text, args.gt_id, args.status)
    except KeyError as e:
        print(f"backlog.py done: unknown id {e} in {BACKLOG}", file=sys.stderr)
        return 1
    except ValueError as e:
        print(f"backlog.py done: {e}", file=sys.stderr)
        return 1
    save(BACKLOG, new_text)
    print(f"{args.gt_id} -> status: {args.status}")
    return 0


def main(argv):
    parser = argparse.ArgumentParser(prog="backlog.py", description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    p_add = sub.add_parser("add", help="append a new row with the next GT-<n> id")
    p_add.add_argument("item", help="the backlog item description")
    p_add.add_argument("assignee", help="the owning agent, e.g. 'ci/pipeline-engineer'")
    p_add.add_argument("--issue", type=int, default=None, help="GitHub issue number to link")
    p_add.set_defaults(func=cmd_add)

    p_done = sub.add_parser("done", help="flip one row's status in place")
    p_done.add_argument("gt_id", metavar="GT-<n>", help="the row id, e.g. GT-42")
    p_done.add_argument("--status", default="done", help="status value (default: done)")
    p_done.set_defaults(func=cmd_done)

    args = parser.parse_args(argv)
    _cli.in_repo_root()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
