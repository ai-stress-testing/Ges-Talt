# OPSEC — 06. Privilege Escalation (MITRE TA0004)

Source: issue #32 "Privilege Controls". Primary owner: `agents/security/cloud-security-architect` +
`agents/security/identity-access-engineer`. Phase legend: prevent / detect / respond.

An adversary who has landed at low privilege wants root/SYSTEM/domain-admin without tripping an
alert — abusing elevation mechanisms, injecting into privileged processes, or riding a
misconfigured policy or container escape up the trust chain. OPSEC here denies the climb: keep
elevation paths locked to least privilege and audited, and instrument the mechanisms attackers
actually escalate through so an unauthorized jump is caught before it lands.

| Technique (ID) | Control | Owner | Phase |
|---|---|---|---|
| Abuse Elevation Control Mechanism (T1548) | Strict setuid/setgid policy + audit; app allowlisting | `agents/security/senior-secops` | prevent |
| Access Token Manipulation (T1134) | EDR for token duplication/impersonation; restrict admin shares; least-privilege accounts | `agents/security/threat-detection-engineer` | detect |
| Account Manipulation (T1098) | PAM w/ credential rotation; audit-log account/group changes | `agents/security/identity-access-engineer` | prevent |
| Boot/Logon Autostart Execution (T1547) | Harden Run keys/startup w/ ACLs; EDR for persistence | `agents/security/senior-secops` | prevent |
| Boot/Logon Initialization Scripts (T1037) | Restrict write on script dirs; code-signing; monitor logon-script mods | `agents/security/senior-secops` | prevent |
| Create or Modify System Process (T1543) | Audit service configs; EDR for new/modified services/agents/daemons | `agents/security/threat-detection-engineer` | detect |
| Domain/Tenant Policy Modification (T1484) | Limit who modifies GPO/trusts; change auditing; multi-person approval for critical policy | `agents/security/identity-access-engineer` | prevent |
| Escape to Host (T1611) | Non-root containers; restrict host path mounts; Pod Security Admission | `agents/cd/orchestration-engineer` | prevent |
| Event Triggered Execution (T1546) | Disable unnecessary WMI subscriptions; monitor registry/plist; integrity monitoring | `agents/security/threat-detection-engineer` | detect |
| Exploitation for Privilege Escalation (T1068) | Rigorous patching; exploit prevention (ASLR/DEP) | `agents/security/cloud-security-architect` | prevent |
| Process Injection (T1055) | Process Mitigation Policies; EDR w/ memory scanning | `agents/security/threat-detection-engineer` | detect |
| Scheduled Task/Job (T1053) | Audit tasks/cron; restrict creation; log task creation/execution | `agents/security/threat-detection-engineer` | detect |
| Valid Accounts (T1078) | MFA; regular account reviews; disable dormant accounts | `agents/security/identity-access-engineer` | prevent |
