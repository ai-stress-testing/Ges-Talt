# OPSEC — 10. Discovery (MITRE TA0007)

Source: issue #36 "Discontinuity". Primary owner: `agents/security/threat-detection-engineer`.
Phase legend: prevent / detect / respond.

An adversary who has landed a foothold now maps the terrain — accounts, software, network
topology, cloud services, and the security tooling watching them — before deciding where to move
next. Most Discovery techniques are inherently noisy queries against normal admin surfaces, so
OPSEC here leans on restricting who can run them and instrumenting the ones that can't be
restricted away.

| Technique (ID) | Control | Owner | Phase |
|---|---|---|---|
| Account Discovery | Restrict/log account enumeration; monitor net user/Get-ADUser | `agents/security/identity-access-engineer` | detect |
| Application Window Discovery | Allowlisting; alert on EnumWindows APIs | `agents/security/threat-detection-engineer` | detect |
| Browser Information Discovery | Encrypt browser profile data; DLP on bulk credential/history export | `agents/security/senior-secops` | prevent |
| Cloud Infrastructure Discovery | Cloud anomaly detection on metadata-endpoint (IMDS) API calls | `agents/security/cloud-security-architect` | detect |
| Cloud Service Dashboard | MFA + session audit for consoles; IP allowlist | `agents/security/identity-access-engineer` | prevent |
| Cloud Service Discovery | IAM read-only limits on critical services; audit logs | `agents/security/cloud-security-architect` | prevent |
| Cloud Storage Object Discovery | Storage access logging; bucket policy denies anonymous listing | `agents/security/cloud-security-architect` | prevent |
| Container & Resource Discovery | RBAC on orchestration APIs; runtime detection of kubectl get probes | `agents/cd/orchestration-engineer` | detect |
| Debugger Evasion | Anti-debug checks; block debugging tools | `agents/security/threat-detection-engineer` | detect |
| Device Driver Discovery | Restrict driver query; audit driverquery///proc/modules | `agents/security/senior-secops` | detect |
| Domain Trust Discovery | Restrict nltest/LDAP trust enum to admins; monitor | `agents/security/identity-access-engineer` | detect |
| File & Directory Discovery | FIM; restrict directory listing on sensitive shares | `agents/security/senior-secops` | prevent |
| Group Policy Discovery | Strict ACLs on SYSVOL; monitor Get-GPO/gpresult | `agents/security/identity-access-engineer` | detect |
| Local Storage Discovery | Encrypt volumes; restrict disk mgmt APIs; log | `agents/security/senior-secops` | prevent |
| Log Enumeration | Centralized tamper-proof logging; alert on non-admin log access | `agents/security/threat-detection-engineer` | detect |
| Network Service Discovery | Host firewalls + port-scan detection; segment | `agents/networking/network-engineer` | prevent |
| Network Share Discovery | Harden SMB; restrict net view; monitor share enumeration | `agents/networking/network-engineer` | detect |
| Network Sniffing | 802.1X + dynamic ARP inspection; block promiscuous mode | `agents/networking/network-engineer` | prevent |
| Password Policy Discovery | Limit access to policy objects; fine-grained policies | `agents/security/identity-access-engineer` | prevent |
| Peripheral Device Discovery | Device control policies; monitor Get-PnpDevice | `agents/security/senior-secops` | detect |
| Permission Groups Discovery | PAM; audit group queries; restrict net localgroup | `agents/security/identity-access-engineer` | prevent |
| Process Discovery | Restrict tasklist/ps for non-admins | `agents/security/senior-secops` | prevent |
| Query Registry | Registry auditing on reg query; restrict sensitive keys | `agents/security/senior-secops` | detect |
| Remote System Discovery | Limit ICMP/NetBIOS; segment; monitor ping sweeps/net view | `agents/networking/network-engineer` | detect |
| Software Discovery | App control vs inventory tools; log wmic/system_profiler | `agents/security/senior-secops` | detect |
| Security Software Discovery | Obfuscate security process names; kernel-level protection | `agents/security/threat-detection-engineer` | prevent |
| Backup Software Discovery | Strong ACLs on backup config; alert on catalog/vault access | `agents/security/senior-secops` | detect |
| System Information Discovery | Restrict systeminfo/uname to admins | `agents/security/senior-secops` | prevent |
| System Location Discovery | VPN/proxy to obscure location; restrict geolocation APIs | `agents/networking/network-engineer` | prevent |
| System Network Configuration Discovery | Restrict ipconfig/ifconfig; monitor ARP/route enum | `agents/networking/network-engineer` | detect |
| System Network Connections Discovery | Firewall limits on netstat; monitor connection scanning | `agents/networking/network-engineer` | detect |
| System Owner/User Discovery | Restrict whoami/session queries; audit | `agents/security/identity-access-engineer` | detect |
| System Service Discovery | Restrict sc query/systemctl | `agents/security/senior-secops` | prevent |
| System Time Discovery | Trusted NTP; monitor time changes | `agents/security/threat-detection-engineer` | detect |
| Virtual Machine Discovery | Obscure hypervisor artifacts; monitor VM enum (esxcli) | `agents/cd/orchestration-engineer` | detect |
| Virtualization/Sandbox Evasion | Sandbox-detection-resistant analysis; monitor time-based checks | `agents/security/threat-detection-engineer` | detect |
