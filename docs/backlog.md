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
