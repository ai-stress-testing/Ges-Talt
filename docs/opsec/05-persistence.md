# OPSEC — 05. Persistence (MITRE TA0003)

Source: issue #31 "Cessation". Primary owner: `agents/security/threat-detection-engineer` +
`agents/security/incident-responder`. Phase legend: prevent / detect / respond.

An adversary who has landed a foothold wants that foothold to survive reboots, credential
rotations, and cleanup — new accounts, autostart hooks, scheduled jobs, and rewritten boot
components that all resurrect access after the original entry point is closed. OPSEC here
denies durability: harden every mechanism that can be re-entered automatically, and instrument
the rest so a resurrection attempt is caught the moment it's planted, not the next time it fires.

| Technique (ID) | Control | Owner | Phase |
|---|---|---|---|
| Account Manipulation (T1098) | PAM w/ automated credential rotation; monitor anomalous privilege changes/multiple resets via SIEM | `agents/security/identity-access-engineer` | prevent |
| BITS Jobs (T1197) | Disable BITS for untrusted apps; monitor new BITS jobs via EDR | `agents/security/senior-secops` | prevent |
| Boot/Logon Autostart Execution (T1547) | Autoruns audit of Run keys/Startup; AppLocker | `agents/security/senior-secops` | prevent |
| Boot/Logon Initialization Scripts (T1037) | Audit script paths (UserInitMprLogonScript, /etc/rc.local); restrict write perms | `agents/security/senior-secops` | prevent |
| Cloud Application Integration (T1671) | Strict OAuth app consent; audit third-party app permissions | `agents/security/cloud-security-architect` | prevent |
| Compromise Host Software Binary (T1554) | File integrity monitoring; verify signatures on critical binaries | `agents/security/threat-detection-engineer` | detect |
| Create Account (T1136) | Audit-log new account creation; automated approval workflow | `agents/security/identity-access-engineer` | detect |
| Create or Modify System Process (T1543) | Monitor new service/daemon installs; restrict service creation to admins | `agents/security/threat-detection-engineer` | detect |
| Event Triggered Execution (T1546) | Disable unnecessary WMI event subscriptions; monitor IFEO/AppInit_DLLs; audit udev rules | `agents/security/threat-detection-engineer` | detect |
| Exclusive Control (T1668) | EDR to detect/terminate other threat actor activity; isolate hosts | `agents/security/incident-responder` | respond |
| External Remote Services (T1133) | MFA + Conditional Access for VPN/Citrix/RDP | `agents/security/identity-access-engineer` | prevent |
| Implant Internal Image (T1525) | Harden CI/CD; scan container images for malware; approved base images only | `agents/ci/containerization-engineer` | prevent |
| Modify Authentication Process (T1556) | Credential Guard; monitor LSASS for unauthorized DLLs; audit PAM configs | `agents/security/identity-access-engineer` | prevent |
| Modify Registry (T1112) | Audit critical Registry keys; EDR to block unauthorized writes | `agents/security/threat-detection-engineer` | detect |
| Office Application Startup (T1137) | Disable Office macros by default; ASR rules; monitor Outlook rules | `agents/security/senior-secops` | prevent |
| Power Settings (T1653) | Group Policy to prevent disabling sleep/hibernation | `agents/security/senior-secops` | prevent |
| Pre-OS Boot (T1542) | Secure Boot, TPM, Measured Boot | `agents/security/cloud-security-architect` | prevent |
| Scheduled Task/Job (T1053) | Monitor schtasks/cron creation; restrict who can create | `agents/security/threat-detection-engineer` | detect |
| Server Software Component (T1505) | WAF to detect web shells; restrict write to web dirs; patch | `agents/networking/network-engineer` | detect |
| Software Extensions (T1176) | Approved extension list; official managed stores only | `agents/security/senior-secops` | prevent |
| Traffic Signaling (T1205) | Host firewalls block inbound by default; monitor port-knocking | `agents/networking/network-engineer` | prevent |
| Valid Accounts (T1078) | MFA everywhere; UEBA for compromised accounts; JIT admin access | `agents/security/identity-access-engineer` | prevent |
