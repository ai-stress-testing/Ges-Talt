<!-- owner: pm/program-tracker · last_validated: 2026-07-26 -->
# Unified risk register (#90)

Risk was **real but siloed** across three registers — `legal/general-counsel`'s
legal-risk register, `pm/program-tracker`'s delivery-risk register, and
`environments/THREAT-MODEL.md`'s security register. No single view spanned
technical + operational + business + security, and there was no tech-debt
*forecast* convention. This is the federating view.

## Principle: federate, don't collapse

The three specialist registers stay where they are and remain authoritative
for their domain (SSOT — issue #76). This view **references** them; it does not
copy their rows. Collapsing them into one file would create three stale copies;
linking them creates one lens over three live sources.

| Domain | Authoritative source | Owner (A) |
|---|---|---|
| Security | `environments/THREAT-MODEL.md` | `security/architect` (CISO) |
| Legal / compliance | `legal/general-counsel` risk register | `legal/general-counsel` (CLO) |
| Delivery / program | `pm/program-tracker` risk register | `pm/delivery-lead` |
| Technical / operational / business | this view + per-initiative PRD "Risks" | `pm/program-tracker` |

## The unified view

Each active risk, whatever its domain, is visible here with a mitigation and a
named accountable owner. A risk with no owner is not tracked — it's an unowned
liability (`docs/templates/risk-assessment.md`).

| ID | Risk | Domain | Likelihood | Impact | Mitigation | Owner (A) | Source |
|---|---|---|---|---|---|---|---|
| R-1 | _example_ meta-repo value only realized against a target repo | business | M | M | onboard a pilot target repo; templates are hand-off-ready | `pm/delivery-lead` | ADR-0001 |

Populate per initiative; every PRD "Risks & assumptions" entry (#85) lands a row
here.

## Tech-debt forecast

`cd/lifecycle-manager` tracks the lifecycle of long-lived artifacts *after*
they exist; this extends it to a **forward forecast** — predict debt *before*
implementation, at spec time:

- Each significant design decision (an ADR) names the debt it knowingly incurs
  (`docs/templates/adr.md`, "Negative / accepted cost").
- Forecasted debt lands here as a risk row with a review trigger (the condition
  that would force paying it down).
- Predicting debt before implementation is an explicit intake step
  (`docs/prioritization.md` effort estimate + PRD risks).

## Verify

Every risk row has a mitigation and an accountable owner; every domain register
is linked, not duplicated. Carries the `doc_freshness` marker so this view
can't rot unnoticed.
