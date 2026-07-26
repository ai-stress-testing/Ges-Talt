<!-- owner: pm/project-manager · last_validated: 2026-07-26 -->
# Traceability — closing the downstream half (#80)

The agency already enforces the **forward** half of traceability: an issue
that doesn't cite a `prd.md §n` or a user journey isn't created
(`docs/templates/issue-spec.md`, `agents/WORKFLOW.md`). What it did not
enforce is the **downstream** half — that every requirement/acceptance
criterion terminates in a *test or an operational metric*, not just a merged
diff. This convention makes the chain bidirectional and, where it can be
mechanized, machine-checked (`scripts/verifiers/traceability.py`).

## The chain

```
Business goal → PRD §n → (SRS req) → Design → Architecture (ADR)
             → API/DB → Impl task (issue/sub-issue) → Acceptance criteria
             → Test / verifier → Deploy → Operational metric
```

Each link **references** the one above it (SSOT — issue #76's "answer a
question once"); no artifact exists without an upstream purpose or a
downstream verification. The rule is symmetric:

- **No orphan upstream** — a requirement with no downstream test/metric is
  unverifiable and fails the gate.
- **No orphan downstream** — a test/artifact with no upstream requirement is
  scope the PM never authorized (surface it, don't silently keep it).

## How it is recorded (meta-repo shape — no SDLC phase folders)

Traceability maps onto the structures the repo **already has**, rather than
introducing `02-design/ 03-engineering/` phase folders (issue #76 non-goal):

| Link | Where it lives |
|---|---|
| Business goal → PRD | `docs/sprint-*/prd.md` (numbered `§n`) |
| PRD → issue/AC | issue-spec `**Source**: prd.md §n` + acceptance criteria |
| AC → test/metric | a `Verify:` line naming a command, a `testing/` role, or a `scripts/verifiers/<name>.py` |
| decision → ADR | `docs/adr/NNNN-*.md` (see `docs/templates/adr.md`) |

For a **target repo** the agency onboards, the same chain is expressed with
that repo's SRS/OpenAPI/test-suite; this file is the convention the agency
hands over, not a filled-in matrix for Ges-Talt.

## The verifier (fitness function)

`scripts/verifiers/traceability.py` asserts the downstream half where it is
machine-checkable in *this* repo: **every acceptance-criterion block in the
current sprint's issue-specs carries a `Verify:` line** (a command, a testing
role, or a verifier). A criterion with no verification link is the
counterexample. It is GT-43-style: single-property, fail-closed, SKIP when
there are no issue-specs to gate yet. It does not replace the forward
discipline — it completes it.

## What this is not

- Not a new gate on top of the verdict loop — it is the loop's *coverage*
  property, registered alongside the others in `scripts/verify.py`.
- Not a demand for phase-folder SDLC ceremony — it rides the sprint/verifier
  structure that exists.
