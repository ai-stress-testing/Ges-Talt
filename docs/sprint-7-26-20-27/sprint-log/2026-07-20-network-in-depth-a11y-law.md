# 2026-07-20 — Network-in-depth (#54) + accessibility-law counsel (#52)

**Session/agent**: main session (orchestrator, direct).
**Issues touched**: #52, #54 (GitHub); GT-52, GT-54 (backlog).

```
run-id: 2026-07-20-network-in-depth-a11y-law
prompt: "Take care of issues 52 and 54; take special care of 54 (network in depth, ensure no overlap with devops/ci-cd)."
agents: main session only (role authoring, direct; no measured subagent token cost to ledger)
specs: 5 new roles (agent.md + SPEC.md) + team-README/ORCHESTRATION wiring
verdicts: build_index PASS (100 agents, 15 teams), verify.py 10/10 PASS, verify_comms/credit/audit_skills all exit 0
commits: (see push)
```

## Done
- **#52 — `legal/accessibility-counsel`** (sonnet, Read/Grep/Glob/Write, no
  Edit/Bash per legal-team rule). Fills the gap the existing coverage left:
  `testing/accessibility-auditor` does the empirical WCAG/AT audit and
  `frontend/section-508-specialist` does ARIA/remediation/VPAT, but nobody
  owned the *cross-jurisdiction legal obligation*. This role maps the binding
  regimes (ADA Title III, Section 508, ADA Title II, EN 301 549, European
  Accessibility Act, AODA, UK Equality Act), sets the legally-required WCAG
  level + deadline, reads VPAT/ACR liability, and tracks exposure in the risk
  register — then hands the doing to testing + frontend. Legal README boundary
  note updated from "legal tracks exposure" to name the dedicated role.
- **#54 — network in depth**, four tool-agnostic roles, deliberately split so
  none overlaps `ci`/`cd` (application/cloud pipelines) or existing
  networking/security roles:
  - `networking/network-automation-engineer` — the device fleet as code:
    declarative config, linting (weak SNMP strings, over-broad ACLs), static
    intent validation, rehearsal in a virtual topology twin (GNS3/CML/cEOS)
    with ping/traceroute. Instances: Ansible/Terraform/Nornir, ansible-lint/
    Batfish, GNS3/Cisco CML/Arista cEOS.
  - `networking/network-reliability-engineer` — safe delivery + failsafe:
    commit-confirm/auto-rollback, the dead-man switch, out-of-band (OOB)
    management, self-healing, health-gated staged rollout. Answers "how do I
    reach the router after I break its config?" — the failure mode app deploy
    doesn't have.
  - `security/ids-ips-architect` (advisory) — IDPS architecture per NIST SP
    800-94: the inline (IPS) vs passive (IDS) placement axis, sensor coverage,
    segregated OOB management network, FIPS 140-validated management crypto,
    dynamic-firewall/border enforcement.
  - `security/network-detection-engineer` (implementer) — network detection
    content: the three NIST SP 800-94 methods (signature/anomaly/stateful
    protocol analysis), NetFlow/IPFIX behavior analytics (the "3am flow to
    Augusta"), wireless rogue-AP/evil-twin/WiFi-Pineapple/deauth detection,
    dynamic firewall/blacklist — feeding high-fidelity alerts to the SIEM.
- Wired both consultants (`ids-ips-architect`, `accessibility-counsel`) into
  the ORCHESTRATION on-demand consultant list; refreshed tools-baseline,
  regenerated INDEX (95→100) + repo-map, updated enterprise.md count.

## Decisions
- **"2 architects, inline and passive" = one role, two modes.** The inline
  (IPS) and passive (IDS) deployments are architectures to choose between and
  combine, not two org roles — `ids-ips-architect` owns both as its central
  design axis, with the see/stop/fail-cost rationale documented per segment so
  it isn't re-litigated. (Reading the user's "2 architects" as one role
  avoids roster bloat; flagged here in case the intent was literally two.)
- **SIEM/SOC/ML stays with `threat-detection-engineer`.** The issue's "SIEM
  central intelligence with ML" and "SOC integration with 90% confidence" are
  the correlation layer the existing role already owns;
  `network-detection-engineer` produces the network-sensor alerts that feed
  it, and HIDS/endpoint detection also routes there. No new SIEM role.
- **No devops overlap.** Network infra has failure modes (lockout via the
  box you're configuring; you can't canary a routing change like a web
  deploy) that justify network-specific reliability separate from `cd/sre` and
  `cd/release-engineer`. Boundary notes are explicit in each SPEC.
- **The gate caught a real bug**: backticked `ci/cd` prose parsed as a
  `team/role` handoff (team `ci`, role `cd`) and both `build_index` and the
  new `handoff_refs_resolve` verifier flagged it — nice cross-check that the
  GT-43 registry works. Fixed to `` `ci`/`cd` ``.
- **No ledger rows** — orchestrator-direct work, no measured token cost.

## Blocked / carried
- Issue #53 not addressed this pass (user scoped to 52 + 54).
- The `reason`-method network verifiers implied by #54 (e.g. "assert no
  unmonitored path exists", "assert OOB is truly isolated") are natural
  additions to `scripts/verifiers/` once a target network topology exists.
