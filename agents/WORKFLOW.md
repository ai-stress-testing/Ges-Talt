# Workflow — verdict loop + delegation

Closes GT-10 and Audit-2 weaknesses 1, 2, 10. Convention, not a new
agent — no roster changes required to follow it.

## 1. Verdict loop

Path: sub-issue → implementer (per its `agent.md`) → static review
(`logicians/`) → empirical verification (`testing/`) → verdict.

A verdict is **PASS** or **FAIL**. Nothing else — no "PASS with notes,"
no numeric score.

**FAIL handback** — one entry per issue found, each carrying:
- `expected` — the acceptance criterion, quoted verbatim
- `actual` — what was observed instead
- `evidence` — file path, command output, or screenshot ref
- `fix instruction` — the specific change to make
- `files to touch` — exact paths

Plus an `attempt` counter (N of 3), carried forward on every handback.

**Retry rule**: the implementer fixes only the listed issues. No new
scope, no drive-by refactors, no "while I'm in here." Re-submit for the
same review → verify cycle.

**Escalation**: attempt 4 auto-escalates to `pm/project-manager` with
the full failure history (what was tried each attempt, why it still
failed). PM picks one of: reassign, decompose, revise approach,
accept-with-limitations, defer — and informs the human of the call.

**PASS path**: static review + empirical verification both PASS on the
stated acceptance criteria → the **hard-verifier gate** (§5) is green for
the properties the change touches → `testing/reality-checker` re-verifies the
evidence as the final gate → done. Reality-checker can still bounce it
back to FAIL; its verdict is the one that ships.

