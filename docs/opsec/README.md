# OPSEC — security management

The security team's operating playbook and gate. Issue #21: **every major
output passes through OPSEC** — OPSEC is the closest consultation edge in
`agents/ORCHESTRATION.md`, so security constraints enter at spec time and
gate the output before it ships, not after.

OPSEC is not a new agent — it's the applied discipline of the existing
`agents/security/` roles plus `networking/`, organized against the MITRE
ATT&CK matrix. This directory is the knowledge; the roles are the appliers.

## The gate

Before a major output ships, the owning security role runs the OPSEC
checklist for the relevant tactic(s) as part of the verdict loop
(`agents/WORKFLOW.md`) — the security step is concretely "did this pass the
OPSEC checklist for the tactics it exposes." A control with no owner is not
a control; every row names one.

- **Design time** — `security/architect` runs the relevant checklists
  against the design (proximity edge #1).
- **PR gate** — `security/senior-secops` enforces the code/config controls.
- **Detection** — `security/threat-detection-engineer` builds the
  monitoring the checklists call for.
- **Response** — `security/incident-responder` owns the playbook actions.
- **Perimeter/network** — `networking/network-engineer` owns segmentation,
  egress, DNS, reverse-proxy controls.

## The MITRE matrix — complete

The full ATT&CK kill chain, in order. Issues #22–#33 delivered the first
seven tactics; #34–#41 complete the second half (issue #12's 15-class
scheme, splitting Defense Evasion from Defense Impairment).

| # | Tactic (MITRE) | Issue | Checklist | Primary owner |
|---|---|---|---|---|
| 01 | Reconnaissance (TA0043) | #22 Anti-RQN | [01-reconnaissance.md](01-reconnaissance.md) | threat-detection-engineer + networking |
| 02 | Resource Development (TA0042) | #23 Resource Perimeter | [02-resource-development.md](02-resource-development.md) | threat-intelligence-analyst + networking |
| 03 | Initial Access (TA0001) | #24 Initial Lock | [03-initial-access.md](03-initial-access.md) | appsec-engineer + senior-secops |
| 04 | Execution (TA0002) | #25 Hardening | [04-execution.md](04-execution.md) | senior-secops + ci/cd |
| 05 | Persistence (TA0003) | #31 Cessation | [05-persistence.md](05-persistence.md) | threat-detection-engineer + incident-responder |
| 06 | Privilege Escalation (TA0004) | #32 Privilege Controls | [06-privilege-escalation.md](06-privilege-escalation.md) | cloud-security-architect + identity-access-engineer |
| 07 | Defense Evasion (TA0005) | #33 ID | [07-defense-evasion.md](07-defense-evasion.md) | threat-detection-engineer |
| 08 | Defense Impairment (T1562) | #34 Defense | [08-defense-impairment.md](08-defense-impairment.md) | threat-detection-engineer + senior-secops |
| 09 | Credential Access (TA0006) | #35 Credential Fortification | [09-credential-access.md](09-credential-access.md) | identity-access-engineer + threat-detection-engineer |
| 10 | Discovery (TA0007) | #36 Discontinuity | [10-discovery.md](10-discovery.md) | threat-detection-engineer |
| 11 | Lateral Movement (TA0008) | #37 Lateral Barriers | [11-lateral-movement.md](11-lateral-movement.md) | identity-access-engineer + networking |
| 12 | Collection (TA0009) | #38 Hoarding | [12-collection.md](12-collection.md) | threat-detection-engineer |
| 13 | Command & Control (TA0011) | #39 Command & Control | [13-command-and-control.md](13-command-and-control.md) | networking + threat-detection-engineer |
| 14 | Exfiltration (TA0010) | #40 Stagnant | [14-exfiltration.md](14-exfiltration.md) | networking + legal/privacy-engineer |
| 15 | Impact (TA0040) | #41 Coloumb | [15-impact.md](15-impact.md) | incident-responder + cd/sre |

## Checklist format

Each tactic file carries the technique→control mappings from its source
issue, cleaned into one table: `Technique (ID) | Control | Owner | Phase`
(phase = prevent / detect / respond). Preserve the source's controls; the
value added is the owner and phase columns so a checklist is *runnable*,
not just a reading list.
