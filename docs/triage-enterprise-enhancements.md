# Triage — Enterprise Enhancements (issue #16)

Owner's 28 candidate categories, triaged against what's actually in the
repo today plus what's already landing in parallel (#17-#20, #14). Verdict
key: **covered** (exists, file named), **landing now** (cite the issue),
**worth a ticket** (concrete next step + owner), **defer/off-mission**
(honest reason, not a gap to backfill).

| Category (owner's term) | Verdict | Where / Why |
|---|---|---|
| decomposition in composition | covered | `agents/pm/project-manager/SPEC.md` — decomposes a goal into issues + sub-issues per `docs/templates/issue-spec.md`; that *is* decomposition-in-composition. |
| Lifecycle management | landing now | #17 — `lifecycle-manager` role. |
| Testing | covered | `agents/testing/` — 8 roles (`agents/INDEX.md`), plus the verdict loop in `agents/WORKFLOW.md`. |
| requirement management | covered | `docs/templates/prd.md` + `docs/templates/issue-spec.md` (checkable acceptance criteria, traced to PRD §n) — that's the requirement-management artifact chain. |
| quality management | landing now | #18 — `falsifier` role. Baseline already exists via `agents/WORKFLOW.md`'s binary PASS/FAIL verdict loop; #18 deepens it. |
| enterprise sustainability | worth a ticket | No environmental/financial-longevity surface, but the *token-cost* reading of "sustainability" is real for an agent-heavy repo — one line added to `agents/devops/finops-engineer/SPEC.md` to track agent-invocation spend closes the only sense of this term that applies here. |
| agile | covered | `CLAUDE.md`'s `sprint-<m>-<y>-<dd>-<dd>/` convention + `docs/backlog.md` + dated `sprint-log/` entries is a running scrum-like cadence already, not a proposal. |
| categorization in classification | covered | `agents/INDEX.md` — generated team→role taxonomy, linted by `scripts/build_index.py`. |
| enterprise tearing [tiering] | landing now | #19 — `docs/enterprise.md` Tiering section. Template already scaffolded: `docs/templates/enterprise-doc.md` §Tiering. |
| enterprise ontology | landing now | #19 — same doc, §Ontology (`docs/templates/enterprise-doc.md`). |
| enterprise taxonomy | landing now | #19 — same doc, §Taxonomy (`docs/templates/enterprise-doc.md`); distinct from the team/role taxonomy already covered above (`agents/INDEX.md`). |
| enterprise Romantics [semantics] | landing now | #19 — same doc, §Semantics (`docs/templates/enterprise-doc.md`) — a project glossary. |
| periodic table of enterprise elements | defer/off-mission | EA-consultancy artifact (a poster, not a workflow); nobody in this roster would own or update it, and a personal staging repo has no landscape big enough to need one. |
| Meta objects | covered | `agents/TEMPLATE/agent.md` + `agents/TEMPLATE/SPEC.md` — the field schema (name/description/tools/model/persona/capabilities/acceptance criteria/handoffs) every role instance conforms to. That schema *is* the meta-object set. |
| enterprise Meta model | covered | Same as above — `agents/TEMPLATE/` plus `docs/templates/` is the meta-model every doc/agent instance is stamped from. |
| artifacts and templates | covered | `docs/templates/` (prd, issue-spec, sprint-log-entry, user-journey, enterprise-doc) + `agents/TEMPLATE/`. |
| L E A D way of structuring | landing now | #20 — LEAD structuring folded into the PM charters. |
| information and system systems engineering [information & systems engineering] | covered | Split across the roster's three architects: `agents/platform/software-architect`, `agents/backend/backend-architect`, `agents/security/architect` (domains disjoint on paper per `AUDIT.md`'s "Three architects" watch-item). |
| data monetization | defer/off-mission | No data product, no customers, nothing to monetize — this is a personal staging repo (`README.md` line 3). |
| multi experience | defer/off-mission | No omnichannel product surface (voice/wearable/chat); `frontend/`, `mobile/`, `design/` each own one surface at a time, and there's no cross-channel product to unify. |
| user democratization | defer/off-mission | Needs a BI/self-serve data surface to democratize access *to* — none exists (`AUDIT.md` Audit-1 gap 6, analytics/BI unowned); a democratization layer on top of a gap that doesn't exist yet is two hops of speculation. |
| human augmentation | defer/off-mission | The EA-buzzword sense (wearables/cognitive augmentation tech) has zero surface here. The repo's own premise — agents assisting a human developer — is a different, already-realized sense of the phrase, not a ticket to cut. |
| blueprinting | worth a ticket | Service-blueprint step sits adjacent to `agents/design/ux-architect` (IA/taxonomy work) and `docs/templates/user-journey.md` (actor/steps/failure-mode table), but nobody owns a cross-team service blueprint today. Natural owner: `design/ux-architect`. |
| implementation | covered | Every implementer team (`backend/`, `frontend/`, `data/`, `devops/`, `ai/`, `mobile/`, `platform/`, `networking/`) executing the "Build" step of `agents/WORKFLOW.md`. |
| enterprise navigator | covered | Closest real analog: `agents/pm/delivery-lead/SPEC.md` (portfolio-level prioritization, resourcing tradeoffs, executive status reporting) and `agents/pm/program-tracker/SPEC.md` (cross-team dependencies, risk register) — the "help me navigate competing initiatives" function this term describes. |
| packaged business capabilities | defer/off-mission | PBC governs composable enterprise applications; this repo ships no product modules to package. Loose analog only: each agent role is already a self-contained contract (`agents/README.md`'s agent.md+SPEC.md convention) — formalizing a PBC layer on top would be over-fit for a personal repo. |
| SMART city and digital city | defer/off-mission | No civic/IoT surface of any kind. Zero relevance. |
| productisation | defer/off-mission | `README.md` states the opposite explicitly: "Personal Claude Code staging environment," not a product being productized. |

## Recommended tickets

Ranked laziest-first — only the two rows above marked "worth a ticket":

1. **Token-cost sustainability note** — add one bullet to
   `agents/devops/finops-engineer/SPEC.md` acknowledging agent-invocation
   token spend as a tracked cost line. One line, no new role, no new file.
2. **Service blueprinting** — extend `agents/design/ux-architect/SPEC.md`
   capabilities to include a cross-team service-blueprint deliverable,
   reusing `docs/templates/user-journey.md`'s actor/steps/failure-mode
   shape rather than inventing a new template.

## Closing assessment

Most of the 28-category framework is Gartner/TOGAF-shaped enterprise-
architecture vocabulary built for a company with real customers, real data,
and real physical/digital channels to govern — `data monetization`,
`multi experience`, `SMART city`, `packaged business capabilities`, and the
`periodic table of enterprise elements` describe problems this repo
doesn't have, and inventing owners for them would be exactly the kind of
padding CLAUDE.md's YAGNI stance and the roster lint (`scripts/build_index.py`)
exist to prevent. Where the framework does line up — tiering, ontology,
taxonomy, semantics, lifecycle, quality, LEAD structuring — it's because
those categories describe documentation and process disciplines the repo
already needed for its own agent org, not because the framework is being
served for its own sake; #17-#20 close them as a byproduct of running the
org, not as framework compliance. Net: treat issue #16 as a checklist to
mine for the handful of categories that map to real gaps (two tickets
above), then close it — running the full 28-category program on a
personal staging repo would fight the repo's philosophy more than serve it.
