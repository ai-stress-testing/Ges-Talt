# Session lifecycle — proactive reaping

THREAT-MODEL C5, and the original Sprint0 ask ("proactive session
deletions"). Stale sessions are idle attack surface and cost — this reaps
them. **Status: designed, NOT armed.** Reaping deletes things, so the live
routine ships only on the owner's go-ahead; this spec is exact enough to arm
in one step.

Owner: `networking/network-engineer`. Arming/disarming is the owner's call.

## What counts as reapable

A session is a candidate only if ALL hold:
- Idle > **24h** (no activity), and
- No uncommitted or unpushed work in its worktree, and
- No open GitHub issue assigned to it / no in-progress task, and
- Not on the protected-session allowlist (owner-maintained).

Any one failing = keep. The bar is deliberately conservative: a false reap
destroys work, a false keep costs a little idle resource. Asymmetric, so
default to keep.

## How it would run (the routine, once armed)

1. **Dry-run first, always.** The sweep lists candidates and their evidence
   (idle time, clean-tree check, no-open-work check) — it does not delete.
2. **Grace period.** A candidate must survive a full grace window (e.g. a
   second daily sweep still finding it reapable) before deletion — no
   same-pass delete.
3. **Reap.** Only then delete, logging each reap (session id, evidence,
   timestamp) to an audit trail.
4. Cadence: daily. Mechanism: a scheduled routine (`create_trigger`) firing
   the sweep.

## Safety rails (why it's unarmed)

- Deletion is irreversible and outward-affecting — arming a cron that
  deletes sessions is exactly the class of action that needs explicit
  confirmation, not self-direction.
- The rails above (dry-run, grace, clean-tree gate, allowlist) exist so that
  when armed it *cannot* reap live work — but they're asserted here, not yet
  proven against a real session list.

## To arm

Owner confirms the criteria and grace window, then the reaping routine is
created (starting in dry-run/report-only mode for at least one cycle to
verify the candidate set is correct before any deletion is enabled). Until
then this is policy, not a live deleter.
