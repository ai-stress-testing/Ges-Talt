run-id: 2026-07-19-model-update-and-polish
prompt: "Is docs/opsec the best place? What would Nous do? polish + update scripts for the new model. Clean up for prod, push to main."
agents:
  - main/orchestrator (opus)
specs: model-sovereignty update + Nous-lens polish + prod cleanup
verdicts: PASS (build_index/verify_comms/credit all green; resolution self-test passed)
commits: this commit

# 2026-07-19 — model-generation update + Nous polish + prod cleanup

## Done
- Scripts updated for the new model generation: scripts/models.toml now
  maps tiers AND readable aliases to real current ids (reason→claude-opus-4-8,
  build→claude-sonnet-5, cheap→claude-haiku-4-5-20251001, +fable alias).
  build_index.py resolves tier/alias/concrete-id → canonical id; the
  read-only boundary keys on the reason-tier id (not the literal "opus"),
  so it survives a generation bump. Roster frontmatter (opus/sonnet/haiku
  aliases) unchanged — a model swap is now one file, per the Nous review's
  #1 finding (model sovereignty), demonstrated for real.
- Nous-lens honesty fix: the COMMS.md attribution example was a wrapped
  multi-line quote that verify_comms silently SKIPS, yet claimed "hence the
  check". Replaced with a single-line example that genuinely validates
  against a real ledger row (devops/devops-automator @ 70,042) — the repo's
  own honesty example is now actually verified.
- docs/model-tiers.md rewritten to the real ids + alias layer + the
  "update = one line" note.
- Prod cleanup: no tracked junk, no stale live handoffs (platform/ hits are
  provenance/history only), all lints green, tools-baseline + INDEX current.

## Decisions
- docs/opsec/ kept as the home: issue #21 defined OPSEC as the gate every
  output passes through; the checklists are its playbook. hard-verifiers.md
  stays there for now and will anchor scripts/verifiers/ when GT-43 lands
  (renaming the dir would churn ~15 refs against the user's own #21 naming).
- Aliases retained so a model bump doesn't rewrite 80+ agent.md files — the
  readable label lives in frontmatter, the real id in models.toml.

## Blocked / carried
- GT-43 (hard-verifier registry), session-reaper arming — still owner-gated.
