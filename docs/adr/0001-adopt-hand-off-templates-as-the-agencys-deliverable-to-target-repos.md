# ADR-0001: Adopt hand-off templates as the agency's deliverable to target repos

**Status**: accepted
**Date**: 2026-07-26 · **Deciders**: `logicians/software-architect`, `pm/project-manager`, repo owner · **Owner (A)**: `logicians/software-architect`
**Traces to**: issue #79 (epic) / #80–#92 · `docs/reviews/delivery-audit-2026-07.md`

## Context

Three delivery-review audits (#75–77) flagged the agency as missing standard
SDLC artifacts: SRS, ADRs, Design Specs, a traceability matrix, release-decision
records. Taken literally, that reads as "the org fails its own SDLC." But
Ges-Talt is a **meta-repo — an agency that builds and hands work to other
repos**, not a product codebase with its own shippable feature. Filling in an
SRS *for this repo* would be theatre; there is no product here to specify.

The load-bearing question the audits forced: when the agency lacks an "SRS," is
the fix to write one, or to write the *template and convention* an assigned
agent uses to produce one **in a target repo**?

## Options considered

1. **Fill in the artifacts for this repo** — author a real SRS/Design-Spec/risk
   register describing Ges-Talt itself. Rejected: this repo has no product
   surface; the artifacts would be contentless ceremony, and the freshness
   burden would rot them (the exact anti-pattern the audits warn about).
2. **Ignore the gaps as "not applicable to a meta-repo"** — declare the SDLC
   checklist off-scope. Rejected: the agency's *whole job* is to carry work
   through an SDLC; having no template to hand over is a real capability hole,
   not a false positive.
3. **Ship the templates/conventions/verifiers, not filled-in artifacts** — add
   `docs/templates/{adr,srs,design-spec,…}.md` plus conventions and fitness
   functions, so an assigned role can instantiate them in whatever repo it's
   working. Chosen.

## Decision

We will close the audit gaps by shipping **templates, conventions, and
verifiers** — the reusable machinery an agent hands to a target repo — rather
than filled-in artifacts for this meta-repo. Every growth child (#80–#92) is
accepted only when it delivers a template/convention/verifier, not a one-off
document about Ges-Talt.

## Consequences

- **Positive** — the agency gains a genuine, reusable SDLC hand-off kit;
  additions are content-light and don't rot; the meta-repo/product distinction
  is now explicit and defensible.
- **Negative / accepted cost** — a reader expecting a conventional repo will
  find templates where they expected filled artifacts; the value is realized
  only when the agency is pointed at a target repo. Tracked in
  `docs/risk-register.md`.
- **Neutral / follow-on** — where a property *is* checkable in this repo
  (traceability, doc freshness), we also ship the verifier so the convention is
  enforced, not merely documented.

## Verify

`docs/templates/` contains adr/srs/design-spec/release-decision/risk-assessment/
vulnerability-assessment/erd/customer-feedback templates; `scripts/verifiers/`
contains `traceability.py` and `doc_freshness.py`; `docs/reviews/delivery-audit-2026-07.md`
records the framing. Superseded only by an ADR that re-scopes Ges-Talt from a
meta-repo to a product repo.
