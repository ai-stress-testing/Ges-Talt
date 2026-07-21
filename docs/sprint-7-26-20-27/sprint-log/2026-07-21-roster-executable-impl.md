# 2026-07-21 — Implement #59–#66: make the roster executable

**Session/agent**: main session (orchestrator, direct — tightly-coupled infra;
personas weren't installable yet, so delegation wasn't possible; the
review/adversarial gate was run inline and recorded, per the new discipline).
**Issues touched**: #59 (epic) + #60–#66; GT-59..GT-66.

```
run-id: 2026-07-21-roster-executable-impl
prompt: "Tackle these issues" (#59–#66: install personas as subagents + gate on the verdict loop).
agents: main session only (no measured subagent token cost to ledger); personas not yet runtime-installed this session, so inline per the WORKFLOW §1 caveat.
specs: docs/agent-triggering.md; CLAUDE.md "Routing"; WORKFLOW.md §1 implementer-agnostic gate; ORCHESTRATION.md exception; 3 new verifiers
verdicts: verify.py 14/14 PASS; build_index/verify_comms/credit/audit_skills PASS. Falsifier pass caught + fixed 2 real bugs (see Decisions).
commits: (see push)
```

## Done
- **#60** `scripts/build_personas.py` → `.claude/agents/` (105 personas, valid
  Claude Code subagent frontmatter: `name`=`<team>-<role>` slug, description,
  least-privilege `tools` passed through, `model` resolved to opus/sonnet/haiku).
  Idempotent; stale files pruned. `personas_installed` verifier asserts a fresh
  1:1 mirror. Wired into CLAUDE.md session-start.
- **#61** `docs/agent-triggering.md` convention + `description_triggers`
  verifier. Only 7/105 descriptions lacked a trigger; 4 already had one my first
  regex missed ("Use before/as" — widened the stem set), 3 genuinely lacked one
  (`ai/model-evaluator`, `cd/lifecycle-manager`, `pm/project-manager`) and were
  given a `Use when…/PROACTIVELY` clause.
- **#62** `CLAUDE.md` "Routing" section — a directive block that overrides the
  don't-spawn default: route non-trivial work through the roster; the
  review/adversarial gate is non-negotiable; the cost caveat stated so it's
  followable.
- **#63** `.claude/settings.json` SessionStart hook → `.claude/hooks/route_reminder.py`
  reinjects the routing discipline every session (no network, stdlib print).
- **#64** `verdict_recorded` verifier — current-sprint run-manifests must carry
  a non-empty `verdicts:` field; SKIP-aware, non-retroactive.
- **#65** real skills at the discovery path: `.claude/skills/run-gate/` and
  `.claude/skills/scaffold-sprint/` (procedure-only). Fixed `audit_skills.py` to
  scan `.claude/skills/` (Python `**` skips hidden dirs — the ceiling had
  silently stopped applying there).
- **#66** `WORKFLOW.md §1` "the gate is implementer-agnostic" + worked example +
  the caveat; `ORCHESTRATION.md` "writes no product code" softened to "never
  ships a major output past the gate" with the honest inline exception.
- Gate is now **14 verifiers**, all PASS.

## Decisions
- **Ran the falsifier pass as a real gate on this very work** (the #66
  discipline, applied to itself) and it earned its keep twice:
  1. `verdict_recorded` PASSed a fixture that should have FAILed — a `\s*` in the
     verdicts regex crossed the newline and captured the closing ``` fence.
     Fixed to horizontal-whitespace matching `^[ \t]*verdicts:[ \t]*(.*)$`.
  2. `audit_skills` reported "0 SKILL.md" — Python's `**` glob skips
     dot-directories, so the two new `.claude/skills/` files were unaudited.
     Fixed to glob the hidden path explicitly.
  Both are exactly the "presume this is wrong, construct the disproof" pass the
  epic says was habitually skipped. Recorded here as the verdict artifact.
- **Inline was the correct call this run, and that's consistent with #66, not a
  violation of it.** The personas become runtime-callable only in a *new*
  session (the harness loads `.claude/agents/` at start); this session couldn't
  spawn them, and the work is tightly-coupled infra. The caveat covers exactly
  this — the non-negotiable was the gate, which ran.
- **Personas are committed, not gitignored** (like INDEX.md) so a fresh clone's
  runtime discovers them; `personas_installed` keeps them honest.

## Blocked / carried
- The payoff is next-session: with `.claude/agents/` populated and the
  SessionStart hook live, roster roles are finally callable `subagent_type`
  values and the routing directive fires. First real test is whether the next
  substantial task actually routes.
- #56 (owner still interpreting data) and #53 remain open.
