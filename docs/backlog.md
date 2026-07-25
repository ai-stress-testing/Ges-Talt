# Backlog

GitHub issues are the canonical tracker for work items; this table is a
summary view, not a second source of truth. Rows are added and kept in
sync by the spec-driven PM (`agents/pm/project-manager`), one row per
issue, and link out via the Issue column when a GitHub issue exists.
Status: todo / in-progress / blocked / done.

| ID | Item | Assignee (agent) | Sprint | Status | Issue |
|---|---|---|---|---|---|
| GT-1 | Convert agency-agents divisions into team roster | (six conversion subagents) | sprint-7-26-12-19 | done | — |
| GT-2 | Ponytail method pass across roster | (ponytail subagent) | sprint-7-26-12-19 | done | — |
| GT-3 | Agent index + roster lint | main session | sprint-7-26-12-19 | done | — |
| GT-4 | Docs convention, templates, init script | main session | sprint-7-26-12-19 | done | — |
| GT-5 | Spec-driven PM upgrade (opus, issues + negative prompts) | main session | sprint-7-26-12-19 | done | — |
| GT-6 | environments/ build-out: MCP tunnels, allowlists, session reaping | networking/network-engineer | sprint-7-26-12-19 | done | — |
| GT-7 | Hyper-specialized critical-systems agents | (owner) | sprint-7-26-12-19 | done | — |
| GT-8 | CI workflow running build_index.py lint | devops/devops-automator | sprint-7-26-12-19 | done | — |
| GT-9 | Legal team: privacy-engineer, DPO, product-counsel, general-counsel | main session (spec-driven flow, issue #1) | sprint-7-26-12-19 | done | [#1](https://github.com/ai-stress-testing/Ges-Talt/issues/1) |
| GT-10 | Verdict-loop convention (FAIL handback, retry cap, escalation) | pm/team-operations | sprint-7-26-12-19 | done | — |
| GT-11 | ai/model-evaluator role + agent-org threat model (environments/THREAT-MODEL.md; control C7 applied) | main session + security/architect | sprint-7-26-12-19 | done | — |
| GT-12 | Issues-canonical backlog + handoff-ref check in lint (auto-generated view deferred until manual sync actually drifts) | devops/devops-automator | sprint-7-26-12-19 | done | — |
| GT-13 | Lint: flag tool-set widening on roster diffs (threat-model C6) | devops/devops-automator + security/architect | sprint-7-26-12-19 | done | — |
| GT-14 | PM upgrades: token-distribution pressure + LEAD structuring | pm charters (sonnet subagent) | sprint-7-26-12-19 | done | [#14](https://github.com/ai-stress-testing/Ges-Talt/issues/14), [#20](https://github.com/ai-stress-testing/Ges-Talt/issues/20) |
| GT-15 | Logicians charter README + falsifier role | logicians (sonnet subagent) | sprint-7-26-12-19 | done | [#15](https://github.com/ai-stress-testing/Ges-Talt/issues/15), [#18](https://github.com/ai-stress-testing/Ges-Talt/issues/18) |
| GT-16 | devops/lifecycle-manager role | platform (sonnet subagent) | sprint-7-26-12-19 | done | [#17](https://github.com/ai-stress-testing/Ges-Talt/issues/17) |
| GT-17 | Enterprise-Doc: template, scaffold, seeded docs/enterprise.md | docs tooling (sonnet subagent) | sprint-7-26-12-19 | done | [#19](https://github.com/ai-stress-testing/Ges-Talt/issues/19) |
| GT-18 | Enterprise-enhancements triage (28 categories) | main session (sonnet subagent) | sprint-7-26-12-19 | done | [#16](https://github.com/ai-stress-testing/Ges-Talt/issues/16) |
| GT-19 | Token-cost sustainability tracking (from #16 triage) | devops/finops-engineer | sprint-7-26-12-19 | done | — |
| GT-20 | Blueprinting convention (from #16 triage) | design/ux-architect | (deferred) | todo | — |
| GT-21 | Agent comms convention: quoted attribution + code-verified tokens | main session | sprint-7-26-12-19 | done | — |
| GT-22 | devops/gitops-engineer role (git-as-truth, drift, rollback) | devops | sprint-7-26-12-19 | done | [#13](https://github.com/ai-stress-testing/Ges-Talt/issues/13) |
| GT-23 | Routines: convention + registry (brainstorm) — see docs/routines-ideas.md | (owner, brainstorming) | (next) | todo | — |
| GT-24 | devops/release-engineer: progressive delivery / release-gate (shift-left error-handling-off-prod) | devops | sprint-7-26-12-19 | done | — |
| GT-25 | Dissolve platform/: move 6 roles to security/logicians/frontend/academic/design/devops | main session | sprint-7-26-12-19 | done | — |
| GT-26 | devops/containerization-engineer + kubernetes-engineer (error-handling-off-prod) | devops | sprint-7-26-12-19 | done | — |
| GT-27 | Orchestration model (variation-interaction-selection, proximity, user journey) | main session | sprint-7-26-12-19 | done | [#26](https://github.com/ai-stress-testing/Ges-Talt/issues/26) |
| GT-28 | Agents close their own issues (verdict-loop terminal state) | main session | sprint-7-26-12-19 | done | [#28](https://github.com/ai-stress-testing/Ges-Talt/issues/28) |
| GT-29 | Feedforward→feedback: closed-loop discipline doc | main session | sprint-7-26-12-19 | done | [#29](https://github.com/ai-stress-testing/Ges-Talt/issues/29) |
| GT-30 | Rename mobile team → mx (multi-experience) | main session | sprint-7-26-12-19 | done | [#27](https://github.com/ai-stress-testing/Ges-Talt/issues/27) |
| GT-31 | Nous-Research-lens review of the MCP/orchestration | main session | sprint-7-26-12-19 | done | [#30](https://github.com/ai-stress-testing/Ges-Talt/issues/30) |
| GT-32 | Acting controller: selection-score per role from ledger (reward=pass−cost−retries) that the PM reads (from #30 sol.2) | ai/model-evaluator | sprint-7-26-12-19 | done | — |
| GT-33 | Model sovereignty: capability-tier (reason/build/cheap) + models.toml + open-model swap eval (from #30 sol.1) | ai/ai-engineer | sprint-7-26-12-19 | done | — |
| GT-34 | Grader independence: adversary grader resolves to a different model family; correlated-grader warning (sol.4) | logicians/falsifier | sprint-7-26-12-19 | done | — |
| GT-35 | Anti-grader-gaming: model-evaluator red-teams the grader on cadence with plants (sol.5) | ai/model-evaluator | sprint-7-26-12-19 | done | — |
| GT-36 | Mesh topology: peer handoff default, orchestrator only for arbitration; measure fan-through (sol.6) | main session | sprint-7-26-12-19 | done | — |
| GT-37 | Ephemeral-agent governance: declare frontmatter, tool-boundary check at spawn, log ephemeral:true (sol.8) | main session | sprint-7-26-12-19 | done | — |
| GT-38 | Run manifest: run-id + structured sprint-chat header for replayability (sol.10) | pm/team-operations | sprint-7-26-12-19 | done | — |
| GT-39 | Depth×economy joint optimum: L0 charter + on-demand L1 DEPTH.md + depth-trigger; exemplar-encoded; compounding memory (sol.9, marquee) | main session + design | sprint-7-26-12-19 | done | — |
| GT-40 | OPSEC framework (issue #21): gate + MITRE matrix hub, security team wiring | main session | sprint-7-26-12-19 | done | [#21](https://github.com/ai-stress-testing/Ges-Talt/issues/21) |
| GT-41 | OPSEC checklists, first 7 MITRE tactics (recon→defense-evasion) | 3 sonnet subagents | sprint-7-26-12-19 | done | #22–#25, #31–#33 |
| GT-42 | OPSEC checklists, second half (cred-access→impact) | security team | sprint-7-26-12-19 | done | [#12](https://github.com/ai-stress-testing/Ges-Talt/issues/12) |
| GT-43 | Hard-verifier registry: scripts/verifiers/ single-property machines gating the verdict loop (from hard-verifiers brainstorm) | security team + ci/pipeline-engineer | sprint-7-26-20-27 | done | — |
| GT-44 | Skills policy (#42) + 501-LoC audit lint (#43) | main session | sprint-7-26-12-19 | done | [#42](https://github.com/ai-stress-testing/Ges-Talt/issues/42), [#43](https://github.com/ai-stress-testing/Ges-Talt/issues/43) |
| GT-45 | Security spec-time consultants: rbac-abac, rls, pq-crypto, side-channel (#50 consultants) | 2 sonnet subagents | sprint-7-26-12-19 | done | #44, #45, #46, #48, #50 |
| GT-46 | security/red-team-critic (opus, read-only) + blue↔red pairing convention | sonnet subagent | sprint-7-26-12-19 | done | [#47](https://github.com/ai-stress-testing/Ges-Talt/issues/47) |
| GT-47 | logicians/agent-evaluator (group-theory) + docs/evals per-team convention | sonnet subagent | sprint-7-26-12-19 | done | [#49](https://github.com/ai-stress-testing/Ges-Talt/issues/49) |
| GT-48 | networking/nginx-specialist consultant (not devops) | sonnet subagent | sprint-7-26-12-19 | done | [#51](https://github.com/ai-stress-testing/Ges-Talt/issues/51) |
| GT-49 | Split `devops/` into `ci/` + `cd/` teams; migrate 9 roles; reframe pipeline-engineer + orchestration-engineer tool-agnostic; add 5 DevSecOps pipeline-function roles (quality-gate, code-security-analyst, supply-chain, dynamic-security-tester, runtime-security) | main session | sprint-7-26-20-27 | done | — |
| GT-50 | Branching + worktree convention (feature/fix/bug/mvp/plan taxonomy, worktree-per-task observability) + branch_taxonomy verifier | main session | sprint-7-26-20-27 | done | — |
| GT-51 | Token-economy repo index: scripts/build_repo_index.py → docs/repo-map.md (path→purpose nav map) + repo_map_fresh verifier | main session | sprint-7-26-20-27 | done | — |
| GT-52 | legal/accessibility-counsel: cross-jurisdiction accessibility-law obligation (ADA/508/EN 301 549/EAA/AODA), sets legally-required WCAG target, VPAT liability, exposure tracking — hands audit→testing, remediation→frontend | main session | sprint-7-26-20-27 | done | [#52](https://github.com/ai-stress-testing/Ges-Talt/issues/52) |
| GT-54 | Network-in-depth (tool-agnostic, non-overlapping with ci/cd): networking/network-automation-engineer + network-reliability-engineer (network-as-code, lab twin, commit-confirm/dead-man/OOB/self-heal); security/ids-ips-architect + network-detection-engineer (NIST SP 800-94 IDPS, inline/passive, NetFlow behavior, wireless rogue-AP, FIPS/OOB, feeds SIEM) | main session | sprint-7-26-20-27 | done | [#54](https://github.com/ai-stress-testing/Ges-Talt/issues/54) |
| GT-55 | Advanced analytics pipeline v1 (consent-gated device intelligence, fraud/bot): frontend/client-telemetry-engineer (stateless+stateful IDs, canvas/WebGL/audio fingerprint, sendBeacon/ECDH) + data/device-intelligence-engineer (ID resolution, IP/datacenter intelligence, ML fraud scoring). Guardrails: lawful-basis/consent-first, no evercookie/respawn, no 3rd-party tracking | main session | sprint-7-26-20-27 | done | [#55](https://github.com/ai-stress-testing/Ges-Talt/issues/55) |
| GT-57 | Security/OPSEC crypto normalization: security/e2ee-protocol-consultant — X3DH/PQXDH handshake (identity/signed/one-time prekeys), Double Ratchet (FS + post-compromise), Sesame multi-device, HKDF salt→PRK→OKM + zeroization, offline deniability; +DEPTH.md. Hands PQ leg→pq-crypto-consultant, impl→secrets-crypto-engineer | main session | sprint-7-26-20-27 | done | [#57](https://github.com/ai-stress-testing/Ges-Talt/issues/57) |
| GT-58 | Evolutionary architecture (MX + Data + fitness functions, issue #58 / Rahman MSR 2016): mx/feature-flag-engineer (toggle taxonomy, staged/cohort rollout, toggle-debt discipline) + data/evolutionary-data-engineer (expand-contract migrations, compatible contracts, experiment-data governance) + docs/fitness-functions.md (fitness functions = verifier-registry mechanism; software-architect owns design) | main session | sprint-7-26-20-27 | done | [#58](https://github.com/ai-stress-testing/Ges-Talt/issues/58) |
| GT-59 | EPIC: Make the roster executable, not decorative — install personas as subagents + verdict-loop as a real gate (diagnosis: framework was decorative; orchestrator wrote all code inline) | pm/project-manager | sprint-7-26-20-27 | done | [#59](https://github.com/ai-stress-testing/Ges-Talt/issues/59) |
| GT-60 | Install personas as subagents: scripts/build_personas.py → .claude/agents/ + personas_installed verifier | ci/pipeline-engineer | sprint-7-26-20-27 | done | [#60](https://github.com/ai-stress-testing/Ges-Talt/issues/60) |
| GT-61 | Trigger-oriented description frontmatter: convention + description_triggers lint + roster-wide rewrite | ai/multi-agent-systems-architect | sprint-7-26-20-27 | done | [#61](https://github.com/ai-stress-testing/Ges-Talt/issues/61) |
| GT-62 | CLAUDE.md routing directive overriding the don't-spawn default (delegation optional/cost-aware; review-gate non-negotiable) | pm/project-manager | sprint-7-26-20-27 | done | [#62](https://github.com/ai-stress-testing/Ges-Talt/issues/62) |
| GT-63 | SessionStart hook + .claude/settings.json injecting the role-routing reminder | ci/pipeline-engineer | sprint-7-26-20-27 | done | [#63](https://github.com/ai-stress-testing/Ges-Talt/issues/63) |
| GT-64 | Hard verifier verdict_recorded: a major output must record a consultation/verdict (run-manifest verdicts/COMMS) | security team + ci/pipeline-engineer | sprint-7-26-20-27 | done | [#64](https://github.com/ai-stress-testing/Ges-Talt/issues/64) |
| GT-65 | Real skills at .claude/skills/ (run-gate; scaffold-sprint) — procedure-only, honest YAGNI | ci/pipeline-engineer + pm/program-tracker | sprint-7-26-20-27 | done | [#65](https://github.com/ai-stress-testing/Ges-Talt/issues/65) |
| GT-66 | Verdict-loop as a real gate even when implementation stays inline (falsifier + consultation-proximity + COMMS, recorded) | pm/project-manager + logicians/falsifier | sprint-7-26-20-27 | done | [#66](https://github.com/ai-stress-testing/Ges-Talt/issues/66) |
| GT-67 | EPIC: Automate the mechanical ceremony — stop spending tokens where a script suffices (introspection) | ci/pipeline-engineer | sprint-7-26-20-27 | todo | [#67](https://github.com/ai-stress-testing/Ges-Talt/issues/67) |
| GT-68 | scripts/gate.py — one-command regenerate+lint+verify pipeline, failures-first, exit code (+ --check) | ci/pipeline-engineer | sprint-7-26-20-27 | todo | [#68](https://github.com/ai-stress-testing/Ges-Talt/issues/68) |
| GT-69 | scripts/extract_text.py — PDF/binary → text (pdftotext/pdfminer degrade, actionable missing-dep error) | data/data-engineer | sprint-7-26-20-27 | todo | [#69](https://github.com/ai-stress-testing/Ges-Talt/issues/69) |
| GT-70 | scripts/new_sprint_log.py — stamp dated sprint-log entry from template w/ run-manifest header prefilled | pm/program-tracker | sprint-7-26-20-27 | todo | [#70](https://github.com/ai-stress-testing/Ges-Talt/issues/70) |
| GT-71 | scripts/ship.py — push dev + fast-forward main with backoff, guarded (never force) | ci/pipeline-engineer | sprint-7-26-20-27 | todo | [#71](https://github.com/ai-stress-testing/Ges-Talt/issues/71) |
| GT-72 | scripts/backlog.py — add row / flip status in canonical table (lowest priority; content is prose) | pm/project-manager | sprint-7-26-20-27 | todo | [#72](https://github.com/ai-stress-testing/Ges-Talt/issues/72) |
| GT-73 | Hermes Local LM Studio Connector MVP (backend + UI + Docker Compose stack, `docker-hermes` repo) | backend/backend-dev, ci/containerization-engineer | sprint-7-26-20-27 | done | — |
| GT-74 | Sandboxed NousResearch Hermes Agent deployment (docker-compose wrapping the real `nousresearch/hermes-agent` image, LM Studio as provider; `docker-hermes` repo, branch `claude/nous-hermes-agent-sandbox`) — supersedes a discarded from-scratch reimplementation | main session + ai/ai-engineer, ci/containerization-engineer (discarded), logicians/falsifier x2, security/appsec-engineer x2 | sprint-7-26-20-27 | done | — |
