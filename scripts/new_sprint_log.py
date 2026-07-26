#!/usr/bin/env python3
"""Stamp a new sprint-log entry from the template (issue #70).

    python3 scripts/new_sprint_log.py <slug> [--prompt "..."]

Creates `docs/sprint-<current>/sprint-log/<YYYY-MM-DD>-<slug>.md` from
`docs/templates/sprint-log-entry.md`, with the run-manifest header
(WORKFLOW.md §4) prefilled: `run-id: <YYYY-MM-DD>-<slug>`, the `prompt:`
line if given, and the current sprint folder auto-detected via
`scripts/_cli.py` (which reuses the sprint-window regex from
`scripts/verifiers/sprint_window_current.py` rather than re-deriving it).

`verdicts:` and `commits:` are left as visible `TODO` placeholders — this
script scaffolds, it never fakes a verdict. The `verdict_recorded` hard
verifier (`scripts/verifiers/verdict_recorded.py`) requires a real,
non-empty value there before a run-manifest counts as recording one; a
bare `TODO` is non-empty (so it won't silently rot unnoticed as "empty")
but is obviously not a real verdict, so the author has to come back and
fill it in rather than ship on a placeholder.

Refuses to overwrite an existing entry. Refuses to create one when no
sprint window covers today, pointing at `scripts/init_docs.py` instead of
guessing which folder to use.
"""
import argparse
import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _cli  # noqa: E402

TEMPLATE = "docs/templates/sprint-log-entry.md"


def render(slug, prompt, today):
    """The full entry text: template body with the H1/Session/Issues
    placeholders marked TODO, and the run-manifest header block inserted
    between the manifest lines and `## Done` — matching every existing
    sprint-log entry's layout (see docs/sprint-*/sprint-log/*.md)."""
    template_path = os.path.join(_cli.repo_root(), TEMPLATE)
    text = open(template_path, encoding="utf-8").read()

    header_lines = [f"run-id: {today:%Y-%m-%d}-{slug}"]
    if prompt:
        header_lines.append(f'prompt: "{prompt}"')
    header_lines += ["agents: TODO", "specs: TODO", "verdicts: TODO", "commits: TODO"]
    header = "```\n" + "\n".join(header_lines) + "\n```"

    lines = text.splitlines()
    out = []
    for line in lines:
        if line.startswith("# <yyyy-mm-dd>"):
            out.append(f"# {today:%Y-%m-%d} — TODO one-line summary")
        elif line.startswith("**Session/agent**:"):
            out.append("**Session/agent**: TODO — who did the work.")
        elif line.startswith("**Issues touched**:"):
            out.append("**Issues touched**: TODO — #n, #n.")
            out.append("")
            out.append(header)
        else:
            out.append(line)
    return "\n".join(out).rstrip("\n") + "\n"


def valid_slug(slug):
    return bool(slug) and all(c.isalnum() or c == "-" for c in slug) and slug.strip("-")


def main(argv):
    parser = argparse.ArgumentParser(
        prog="new_sprint_log.py",
        description="Stamp a new dated sprint-log entry from the template.",
    )
    parser.add_argument("slug", help="short kebab-case slug, e.g. 'ship-script'")
    parser.add_argument("--prompt", default=None,
                         help="the driving prompt/instruction, recorded verbatim")
    args = parser.parse_args(argv)

    if not valid_slug(args.slug):
        print(f"new_sprint_log.py: '{args.slug}' is not a valid slug — use "
              "lowercase letters, digits, and hyphens only", file=sys.stderr)
        return 1

    root = _cli.repo_root()
    today = datetime.date.today()
    sprint_dir = _cli.current_sprint_dir(today)
    if sprint_dir is None:
        print(
            f"new_sprint_log.py: no docs/sprint-<m>-<yy>-<dd>-<dd> folder covers "
            f"today ({today}) — scaffold the next sprint first: "
            "`python3 scripts/init_docs.py .`", file=sys.stderr,
        )
        return 1

    out_dir = os.path.join(root, sprint_dir, "sprint-log")
    out_name = f"{today:%Y-%m-%d}-{args.slug}.md"
    out_path = os.path.join(out_dir, out_name)
    if os.path.exists(out_path):
        print(f"new_sprint_log.py: refusing to overwrite existing entry "
              f"{sprint_dir}/sprint-log/{out_name}", file=sys.stderr)
        return 1

    content = render(args.slug, args.prompt, today)
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"wrote {sprint_dir}/sprint-log/{out_name}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
