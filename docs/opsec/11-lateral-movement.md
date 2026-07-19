# OPSEC — 11. Lateral Movement (MITRE TA0008)

Source: issue #37 "Lateral Barriers". Primary owners: `agents/security/identity-access-engineer` +
`agents/networking/network-engineer`.
Phase legend: prevent / detect / respond.

Once inside, an adversary pivots from the beachhead toward the objective — riding legitimate
remote-access paths, stolen sessions, and trusted deployment tooling instead of noisy exploits.
OPSEC here narrows the paths a compromised identity can travel (segmentation, jump servers, PoLP)
and instruments the ones that can't be closed off (session auditing, file-transfer telemetry,
anomalous ticket detection).

| Technique (ID) | Control | Owner | Phase |
|---|---|---|---|
| Exploitation of Remote Services (T1210) | Patch RDP/SMB; app allowlisting; network IDS | `agents/security/senior-secops` | prevent |
| Internal Spearphishing (T1534) | Conditional access + UEBA on internal forwarding/mass messaging; awareness training | `agents/security/identity-access-engineer` | prevent |
| Lateral Tool Transfer (T1570) | App control vs execution from writable shares; monitor abnormal file transfer (Sysmon); limit outbound SMB | `agents/security/threat-detection-engineer` | detect |
| Remote Service Session Hijacking (T1563) | Session timeouts; uniquely sign sessions; restrict concurrent; NLA for RDP/SSH; monitor tscon.exe | `agents/security/identity-access-engineer` | detect |
| Remote Services (T1021) | PoLP + jump servers; JIT privileged access; audit remote logins (Event 4624) | `agents/security/identity-access-engineer` | prevent |
| Replication Through Removable Media (T1091) | Disable AutoRun; EDR blocks USB execution; device control whitelist | `agents/security/senior-secops` | prevent |
| Software Deployment Tools (T1072) | Dedicated admin accounts + MFA + segmentation for SCCM/Intune; restrict command execution | `agents/security/cloud-security-architect` | prevent |
| Taint Shared Content (T1080) | Scan shares for malicious scripts/macros; FIM; restrict write perms | `agents/security/senior-secops` | prevent |
| Use Alternate Authentication Material (T1550) | Kerberos armoring (FAST); disable NTLM where possible; Credential Guard; rotate service passwords; monitor anomalous tickets (Golden Ticket) | `agents/security/identity-access-engineer` | prevent |