**Closing the issue** (issue #28): a PASS is not done until the issue is
closed. The assigned agent (or the orchestrator on its behalf) posts the
closing `COMMS.md` attribution and closes the GitHub issue with
`state_reason: completed`. An issue left open after a reality-checker PASS
is unfinished work, not a formality — the loop's terminal state is a
closed issue, not a green verdict. A FAIL never closes; it hands back.

**The gate is implementer-agnostic** (issue #66). The verdict loop is not a
thing that only happens when work is *delegated*. Whoever produces a major
output — a delegated subagent **or the orchestrator writing inline** — the
review/adversarial gate runs before it ships, and is *recorded*:

- **Consultation-proximity at spec time** — security (OPSEC) and legal
  constraints enter before implementation, in the proximity order of
  `ORCHESTRATION.md`. Recorded, not assumed.
- **The review pass, risk-tiered** (issue #74) — the *depth* of review scales
  with blast radius, because the `logicians/falsifier` pass is expensive
  (opus, adversarial) and firing it on every change is the over-triggering the
  owner flagged:
  - **Critical systems** — authentication/authorization, API boundaries,
    payments/billing, crypto/secrets, irreversible or data-loss operations —
    get the explicit `logicians/falsifier` "presume this is wrong, construct
    the disproof" pass, result written down (PASS with attempts listed, or the
    counterexample). `logicians/software-architect` joins where structure is
    at stake.
  - **Lower-risk changes** — the linter/test-suite gate stands in for the
    falsifier: `scripts/verify.py` (+ `scripts/gate.py` once it lands) plus
    the relevant `testing/` role. Prefer **Playwright E2E**
    (`testing/test-automation-engineer`) as the empirical gate wherever a
    UI/flow is involved — use it in more cases, not fewer. No falsifier pass
    is required for these; the gate's PASS is the verdict.
- **The recording** — either way the outcome lands in the sprint-log
  run-manifest's `verdicts:` field and a `COMMS.md` attribution line ("lint +
  Playwright PASS" is a valid recorded verdict; a falsifier verdict is not
  mandatory for non-critical work). "I considered it informally" does not
  count; the criterion is the artifact. `§5`'s `verdict_recorded` verifier
  gates that *a* verdict is recorded, not which tier produced it.

*Worked example* — the run that added the `verdict_recorded` verifier
(GT-64) ran a falsifier pass on it: "presume it never fails." A fixture with
an empty `verdicts:` field was constructed; the verifier passed when it
should have failed (a `\s*` in the regex swallowed the newline and captured
the closing fence). The disproof was the counterexample; the fix was
horizontal-whitespace matching; the run-manifest recorded
`verdicts: verify.py PASS (falsifier caught + fixed an empty-verdicts miss)`.
That is the gate doing its job — and it is the part most easily skipped.

**The caveat, so this stays followable.** Delegation is not free — cold
subagents re-derive context, cost tokens, and can collide on shared files.
Keeping a single tightly-coupled change inline is often the right call and is
*not* a violation. This is not "fan out everything." The non-negotiable is
that a major output carries a **recorded, risk-appropriate verdict** — the
falsifier for critical systems, the lint/test gate otherwise (issue #74). The
failure is shipping a major output with *no* recorded verdict, or spending the
opus falsifier on a change a linter already covers; implementing a small
change yourself, or gating a routine one with lint+test, is not.

## 2. Delegation rules (de-chokepoint the PM)

The PM does not personally re-review work that already has a
reality-checker PASS — that verdict *is* the acceptance sign-off.

Route by altitude, not habit:
- Portfolio-level tradeoffs (competing initiatives, resourcing) →
  `pm/delivery-lead`
- Initiative/multi-sprint milestone decisions → `pm/program-tracker`
- Everything else implementation-shaped → the assigned agent, per its
  own handoff

`pm/project-manager` personally arbitrates only:
- spec ambiguity (PRD doesn't say)
- cross-team conflict (two roles, one deliverable, disagreement)
- scope changes (mid-flight addition to an issue)
- retry-cap escalations (§1)
- access-widening sign-offs (security-relevant — stays with PM, not
  delegated to delivery-lead or program-tracker)

## 3. Incident routing rule

An ambiguous page (broken vs. malicious, not yet known) goes to
`cd/sre` first — availability triage.

The moment malice is suspected: hand off to
`security/incident-responder` and stop making ops changes on the
affected system. Containment from that point is IR's call, not SRE's —
further live changes can destroy evidence.

`incident-responder` owns the incident from handoff forward, including
notifying `legal/data-protection-officer` (the 72h breach-notification
clock starts at confirmed breach, not at page time).

## 4. Run manifest

Every run's sprint-log entry opens with a structured run-manifest header —
run-id, prompt, agents spawned, specs, verdicts, commits (`ORCHESTRATION.md`
"Run manifest"). The verdict loop's outcome (§1 — PASS, or the FAIL history
up to escalation) is the `verdicts` field of that header; write it once the
loop settles, not mid-retry.

## 5. Hard-verifier gate (GT-43)

The efficacy arm of the loop. Where §1's review roles reason about whether a
change is right, the **hard verifiers** in `scripts/verifiers/` *decide* one
property each — binary, with a counterexample, fail-closed
(`docs/opsec/hard-verifiers.md`). `scripts/verify.py` composes them; a major
output does not take the PASS path (§1) until the verifiers for the
properties it touches are green, the same way `build_index.py` /
`verify_comms.py` already gate the roster.

- **One property, one machine.** Each `scripts/verifiers/<name>.py` exposes
  `PROPERTY` / `METHOD` / `OWNER` / `check() -> (status, detail)`; the runner
  prints failures first and exits non-zero on any FAIL. `SKIP` means the
  property is N/A here (e.g. not a git repo) and does not fail the gate.
- **Fail closed.** A verifier that raises is a FAIL, never a silent pass —
  absence of a PASS is a FAIL.
- **The security/PM team writes and owns verifiers; it is not the verifier.**
  A persona reasons and maintains the machine; the machine gates. Add a
  verifier when a property is worth enforcing every run, not narrating once.
- **Deterministic > probe > reason.** Prefer a static assertion that always
  answers; a `reason`-method verifier (`logicians/falsifier`,
  `ai/model-evaluator`) is only for properties code can't decide.

Seed registry (run `python3 scripts/verify.py --list`): roster pairing,
reason-tier read-only boundary, handoff-reference resolution, INDEX
freshness, ledger well-formedness, tools-baseline containment, current
sprint window, branch taxonomy (`docs/branching.md`), repo-map
freshness, **downstream traceability** (`traceability` — every
requirement/AC terminates in a test, `docs/traceability.md`), and
**doc freshness** (`doc_freshness` — governed convention docs carry a
non-stale `owner`/`last_validated` marker, `docs/doc-metadata.md`). These
secure the agent org itself (`hard-verifiers.md`: "the machine that
secures the machines"); target repos drop their own domain verifiers into
the same `scripts/verifiers/` registry.

The consolidated **Definition of Done** (`docs/definition-of-done.md`)
names, in one place, every gate a major output clears — this verifier gate,
the risk-tiered §1 review, traceability, and the recorded verdict. For a
release, the go/no-go is recorded via the `release-readiness` skill
(`docs/templates/release-decision.md`).

## 6. Pre-PR comprehension check (issue #73)

Before opening a pull request (or pushing a substantial change), the agent
poses a short **multiple-choice quiz** to the human on what the change does —
the anti-slop, human-in-the-loop gate. Owned by
`pm/ticket-workflow-steward` (it sits on the PR path, alongside branch/commit
convention).

- **3–5 questions**, multiple choice, drawn from the actual diff. Two kinds:
  (a) *what changed* — a small "read this hunk, what does it now do?"
  LeetCode-style question grounded in the real code; (b) *why* — a decision
  the change made and the alternative it rejected (the load-bearing call, not
  trivia). One correct answer each, plausible distractors.
- **Purpose is understanding, not a grade.** The point is to force the human
  to engage with what's being merged so AI slop doesn't sail through
  unread, and to build the reviewer's instinct for the codebase. A wrong
  answer is a signal to slow down and read, not a blocker.
- **Scope to substance.** Skip it for a docs typo or a mechanical rename; run
  it when the diff carries real logic or a decision worth understanding —
  the same "major output" bar as the review gate (§1).
- **Not a script.** Generating good questions from a diff is judgment, not
  deterministic scaffolding (`issue #67` non-goals) — the agent authors the
  quiz per change; it is not `scripts/`-automated.
