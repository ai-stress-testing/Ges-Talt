# OPSEC — 08. Defense Impairment (MITRE T1562)

Source: issue #34 "Defense". Primary owner: `agents/security/threat-detection-engineer` +
`agents/security/senior-secops`.
Phase legend: prevent / detect / respond.

An adversary who already has a foothold wants to blind the defenses watching them — disabling
firewalls and EDR, rewriting policy and registry state, weakening encryption, and tampering with
boot integrity — so that everything they do next goes unlogged and unnoticed. OPSEC here denies
that by locking privileged changes to security controls behind restricted, auditable workflows and
by instrumenting real-time change detection (GPO, registry, firewall, cloud config) that a tampering
adversary cannot avoid triggering.

| Technique (ID) | Control | Owner | Phase |
|---|---|---|---|
| Disable/Modify System Firewall (T1562.004) | Centralized firewall mgmt w/ change alerts; restrict admin | `agents/networking/network-engineer` | detect |
| Disable/Modify Tools (T1562.001) | EDR tamper protection + integrity monitoring of security processes | `agents/security/threat-detection-engineer` | prevent |
| Domain/Tenant Policy Modification (T1484) | PAW w/ JIT access; real-time GPO change audit | `agents/security/identity-access-engineer` | prevent |
| Downgrade Attack (T1562.010) | Reject old vulnerable versions; app allowlisting blocks known-bad builds | `agents/security/appsec-engineer` | prevent |
| Exploitation for Defense Impairment (T1211) | Rigorous patching; vuln scanners for security-software flaws | `agents/security/appsec-engineer` | prevent |
| File/Directory Permissions Modification (T1222) | Credential Guard; advanced audit on sensitive-file permission changes | `agents/security/senior-secops` | prevent |
| Modify Authentication Process (T1556) | MFA; monitor LSASS/PAM DLL injection & registry changes | `agents/security/identity-access-engineer` | prevent |
| Modify Cloud Compute Infrastructure (T1578) | IaC w/ drift detection; restrict create/delete/revert instance perms | `agents/security/cloud-security-architect` | detect |
| Modify Cloud Resource Hierarchy (T1666) | Least-privilege RBAC; audit hierarchy changes | `agents/security/cloud-security-architect` | prevent |
| Modify Registry (T1112) | Registry auditing; ASR rules block critical-key mods | `agents/security/threat-detection-engineer` | detect |
| Modify System Image (T1601) | Secure boot + firmware integrity; verify image hashes pre-deploy | `agents/devops/gitops-engineer` | prevent |
| Network Boundary Bridging (T1599) | Strict segmentation; monitor unauthorized NAT/routing changes | `agents/networking/network-engineer` | prevent |
| Plist File Modification (T1647) | FIM on macOS plists; endpoint alerts | `agents/security/threat-detection-engineer` | detect |
| Prevent Command History Logging (T1562.003) | Mandatory session logging shipped to remote SIEM | `agents/security/threat-detection-engineer` | detect |
| Rogue Domain Controller (T1207) | Monitor unauthorized DC registrations; AD replication audit | `agents/security/identity-access-engineer` | detect |
| Safe Mode Boot (T1562.009) | Password for safe mode; EDR boot-time protection | `agents/security/senior-secops` | prevent |
| Subvert Trust Controls (T1553) | App control (AppLocker); validate code-signing certs | `agents/security/appsec-engineer` | prevent |
| Weaken Encryption (T1600) | Mandatory TLS 1.3; audit device crypto configs | `agents/networking/network-engineer` | prevent |
