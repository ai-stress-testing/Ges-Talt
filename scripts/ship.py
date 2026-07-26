#!/usr/bin/env python3
"""Push the current branch to origin, guarded (issue #71).

    python3 scripts/ship.py            # git push -u origin <current branch>
    python3 scripts/ship.py --main     # + fast-forward origin/main to HEAD
    python3 scripts/ship.py --dry-run  # print what would run; no git push

A push that fails for a NETWORK reason (DNS/connect/TLS/timeout) retries
with exponential backoff (2/4/8/16s — up to 4 retries after the first
attempt). A push that fails for any other reason — rejected,
non-fast-forward, auth — surfaces immediately and is never retried:
retrying those wastes four backoff cycles on something backoff can't fix
and can mask a real problem (someone else pushed, credentials expired).

`--main` additionally publishes HEAD to origin's `main` ref, but ONLY when
that is a real fast-forward: `git merge-base --is-ancestor origin/main
HEAD` must hold AND HEAD must differ from origin/main (a strict
descendant). If it doesn't hold, ship.py refuses with a clear message
instead of attempting anything. This script NEVER force-pushes, NEVER
uses --force-with-lease, and NEVER creates a commit — the only git
mutations it performs are `git push` (never with -f) and `git fetch`.

Prints exactly the refs + short SHAs it pushed, nothing more.
"""
import re
import subprocess
import sys
import time

BACKOFF = (2, 4, 8, 16)  # seconds, waited before retries 1..4 respectively

# Combined stdout+stderr substrings that indicate a transport-layer
# (network) failure, not a git-semantic rejection. Deliberately narrow: an
# unrecognized failure defaults to "reject" (surface immediately), which is
# the safe direction — we only retry when we're confident it's the network.
NETWORK_PATTERNS = [re.compile(p, re.I) for p in (
    r"could not resolve host",
    r"could not connect to server",
    r"connection timed out",
    r"connection refused",
    r"network is unreachable",
    r"no route to host",
    r"recv failure",
    r"send failure",
    r"ssl[ _-]?(handshake|connect|read|write)",
    r"tls handshake",
    r"gnutls_handshake",
    r"the remote end hung up unexpectedly",
    r"early eof",
    r"temporary failure in name resolution",
    r"operation timed out",
)]


def run_git(args, cwd=None):
    """Run `git <args>`; return (returncode, stdout, stderr). Never raises
    on a non-zero exit — callers classify it themselves."""
    proc = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    return proc.returncode, proc.stdout, proc.stderr


def classify_push_failure(output):
    """'network' if `output` matches a known transport-layer failure;
    'reject' otherwise (rejected / non-fast-forward / auth / anything
    unrecognized) — the default that must NOT be retried."""
    return "network" if any(p.search(output) for p in NETWORK_PATTERNS) else "reject"


def current_branch(runner=run_git, cwd=None):
    rc, out, err = runner(["rev-parse", "--abbrev-ref", "HEAD"], cwd)
    branch = out.strip()
    if rc != 0 or not branch or branch == "HEAD":
        raise RuntimeError(f"cannot determine current branch (detached HEAD?): {err.strip()}")
    return branch


def short_sha(ref, runner=run_git, cwd=None):
    rc, out, err = runner(["rev-parse", "--short", ref], cwd)
    if rc != 0:
        raise RuntimeError(f"cannot resolve {ref}: {err.strip()}")
    return out.strip()


def push_with_retry(refspec, remote="origin", extra_args=(), runner=run_git,
                     cwd=None, sleep=time.sleep, dry_run=False, log=print):
    """Push `refspec` to `remote` (never with -f/--force-with-lease).
    Retries with BACKOFF only while classify_push_failure says 'network'.
    Returns (ok: bool, combined_output: str)."""
    args = ["push", *extra_args, remote, refspec]
    if dry_run:
        return True, f"[dry-run] git {' '.join(args)}"

    attempt = 0
    while True:
        rc, out, err = runner(args, cwd)
        combined = out + err
        if rc == 0:
            return True, combined
        kind = classify_push_failure(combined)
        if kind != "network" or attempt >= len(BACKOFF):
            return False, combined
        delay = BACKOFF[attempt]
        log(f"ship.py: push failed (network, attempt {attempt + 1}/{len(BACKOFF)}); "
            f"retrying in {delay}s...", file=sys.stderr)
        sleep(delay)
        attempt += 1


def can_fast_forward_main(runner=run_git, cwd=None):
    """(status, detail). status in {"ff", "up-to-date", "diverged", "unknown"}.
    The real FF check: `git merge-base --is-ancestor origin/main HEAD` must
    hold AND HEAD must differ from origin/main (a *strict* descendant)."""
    rc_head, head_sha, _ = runner(["rev-parse", "HEAD"], cwd)
    rc_main, main_sha, _ = runner(["rev-parse", "origin/main"], cwd)
    if rc_head != 0 or rc_main != 0:
        return "unknown", "cannot resolve HEAD or origin/main — fetch first?"
    head_sha, main_sha = head_sha.strip(), main_sha.strip()
    if head_sha == main_sha:
        return "up-to-date", f"origin/main is already at {head_sha[:7]}"
    rc, _, _ = runner(["merge-base", "--is-ancestor", "origin/main", "HEAD"], cwd)
    if rc == 0:
        return "ff", f"HEAD is a strict descendant of origin/main ({main_sha[:7]} -> {head_sha[:7]})"
    return "diverged", (
        f"origin/main ({main_sha[:7]}) is not an ancestor of HEAD ({head_sha[:7]}) — "
        "this would not be a fast-forward; refusing (ship.py never force-pushes main)"
    )


def main(argv):
    do_main = "--main" in argv
    dry_run = "--dry-run" in argv
    pushed = []  # refs actually pushed so far — reported regardless of how
                 # the run ends, since a real push must never go unreported.

    def report(code):
        for ref in pushed:
            print(f"pushed {ref}")
        return code

    try:
        branch = current_branch()
    except RuntimeError as e:
        print(f"ship.py: {e}", file=sys.stderr)
        return report(1)

    ok, out = push_with_retry(branch, extra_args=["-u"], dry_run=dry_run)
    if not ok:
        print(f"ship.py: push of {branch} failed, not retrying further:\n{out.rstrip()}",
              file=sys.stderr)
        return report(1)
    sha = short_sha("HEAD") if not dry_run else "(dry-run)"
    pushed.append(f"origin/{branch}@{sha}")

    if do_main:
        if not dry_run:
            rc, fout, ferr = run_git(["fetch", "origin", "main"])
            if rc != 0:
                print(f"ship.py: git fetch origin main failed:\n{(fout + ferr).rstrip()}",
                      file=sys.stderr)
                return report(1)
            status, detail = can_fast_forward_main()
        else:
            status, detail = "ff", "[dry-run] skipped fetch/ancestry check"

        if status == "up-to-date":
            print(f"ship.py --main: {detail}; nothing to fast-forward")
        elif status == "ff":
            ok, out = push_with_retry("HEAD:main", dry_run=dry_run)
            if not ok:
                print(f"ship.py: fast-forward push to main failed, not retrying further:"
                      f"\n{out.rstrip()}", file=sys.stderr)
                return report(1)
            main_sha = short_sha("origin/main") if not dry_run else "(dry-run)"
            pushed.append(f"origin/main@{main_sha}")
        else:
            print(f"ship.py --main: refusing — {detail}", file=sys.stderr)
            return report(1)

    return report(0)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
