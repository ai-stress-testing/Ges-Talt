# ADR-NNNN: <short decision title>

**Status**: proposed | accepted | superseded by ADR-MMMM | deprecated
**Date**: YYYY-MM-DD · **Deciders**: `<team/role>`, … · **Owner (A)**: `<team/role>`
**Traces to**: `prd.md §n` / issue #n / `docs/…` (the upstream reason — no
ADR without one, per `docs/traceability.md`)

## Context

The forces at play — technical, business, team — that make a decision
necessary. State the problem and the constraints, not the answer. A reader
who disagrees with the decision should still agree this is the context.

## Options considered

1. **<option>** — one line on what it is; its cost/benefit; why in or out.
2. **<option>** — …
3. **<option>** — …

At least the rejected options that were genuinely on the table. An ADR that
lists only the chosen path is a changelog, not a decision record.

## Decision

The option chosen, in one or two sentences, active voice: "We will …".

## Consequences

- **Positive** — what this buys us.
- **Negative / accepted cost** — what we give up or take on (the debt this
  creates traces to `docs/risk-register.md`).
- **Neutral / follow-on** — what now becomes possible or necessary.

## Verify

How a later reader confirms this decision still holds (or has been
superseded): the code/doc that embodies it, or the ADR that replaced it.

<!--
Stamp a new ADR with: python3 scripts/new_adr.py "<title>"
It allocates the next NNNN, writes docs/adr/NNNN-<slug>.md from this template,
and (re)builds docs/adr/README.md as the index. ADRs are immutable once
accepted — a reversal is a NEW ADR that supersedes, never an edit in place.
-->
