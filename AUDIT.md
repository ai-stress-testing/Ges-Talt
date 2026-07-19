# Workflow Audit — post-conversion (2026-07-17)

State at audit time: 67 agents / 14 teams (sonnet 58, opus 5, haiku 4).
All five opus roles are read-only (`logician`, `code-reviewer`,
`academic/statistician`, `security/architect`, `logicians/software-architect`)
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
- **Three architects** (`logicians/software-architect`,
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
7. **Data governance** — closed by issue #1: `legal/data-protection-officer`
   now owns classification, retention, and DSR/deletion obligations, with
   `legal/privacy-engineer` verifying code reality ("true to code").

### Critical-systems slots — FILLED (GT-7)

Built and nested under existing teams, each justifying model + tools:

- **Secrets & cryptography** → `security/secrets-crypto-engineer` (KMS/HSM,
  key lifecycle, envelope encryption, crypto-agility).
- **Disaster recovery / backup** → `devops/disaster-recovery-engineer`
  (RPO/RTO, immutable backups, restore drills, ransomware resilience) +
  `data/database-administrator` (replication/backup/PITR, distinct from
  `database-optimizer`'s tuning).
- **Distributed-systems correctness** → `logicians/distributed-systems-verifier`
  (opus + read-only — consistency model, delivery semantics, idempotency,
  split-brain, producing the failing interleaving as counterexample).
- **Regulated-data handling** → `security/regulated-data-specialist`
  (PCI/PHI scoping + tokenization, distinct from `compliance-auditor`'s
  assessment and `legal/dpo`'s program).
- **Capacity & performance engineering** — deliberately NOT a new role:
  `devops/sre` already charters capacity engineering and
  `testing/performance-benchmarker` the measurement. Split would duplicate.

---

# Audit 2 — enterprise weaknesses & knowledge gaps (2026-07-17, post-merge to main)

State: 71 agents / 15 teams (sonnet 60, opus 7, haiku 4); legal team live;
spec-driven flow proven end-to-end on issue #1. Evidence gathered for this
audit: a referential-integrity scan of every `team/role` handoff mention
(0 broken references — the graph is consistent across seven different
authors) and a dependency count on the PM (94 file-mentions of
`pm/project-manager` across the roster).

## Weaknesses (structural / process)

1. **The PM is a chokepoint.** 94 references: acceptance sign-offs,
   access-widening approvals, spec ambiguity, and cross-team conflicts
   all route through one opus role with no delegation rule. Under
   parallel work this serializes everything. Fix is cheap: name which
   sign-offs delegate to `pm/delivery-lead` (portfolio) and
   `pm/program-tracker` (initiative), and let acceptance verification
   ride on `testing/reality-checker`'s verdict instead of PM re-review.
2. **The verdict loop is still prose.** What a testing FAIL hands back,
   the retry cap, and when escalation fires remain undefined — the last
   big hole in the build→verify cycle (carried from Audit 1).
3. **Every guardrail is convention, not mechanism.** The opus-Write
   exception, sprint-log discipline, negative prompts, and today's
   handoff integrity are all enforced by prose and good behavior.
   Nothing runs in CI (GT-8 open). Today's 0-broken-refs result is a
   snapshot, not a guarantee — the reference check belongs inside
   `build_index.py`.
4. **The org is documentation until it's wired to a runtime.** agents/
   specs aren't installed anywhere loadable (no `.claude/agents/`
   render). *Partly closed (GT-6):* `environments/` now carries real
   substrate — egress allowlists, MCP scoping, path-scoped writes,
   secrets policy, and a session-reaping spec (unarmed) — implementing
   threat-model C1–C5. Still declarative until a runtime enforces it, but
   no longer 0 hands.
5. **Two sources of truth for work.** `docs/backlog.md` GT-rows and
   GitHub issues overlap (GT-9 ↔ #1) with manual sync. Declare issues
   canonical and make the backlog a generated view, or accept drift.
6. **The roster has never been reviewed by its own reviewers.** Seven
   authors wrote 71 roles quickly; consistency held (see scan), but
   `logicians/logician` has never audited the charters for overlap or
   contradiction the way it would audit any other spec.
7. **No threat model for the agent org itself.** The security team
   points at product code; nobody owns prompt-injection, tool-misuse,
   or data-exfiltration risk *of the agent system* — acute before
   environments/ adds MCP tunnels and egress config. Natural first
   ticket for `security/architect` (read-only, already reasoning-tier).

## Knowledge gaps (questions the enterprise can't currently answer)

Carried from Audit 1, still open: release management for web/backend;
networking depth (CDN/edge, service mesh, DNS ops); analytics/BI;
the critical-systems wave (secrets/crypto, DR/backup + DBA, distributed
correctness, regulated data, capacity) — queued by the owner.

New:

8. **AI evaluation & safety.** The ai team builds (`ai-engineer`,
   `prompt-engineer`, `multi-agent-systems-architect`) but nobody
   evaluates: no LLM-eval / model-QA / red-teaming role, and the testing
   team is classic software QA. For an agent-heavy org this is the
   sharpest gap on the board.
9. **Supply-chain security.** `appsec-engineer` wires SCA scanning, but
   SBOM, dependency provenance, and third-party/vendor risk have no
   owner (`testing/tool-evaluator` only evaluates QA tooling).
10. **Operational readiness.** SLOs (`devops/sre`) and breach response
    (`security/incident-responder`) exist, but there's no on-call/paging
    definition and no decision rule for routing an ambiguous page
    (broken vs. malicious) — the Audit 1 overlap watch is now a gap
    because both roles are live.
11. **Support intake.** No role owns user-reported defects → triage into
    the PM flow; `design/ux-researcher` covers research, not tickets.

## Recommended order (laziest sufficient fix first)

1. Fold the handoff-reference check into `build_index.py` and stand up
   the GT-8 CI workflow — turns today's manual honesty into enforcement.
2. Write the verdict-loop convention (PASS/FAIL handback, retry cap,
   escalation) — one doc closes weakness 2 and half of weakness 1.
3. Declare GitHub issues canonical; backlog becomes a generated view.
4. Add `ai/model-evaluator` (gap 8) and cut the agent-org threat model
   ticket to `security/architect` (weakness 7) before environments work
   begins.
5. Then GT-6 (environments) and the owner's critical-systems wave (GT-7).
