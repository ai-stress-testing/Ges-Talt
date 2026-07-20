# 2026-07-20 — Split devops/ into CI + CD teams; add tool-agnostic DevSecOps roles

**Session/agent**: main session (orchestrator, direct).
**Issues touched**: GT-49 (backlog). No GitHub issue cut — owner-directed model.

```
run-id: 2026-07-20-ci-cd-split
prompt: "Upgrade devops into 2 teams (CI + CD); agents not fixed to a library/service; map the 6-stage DevSecOps pipeline; explain enterprise-production value."
agents: main session only (no subagents spawned — structural migration + role authoring done direct; no measured token cost to ledger)
specs: agents/ci/README.md, agents/cd/README.md (team charters w/ stage map)
verdicts: lints — build_index PASS (95 agents, 15 teams), verify_comms PASS, credit PASS, audit_skills PASS
commits: (see push)
```

## Done
- Dissolved `agents/devops/`; every role migrated by `git mv` (history
  preserved) into two new teams split by pipeline half:
  - **CI = "make a trustworthy artifact"** (stages 1–4): pipeline-engineer
    (was devops-automator, reframed), containerization-engineer, +4 new.
  - **CD = "safely deliver and operate"** (stages 5–6): gitops-engineer,
    release-engineer, sre, disaster-recovery-engineer, finops-engineer,
    lifecycle-manager, orchestration-engineer (was kubernetes-engineer,
    reframed), + runtime-security-engineer (new).
- Reframed two roles to be **tool-agnostic** (own the function, tools are
  instances): `devops-automator → ci/pipeline-engineer` (the pipeline as
  code; Jenkins/GHA/GitLab CI are instances) and `kubernetes-engineer →
  cd/orchestration-engineer` (scheduling+health-gating; K8s/Nomad/ECS).
- Authored **5 new tool-agnostic DevSecOps pipeline-function roles**:
  `ci/quality-gate-engineer` (pre-commit/unit/lint/coverage gates),
  `ci/code-security-analyst` (SAST + secret detection + IaC scanning),
  `ci/supply-chain-engineer` (SCA + SBOM + signing + provenance),
  `ci/dynamic-security-tester` (DAST), `cd/runtime-security-engineer`
  (CIS benchmarking + deployed-image CVE rescan + runtime detection +
  CVE→SBOM→remediation-PR loop).
- Rewrote all `devops/<role>` cross-references across agents/, docs/opsec/,
  docs/enterprise.md, environments/ to the new `ci/`|`cd/` paths; fixed
  frontmatter `name:`/`Team:`; split the `devops` egress row in
  network-policy into `ci` (scan feeds) and `cd` (control-plane) rows.
- Regenerated INDEX (95 agents, 15 teams), refreshed tools-baseline
  intentionally, all four lints exit 0.

## Decisions
- **Team boundary = pipeline half, not tool.** CI ends at the signed,
  attested artifact; CD begins there. This is why SBOM+signing live in CI
  (they describe the artifact) but CVE-rescan lives in CD (it re-judges the
  running artifact over time).
- **CI/CD owns the *gate*; security owns the *standard*.** The new security
  roles wire scanners as blocking gates and triage output; they defer the
  security standard and deep manual review to `security/appsec-engineer` /
  `senior-secops`, and route key material to `secrets-crypto-engineer`.
  This keeps "shift-left" from duplicating the security team.
- **DAST (`ci/dynamic-security-tester`) ≠ functional E2E
  (`testing/test-automation-engineer`) ≠ manual pentest
  (`security/penetration-tester`).** Three distinct owners, referenced in
  each other's handoffs.
- **Historical records left untouched**: `docs/agent-ledger.jsonl`,
  `agents/COMMS.md`'s validated example (cites `devops/devops-automator` @
  70,042 — must still match the ledger row), `selection-weights.json`
  (regenerated from the ledger, so keyed on historical role names), and the
  `done` backlog rows. Rewriting them would break `verify_comms` and
  falsify the run history.
- **No ledger rows appended.** This was orchestrator-direct work with no
  measured subagent token cost; fabricating a cost would violate the
  ledger's integrity (observer-measured only).

## Blocked / carried
- New sprint window `sprint-7-26-20-27` was auto-scaffolded (today 07-20 is
  past the prior window's 07-19 end). This entry opens it.
- Carried, owner-gated: arm the session reaper; GT-43 hard-verifier registry
  (now assigned security team + `ci/pipeline-engineer`).
