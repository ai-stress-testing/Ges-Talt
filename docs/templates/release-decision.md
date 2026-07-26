# Release Decision — <release / version>

**Owner (A)**: `cd/release-engineer` · **Date**: YYYY-MM-DD ·
**Traces to**: issue #n / `prd.md §…`

The go/no-go record for a release (issue #77). Cross-references the gates that
already exist (`agents/WORKFLOW.md`, `docs/definition-of-done.md`,
`scripts/gate.py`) — it does not re-run them, it records their outcome and the
decision. Not a release *tool*; a release *decision artifact*.

## Blockers — do NOT release if any is true

- [ ] Core business logic fails.
- [ ] Data integrity is compromised.
- [ ] A security finding exceeds risk tolerance (see the Vulnerability
      Assessment; critical-path findings triggered the falsifier gate, #74).
- [ ] Acceptance criteria are incomplete (`docs/traceability.md` shows an
      unverified requirement).
- [ ] Definition of Done is unmet (`docs/definition-of-done.md`).
- [ ] `scripts/gate.py` is not green.

Any box checked ⇒ **NO-GO**. No overrides without a named accountable owner
and a recorded reason.

## Backlog candidates — may be deferred with approval

Minor issues that do NOT block: cosmetic defects, low-priority UX polish, doc
enhancements, non-critical improvements. List each with the issue it becomes.

## Gate results (recorded, not re-argued)

| Gate | Result | Evidence |
|---|---|---|
| Code review | PASS/FAIL | link |
| Tests (risk-tier per #74) | N/N PASS | `gate.py` / `verify.py` |
| Security review | PASS/FAIL | Vulnerability Assessment |
| Performance | within budget | perf report |
| UAT sign-off | approved | who + date |

## Decision

**GO / NO-GO**, one line, with the accountable owner's name and date. A NO-GO
names the single blocking condition and the issue that tracks clearing it.
