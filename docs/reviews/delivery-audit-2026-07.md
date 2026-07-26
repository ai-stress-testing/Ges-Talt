# Delivery-review audit + org comparison (issues #75–78)

2026-07-26. Three roster subagents audited the current Ges-Talt agency against
the owner's three phase-gate delivery checklists; the orchestrator compared
the roster against the owner's alternative model-tiered org (#78). This is the
durable synthesis; the growth opportunities became issues #79 (epic) + its
children.

**Method** (routed through the now-live roster, ledger-recorded):
- #75 Intake → `pm/team-operations` (57,867 tok)
- #76 Design & Systems → `logicians/software-architect` (63,552 tok)
- #77 Dev/Verification/Release → `logicians/code-reviewer` (61,473 tok)
- #78 org comparison → orchestrator (inline)

## The framing that governs everything below

This is a **meta-repo (an agency), not a product SDLC repo** (software-architect's
caveat). Most "MISSING" items are not the org failing its own SDLC — they are
**conventions/templates the agency should be able to *hand to a target repo***
and doesn't yet have. That distinction sets the acceptance bar: ship the
template/convention/verifier, not a filled-in artifact for this repo.

## Where the agency already exceeds the checklists (do not rebuild)

- **Progress is mechanized, not asserted** — the 15-machine hard-verifier
  registry + `gate.py` + `verdict_recorded` realize "measured by evidence,
  hard to game" as fail-closed code, not prose.
- **SSOT by generation** — INDEX/repo-map/personas are generated-not-authored
  with freshness verifiers; duplication-as-entropy is a machine gate.
- **AI-assisted-dev validation** exceeds the ask — falsifier "presume wrong",
  reality-checker re-execution, grader-independence + anti-grader-gaming, the
  pre-PR comprehension quiz.
- **Risk-tiered review (#74)** scales review cost to blast radius — more mature
  than the checklists' uniform review.
- **Negative prompts, consultation-proximity, closed feedback loop, executable
  architecture governance (fitness functions), reflexive security
  (THREAT-MODEL on itself), architectural YAGNI** — all beyond the checklists.

## The gaps, by phase (the highest-value only)

| Phase | Biggest MISSING/PARTIAL |
|---|---|
| **#75 Intake** | RACI + named ownership; stakeholder 2×2; a documented prioritization framework (RICE/MoSCoW/Kano); customer-feedback intake artifact; business-case/ROI in the PRD; a *named* consolidated Definition of Done; marketing/launch ownership (a real roster hole). |
| **#76 Design/Systems** | **End-to-end traceability matrix** (the forward-reference rule is only half; downstream "every requirement → a test" is unenforced); ADR home; SRS / Design-Spec / blueprint-diagram (GT-20) / ERD templates; unified risk register. |
| **#77 Dev/Release** | **Tiered T1–T4 testing budget** + flake-budget policy (≤1%); README-for-AI-agents + ops-readiness (arch overview, env setup, troubleshooting); repo health (LICENSE, badges, dependency surface); per-doc owner+last-validated metadata + staleness verifier; Release-Decision / Risk-Assessment / Vulnerability-Assessment templates; formal UAT sign-off. |

## #78 — org comparison (model-tiered seniority ladder)

The alternative organizes ~115 roles by **seniority × model-intelligence tier**
(opus VP/CISO/CLO/PM-director → sonnet managers → fable/sol seniors → local
qwen/gemma/terra/luna for mid/jr/entry), repeating the *same function* at 4–5
model tiers. Ges-Talt organizes by **function**, one cheapest-sufficient model
per role, mesh topology, no seniority ladder.

**Adopt:**
- **Per-role model-tier escalation ladder + a `local` tier** — the marquee
  idea, reframed: not 5 roles per function, but one role that routes a task to
  the cheapest tier (incl. local models) and escalates only on complexity. A
  granular upgrade to "cheapest-sufficient" and the biggest token-economy win.
- **A thin accountability layer** — name the "Accountable" heads (CISO ≈
  security/architect, CLO ≈ general-counsel, a delivery/PM director ≈
  delivery-lead) to close #75's RACI/ownership gap — *without* a manager tier
  (that reintroduces the star-topology chokepoint the mesh rejects).
- **Evaluate genuine role gaps**: support/IT-ops, research-scientist, a unified
  GRC lens. (Flag for owner decision — roster shape is the owner's call.)

**Do not adopt:** the seniority hierarchy itself (chokepoint risk), the
~115-role duplication (a tier ladder *within* a role is leaner), and nothing
that dilutes the governance machinery (#78 has no verifiers/ledger/threat model
at all — that is Ges-Talt's core advantage).

## Verdict

The agency is **stronger on governance and evidence** than all three checklists
and #78; it is **weaker on hand-off-ready artifacts** (templates/conventions a
target repo consumes) and on **fine-grained resource tiering** (#78's model
ladder). The growth issues target exactly that asymmetry.
