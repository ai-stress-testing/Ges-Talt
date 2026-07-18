# 2026-07-18 — comms convention, GitOps agent, routines parked, devops reframe

**Session/agent**: main session (opus).
**Issues touched**: #13 (GitOps) addressed; backlog GT-21..GT-24.

## Done
- agents/COMMS.md: quoted-attribution convention — every relay/handoff
  closes with "quote" — `team/role` (model), N tokens ✓, where ✓ means
  verified against docs/agent-ledger.jsonl by scripts/verify_comms.py.
  Observer writes the number, never the observed agent (threat-model
  separation of duties).
- scripts/verify_comms.py + docs/agent-ledger.jsonl (seeded with real
  verified figures from this session's subagent runs). Self-check +
  full scan both green; the COMMS.md example line verifies against the
  ledger, proving code-verification end to end.
- devops/gitops-engineer (#13): git-as-source-of-truth, drift detection,
  PR-as-deploy, rollback-by-revert.
- devops/README.md reframed toward "catch failure before it ships" per
  owner's definition; names the shared shift-left ownership and the
  unowned release-gate gap.
- docs/routines-ideas.md: brainstorm parking lot with 7 candidate
  routines (GT-23), per owner's request to queue not build.

## Decisions
- Token figures are code-verified, not hand-typed; an unverified figure
  carries no ✓.
- Ledger seeded only with figures actually reported this session — no
  fabricated numbers (would defeat the verifier's purpose).

## Blocked / carried
- GT-23 routines await owner brainstorm.
- GT-24 shift-left release-gate owner: carving undecided, asked the owner.
