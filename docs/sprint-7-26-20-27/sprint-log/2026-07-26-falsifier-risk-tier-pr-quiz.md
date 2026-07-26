# 2026-07-26 — Recalibrate the review gate (#74) + pre-PR comprehension quiz (#73)

**Session/agent**: main session (orchestrator, direct — tightly-coupled
convention/policy edits across a few files; not a critical system, so gated by
lint/test per the very policy this change installs, no falsifier pass).
**Issues touched**: #73, #74 (GitHub); GT-73, GT-74.

```
run-id: 2026-07-26-falsifier-risk-tier-pr-quiz
prompt: "See issues, update the agency accordingly." (acted on the two fresh owner issues that recalibrate agency behavior: #74, #73)
agents: main session only (policy/doc edits; no measured subagent token cost to ledger)
specs: falsifier charter; WORKFLOW.md §1 (risk-tiered gate) + §6 (PR quiz); CLAUDE.md Routing; .claude/hooks/route_reminder.py; logicians/README.md
verdicts: verify.py 14/14 PASS + build_index/verify_comms/credit/audit_skills PASS — the lint/test gate, which IS the correct tier for a non-critical policy change (#74). No falsifier pass: doing so would be the over-triggering #74 flags.
commits: (see push)
```

## Done
- **#74 — risk-tier the falsifier gate.** Owner feedback: the "anti logician"
  (falsifier) was firing 2–4× per query; it should be reserved for critical
  systems, with a linter/test-suite standing in for lower-risk reviews, and
  more Playwright. Implemented that recalibration everywhere the old
  "falsifier on every major output" rule lived:
  - `agents/logicians/falsifier/agent.md` — description now leads "Use for
    critical-path changes (auth, API, payments, crypto/secrets, irreversible/
    data-loss ops)…; for lower-risk changes a linter/test gate stands in";
    added a "When to invoke" scope block and a Never ("fire on a low-risk
    change the linter already covers").
  - `agents/WORKFLOW.md §1` — the gate is now **risk-tiered**: critical →
    falsifier; lower-risk → `verify.py` + `testing/` (Playwright E2E preferred
    "in more cases"). Recording still required either way; `verdict_recorded`
    checks *a* verdict exists, not which tier. Caveat reworded to "a recorded,
    risk-appropriate verdict."
  - `CLAUDE.md` Routing + `.claude/hooks/route_reminder.py` — both softened
    from "an explicit falsifier pass" to the tiered rule, so the session-start
    nudge stops pushing over-invocation.
  - `agents/logicians/README.md` — falsifier one-liner marked "reserved for
    critical systems."
- **#73 — pre-PR comprehension quiz.** `WORKFLOW.md §6`: before a substantial
  PR, the agent poses a 3–5 question MCQ drawn from the diff — (a) what a hunk
  now does, (b) which decision was made and what it rejected — to force human
  engagement and curb AI slop. Owned by `pm/ticket-workflow-steward`. Scoped to
  substance (skip docs typos/renames); explicitly *not* a script (question
  generation is judgment, per #67 non-goals).

## Decisions
- **Applied #74 to its own implementation.** This change is conventions/policy,
  not a critical system, so the correct gate is the lint/test gate (14/14
  PASS) — I deliberately did **not** spawn the falsifier on it. Spawning the
  opus adversarial reviewer on a docs-policy edit is exactly the over-firing
  the owner is complaining about; the disciplined move was to not.
- **#66 refined, not reversed.** #66 made "a recorded verdict" non-negotiable;
  #74 fixes the *tier*: the verdict for non-critical work is lint/test, not a
  falsifier pass. The non-negotiable is now "a recorded, risk-appropriate
  verdict," and the failure modes are symmetric — shipping with no verdict, OR
  spending the opus falsifier on a routine change.
- **Kept inline, on purpose.** Five files, one tightly-coupled policy change; a
  cold subagent would re-derive all of it. This is the caveat's inline case,
  and — given #74 — forcing a spawn here would contradict the very lesson.
- **Scope of "update the agency accordingly":** acted on the two fresh owner
  issues that change agency *behavior* (#74 gate policy, #73 PR workflow).
  Left the automation epic (#67–#72, tooling not agency) and the older broad
  issues (#7 API-hardening, #16 enterprise-enhancements, #11 memory-safety,
  #56 location-analytics) for a follow-up — flagged to the owner.

## Blocked / carried
- Offered next: implement the #67–#72 automation epic (gate.py etc.), or take
  #7/#56 (both recently edited by the owner). Awaiting direction on scope.
- #53 remains open.
