#!/usr/bin/env python3
"""One command runs the whole regenerate+verify pipeline, in order (#68).

The mechanical ceremony this repo's own session manual asks for by hand
every time (CLAUDE.md "On session start" steps 3-4, plus verify_comms /
credit / audit_skills) — a repeated manual sequence is a bug, so it's a
script instead.

Orchestrates the EXISTING scripts as subprocesses; it never reimplements
their logic:

    regenerate (skipped in --check): build_index.py, build_personas.py,
                                      build_repo_index.py
    verify (always):                 verify_comms.py, credit.py,
                                      audit_skills.py, verify.py

`build_index.py` runs first and alone: it is both a regenerate step and
the roster lint gate everything downstream depends on (build_personas.py
reads the same frontmatter it lints; a broken roster makes every
regenerated artifact suspect). If it exits non-zero, the gate aborts
immediately without running anything else. Otherwise every remaining step
runs regardless of earlier failures — this runner aggregates, prints
FAILURES FIRST, then a one-line summary, and exits non-zero iff anything
failed. A step's exit code is never swallowed.

Usage:
    python3 scripts/gate.py            # regenerate + verify (full pipeline)
    python3 scripts/gate.py --check    # verify-only (CI: artifacts must
                                        # already be committed fresh)
"""
import subprocess
import sys
from pathlib import Path

SCRIPTS_DIR = Path(__file__).resolve().parent
ROOT = SCRIPTS_DIR.parent

REGEN = ["build_index.py", "build_personas.py", "build_repo_index.py"]
VERIFY = ["verify_comms.py", "credit.py", "audit_skills.py", "verify.py"]


def run_step(name, runner=subprocess.run):
    """Run scripts/<name> from the repo root; return (name, returncode,
    combined stdout+stderr). Never raises on a non-zero exit — the caller
    decides what to do with it."""
    proc = runner(
        [sys.executable, str(SCRIPTS_DIR / name)],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )
    return name, proc.returncode, proc.stdout + proc.stderr


def run_gate(check_only, runner=subprocess.run):
    """Execute the pipeline and return (exit_code, report_str). Pure enough
    to unit-test: the only side effects are the subprocess calls inside
    run_step, which the caller can stub via `runner`."""
    results = []
    lines = []

    if not check_only:
        name, rc, out = run_step(REGEN[0], runner)  # build_index.py
        results.append((name, rc, out))
        if rc != 0:
            lines.append(
                f"FAIL {name} (exit {rc}) — roster lint failed; aborting "
                f"the rest of the gate (a red roster makes every "
                f"downstream artifact suspect):\n{out.rstrip()}"
            )
            lines.append(f"\ngate (full): 0/1 passed — {name}=FAIL({rc}), rest not run")
            return 1, "\n".join(lines)
        remaining = REGEN[1:] + VERIFY
        mode = "full"
    else:
        remaining = VERIFY
        mode = "check"

    for name in remaining:
        results.append(run_step(name, runner))

    failures = [(n, rc, out) for n, rc, out in results if rc != 0]

    if failures:
        lines.append(f"{len(failures)} FAILURE(S):\n")
        for name, rc, out in failures:
            lines.append(f"--- {name} (exit {rc}) ---")
            lines.append(out.rstrip() or "(no output)")
            lines.append("")

    n_pass = len(results) - len(failures)
    summary = ", ".join(
        f"{n}={'PASS' if rc == 0 else f'FAIL({rc})'}" for n, rc, _ in results
    )
    lines.append(f"gate ({mode}): {n_pass}/{len(results)} passed — {summary}")

    return (1 if failures else 0), "\n".join(lines)


def main(argv):
    check_only = "--check" in argv
    code, report = run_gate(check_only)
    print(report)
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
