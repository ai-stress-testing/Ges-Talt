# 2026-07-20 — Hard-verifier registry (GT-43) + branching convention + token-economy repo index

**Session/agent**: main session (orchestrator, direct).
**Issues touched**: GT-43, GT-50, GT-51 (backlog). No GitHub issue cut.

```
run-id: 2026-07-20-verifier-registry
prompt: "Move forward with GT-43. Add feature/bug/fix/mvp/plan branching + worktree observability. Add a repo index to save tokens."
agents: main session only (framework + convention authoring, direct; no measured subagent token cost to ledger)
specs: docs/branching.md, agents/WORKFLOW.md §5, docs/opsec/hard-verifiers.md "Built (GT-43)"
verdicts: scripts/verify.py 9/9 PASS (exit 0); build_index / verify_comms / credit / audit_skills all exit 0
commits: (see push)
```

## Done
- **GT-43 — hard-verifier registry.** Built `scripts/verify.py` (the
  runner) + `scripts/verifiers/` (single-property machines). Each verifier
  exposes `PROPERTY`/`METHOD`/`OWNER`/`check() -> (status, detail)`; the
  runner composes them, prints failures first, and exits non-zero on any
  FAIL. Fail-closed: a verifier that raises is a FAIL, not a skip. Seeded 9
  machines that secure the agent org itself: roster pairing, reason-tier
  read-only boundary, handoff-ref resolution, INDEX freshness, ledger
  well-formedness, tools-baseline containment, current sprint window, branch
  taxonomy, repo-map freshness. Wired into the verdict loop as
  `WORKFLOW.md §5` and updated `hard-verifiers.md` from "next step if
  pursued" to "built".
- **GT-50 — branching + worktree convention.** `docs/branching.md`: typed
  work branches `feature|fix|bug|mvp|plan/<slug>` + reserved trunks
  (`main`, `Sprint0`, `claude/*`), enforced by the `branch_taxonomy`
  verifier; worktree-per-task documented as the observability fix (one
  tree = one blast radius; `git worktree list` = live map of in-flight
  work). Owned by `cd/gitops-engineer` + `ci/pipeline-engineer`.
- **GT-51 — token-economy repo index.** `scripts/build_repo_index.py` →
  `docs/repo-map.md`: a deterministic path→purpose navigation map (layout,
  teams, scripts, environments, docs) so an agent reads one terse file
  instead of grepping the tree. Kept fresh by the `repo_map_fresh` verifier;
  points at `agents/INDEX.md` for agent detail rather than duplicating it.
- Session-start checklist (`CLAUDE.md`) now runs `verify.py` and points at
  `repo-map.md` before grepping.
- **The index earned its keep on the first run**: `repo-map.md` surfaced
  `backend/` as the lone team with no `README.md` (14/15 had one). Wrote the
  missing charter and added a 10th verifier, `team_readmes`, so the gap can't
  reopen. Gate is 10/10 PASS.

## Decisions
- **verify.py reuses build_index's primitives** (frontmatter parse, model
  resolution, handoff check, tools baseline) instead of re-implementing them
  — a verifier that copied that logic could drift from the thing it verifies.
- **Verifiers gate the org as target** (`hard-verifiers.md`: "secure the
  machine that secures the machines"). The security/domain verifiers already
  brainstormed (egress allowlist, BOLA/IDOR, banned crypto, …) are the same
  shape — a target repo drops them into the same `scripts/verifiers/` dir and
  the runner picks them up. The seed set is the meta-repo's own invariants.
- **SKIP ≠ FAIL.** A property that's N/A in context (not a git repo, no
  ledger yet) skips without failing the gate; only a real FAIL blocks.
- **Caught during build**: `_lib.repo_root()` was off by one directory
  (resolved to `scripts/`, not the repo root), which made `roster_pairing`
  and `handoff_refs_resolve` pass on *empty* globs — a false green. Fixed the
  anchor (three dirnames up from `scripts/verifiers/_lib.py`) and added an
  explicit "empty roster ⇒ FAIL" guard so a wrong cwd can never read as PASS.
- **No ledger rows appended** — orchestrator-direct work, no measured
  subagent token cost; fabricating one would corrupt the ledger.

## Blocked / carried
- Owner-gated: arm the session reaper; GT-20 blueprinting; GT-23 routines.
- The `reason`-method verifiers (business-logic invariants via
  `logicians/falsifier`, AI-surface via `ai/model-evaluator`) are speced in
  `hard-verifiers.md` but not yet built — they need a running target, so they
  land when a target repo adopts the registry.
