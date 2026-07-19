# OPSEC — 09. Credential Access (MITRE TA0006)

Source: issue #35 "Credential Fortification". Primary owner: `agents/security/identity-access-engineer` +
`agents/security/threat-detection-engineer`.
Phase legend: prevent / detect / respond.

An adversary wants to steal legitimate credentials, tokens, tickets, or session material so they can
authenticate as a real user instead of exploiting the target directly — the quietest path to
everything downstream. OPSEC denies this by hardening authentication itself (phishing-resistant MFA,
short-lived tokens, encrypted credential stores and transport) and by instrumenting the telemetry
that credential theft and misuse cannot avoid triggering (LSASS access, anomalous ticket issuance,
token/cookie replay).

| Technique (ID) | Control | Owner | Phase |
|---|---|---|---|
| Adversary-in-the-Middle (T1557) | HTTPS/SSH + segmentation w/ ARP/DHCP spoof detection | `agents/networking/network-engineer` | prevent |
| Brute Force (T1110) | Strong password policy, lockouts, MFA | `agents/security/identity-access-engineer` | prevent |
| Credentials from Password Stores (T1555) | Restrict admin access to keychains/browsers; strong master passwords; monitor access | `agents/security/identity-access-engineer` | prevent |
| Exploitation for Credential Access (T1212) | Patch mgmt + vuln scanning | `agents/security/appsec-engineer` | prevent |
| Forced Authentication (T1187) | Block external SMB auth; firewall outbound auth | `agents/networking/network-engineer` | prevent |
| Forge Web Credentials (T1606) | Short-lived tokens; strict cert validation; monitor anomalous token issuance/cookie replay | `agents/security/identity-access-engineer` | prevent |
| Input Capture (T1056) | EDR for keyloggers; app allowlisting; user training on fake prompts | `agents/security/threat-detection-engineer` | detect |
| Modify Authentication Process (T1556) | FIM on registry/system files; restrict DLL loading to signed | `agents/security/threat-detection-engineer` | detect |
| MFA Interception (T1111) | Phishing-resistant MFA (FIDO2/WebAuthn); monitor MFA enrollment/push | `agents/security/identity-access-engineer` | prevent |
| Network Sniffing (T1040) | Encrypt traffic (TLS/IPSEC); switch port security vs promiscuous mode | `agents/networking/network-engineer` | prevent |
| OS Credential Dumping (T1003) | Credential Guard; restrict admin; monitor LSASS access via EDR | `agents/security/senior-secops` | prevent |
| Steal Application Access Token (T1528) | Token binding; short lifetimes; monitor unusual token usage | `agents/security/appsec-engineer` | prevent |
| Steal/Forge Auth Certificates (T1649) | Cert transparency logs; monitor unauthorized cert requests; HSMs | `agents/security/cloud-security-architect` | detect |
| Steal/Forge Kerberos Tickets (T1558) | AES encryption; rotate KRBTGT; monitor anomalous ticket requests (Golden Ticket) | `agents/security/identity-access-engineer` | prevent |
| Steal Web Session Cookie (T1539) | HttpOnly/Secure flags; re-auth for sensitive transactions | `agents/security/appsec-engineer` | prevent |
| Unsecured Credentials (T1552) | No plaintext passwords in files/scripts; credential mgmt tools; scan repos for secrets | `agents/devops/gitops-engineer` | prevent |
| MFA Request Generation (T1621) | Number-matching/location-based MFA; alert on multiple denied requests | `agents/security/identity-access-engineer` | prevent |
