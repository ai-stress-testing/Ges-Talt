run-id: 2026-07-18-backlog-wave
prompt: "Take on some of the backlog, spinning subagents, proper model per task."
agents:
  - logicians/software-architect (opus, 44,749 tok)   # GT-39 depth-pack joint optimum
  - devops/devops-automator (sonnet, 70,042 tok)      # GT-32 acting feedback controller
  - devops/devops-automator (sonnet, 82,145 tok)      # GT-33 tiers + GT-13 widening lint
  - pm/team-operations (sonnet, 55,318 tok)           # GT-37 ephemeral gov + GT-38 run manifest
specs: backlog GT-13/32/33/37/38/39
verdicts: PASS (all four; self-tests green — build_index/verify_comms/credit all exit 0)
commits: this commit

# 2026-07-18 — backlog wave (four subagents, model matched to task)

**Session/agent**: orchestrator + four subagents (1 opus, 3 sonnet),
disjoint file ownership; observer wrote ledger credit.

## Done
- GT-39 (opus, marquee): L0 charter + on-demand L1 DEPTH.md; docs/
  depth-packs.md, TEMPLATE/DEPTH.md, example packs for falsifier +
  backend-dev. Depth without per-call token cost.
- GT-32: scripts/credit.py — per-role selection score from the ledger
  (the mechanism that makes the feedback loop ACT). docs/credit.md,
  docs/selection-weights.json.
- GT-33: capability tiers (scripts/models.toml, reason/build/cheap) +
  build_index resolves them; ai-engineer demoed on `build`. docs/
  model-tiers.md. GT-13: tool-widening lint vs scripts/tools-baseline.json.
- GT-37: ephemeral-agent governance (declare/check/log) in ORCHESTRATION.
  GT-38: run manifest (this header is the first one).

## Decisions
- Ledger reconciled for integrity: 3 stale platform/* roles remapped to
  current homes; 4 synthetic demo rows dropped (real ledger = real
  observed runs only); this wave's 4 runs appended with verified tokens
  (observer writes credit, per COMMS.md).
- All four verdicts PASS, so credit ranking is cost-driven (no fabricated
  FAIL data) — honest signal, not invented variance.

## Blocked / carried
- GT-34/35/36 (grader independence, anti-gaming, mesh) ride on the tier
  mapping now landed — unblocked, queued.
- GT-6 (environments), GT-7 (critical-systems), GT-23 (routines) still
  need owner direction.
