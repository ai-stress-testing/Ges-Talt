# Workflow Audit — post-conversion (2026-07-17)

State at audit time: 67 agents / 14 teams (sonnet 58, opus 5, haiku 4).
All five opus roles are read-only (`logician`, `code-reviewer`,
`academic/statistician`, `security/architect`, `platform/software-architect`)
— the "reasoning depth, not blast radius" invariant holds roster-wide and
is now machine-checked by `scripts/build_index.py`. Ponytail method is
baked into all 26 implementer roles (identical ladder block + SPEC
criterion) and phrased per-role into 6 architecture/review roles;
`frontend/section-508-specialist` is deliberately exempt (accessibility
guardrail outranks laziness framing).

## The workflow as it stands

A request can flow end-to-end with a named owner at every step:

1. **Scope** — `pm/project-manager` decomposes into team-scoped tickets
   with acceptance criteria (`program-tracker`/`delivery-lead` above it
   for initiative/portfolio altitude).
2. **Design** — `design/*` for research/IA/system governance,
   `frontend/designer` for implementation-adjacent spec.
3. **Build** — the owning implementer role (frontend/backend/data/
   devops/ai/mobile/platform/networking), all ladder-bound.
4. **Static review** — `logicians/logician` (invariants/spec
   contradictions), `logicians/code-reviewer` (diff review, now including
   over-engineering as a finding class).
5. **Empirical verification** — `testing/*`, with `reality-checker` as
   the final gate re-verifying other agents' evidence.
6. **Security** — `security/appsec-engineer` in the SDLC,
   `senior-secops` as PR gate, `architect` at design time.
7. **Operate** — `devops/*` (deploy/SLO/cost), `security/incident-responder`
   for breaches.

Advisory bench (academic) consults across all steps without write access.

## Overlap watches (bounded today, worth a routing rule)

- **Accessibility, two owners**: `testing/accessibility-auditor` is
  audit-only; `frontend/section-508-specialist` audits *and* remediates
  and owns legal conformance (VPAT/ADA/508). Routing rule: empirical
  WCAG audit of a build → testing; remediation work and conformance
  documentation → frontend specialist. Drift risk if either grows.
- **Incidents, two flavors**: `security/incident-responder` (breach) vs
  `devops/sre` (availability). Fine while the distinction is "malicious
  vs broken," but a paged agent must pick one fast — worth one line in
  each SPEC eventually.
- **Three architects** (`platform/software-architect`,
  `backend/backend-architect`, `security/architect`): domains are
  disjoint on paper; watch that cross-cutting decisions (e.g. authN
  topology) don't get triple-owned.

## Gaps

### Structural (blocking the workflow from actually running)

1. **Dispatch: partially closed; QA verdict loop still open.** The
   spec-driven PM upgrade (opus `pm/project-manager` + CLAUDE.md +
   `docs/templates/issue-spec.md`) now covers assignment: every sub-issue
   carries an assignee, acceptance criteria, and a negative prompt.
   Still undefined: the verdict cycle — what a testing FAIL hands back
   to the implementer, how many retries before escalation. agency-agents'
   PASS/FAIL/escalation templates remain the source to port as a
   lightweight convention.
2. **Environments (the hands) still don't exist.** `environments/` is a
   stub; `networking/network-engineer`'s charter references configs that
   aren't there. MCP tunnels, egress allowlists, and proactive session
   deletion remain the Sprint1 priority — the brains now outnumber the
   hands 67 to 0.
3. **No CI on the roster.** `build_index.py` lints locally; nothing runs
   it on push. One small workflow closes it (agency-agents'
   `lint-agents.yml` is the pattern).

### Coverage (roles the mock-enterprise is missing)

4. **Release management** — mobile has a release engineer; web/backend
   don't. No owner for prod cutover, change approval, rollback decisions.
5. **Networking is a one-person team** — edge/CDN/load-balancing,
   service mesh, DNS ops are unowned subclasses the moment environments
   work starts.
6. **Analytics/BI** — `academic/statistician` reviews metrics but nobody
   *builds* the metrics pipelines/dashboards it would review.
7. **Data governance** — residency advice (geographer) and framework
   audits (compliance-auditor) exist, but no owner for data
   classification, retention, or deletion obligations.

### Critical-systems slots (for the next wave of hyper-specialized agents)

The natural insertion points, most already adjacent to existing roles:

- **Secrets & cryptography** — key management, rotation, envelope
  encryption; adjacent to `identity-access-engineer` + `cloud-security-architect`.
- **Disaster recovery / backup** — RPO/RTO ownership, restore drills;
  currently nobody's job. Pairs with a proper **database administrator**
  (operational: replication/backup) distinct from `database-optimizer`
  (tuning).
- **Distributed-systems correctness** — consensus, exactly-once,
  partition behavior; a strong candidate for the opus + read-only
  pattern, reviewing designs the way `logician` reviews logic.
- **Regulated-data handling** — PCI/PHI scoping beside
  `payments-billing-engineer` and `compliance-auditor`.
- **Capacity & performance engineering** — load modeling beyond
  `performance-benchmarker`'s measurement.

Per the repo's philosophy these should nest under existing teams (or a
`critical-systems/` team if they need a shared charter), each justifying
model + tools in its SPEC — the two established patterns to reach for are
opus/read-only for reasoning-bound review roles and sonnet/full-tools for
implementers.
