# OPSEC — 12. Collection (MITRE TA0009)

Source: issue #38 "Hoarding". Primary owner: `agents/security/threat-detection-engineer`.
Phase legend: prevent / detect / respond.

Before data can leave, an adversary first gathers it — pulling from local disks, shared
drives, cloud storage, email, clipboards, and repositories, or capturing it live off screens,
mics, cameras, and keyboards. OPSEC here narrows the aggregation surface (least privilege,
DLP, app control) and instruments the bulk-access and archiving behavior that hoarding data
can't avoid producing.

| Technique (ID) | Control | Owner | Phase |
|---|---|---|---|
| Adversary-in-the-Middle (T1557) | HTTPS/SSH + DNSSEC; monitor ARP poisoning/unauthorized DHCP | `agents/networking/network-engineer` | prevent |
| Archive Collected Data (T1560) | DLP inspects compressed/encrypted files; monitor archiving utilities (7zip/WinRAR) by non-admins | `agents/security/threat-detection-engineer` | detect |
| Audio Capture (T1123) | App allowlist vs mic access; audit/restrict peripherals via GPO | `agents/security/senior-secops` | prevent |
| Automated Collection (T1119) | UEBA for unusual file-access/aggregation; restrict scripting interpreters | `agents/security/threat-detection-engineer` | detect |
| Browser Session Hijacking (T1185) | Secure updated browsers + web filters; MFA on critical apps vs session reuse | `agents/security/identity-access-engineer` | prevent |
| Clipboard Data (T1115) | DLP vs processes accessing clipboard; app control | `agents/security/threat-detection-engineer` | detect |
| Data from Cloud Storage (T1530) | Conditional Access + MFA; monitor cloud audit logs for unusual downloads | `agents/security/identity-access-engineer` | prevent |
| Data from Configuration Repository (T1602) | RBAC on network-device config repos; monitor unexpected SNMP/config dumps | `agents/networking/network-engineer` | prevent |
| Data from Information Repositories (T1213) | Access controls + DLP for Confluence/SharePoint/code repos; audit external sharing links | `agents/legal/privacy-engineer` | prevent |
| Data from Local System (T1005) | Least privilege on files; EDR monitors bulk copy/read | `agents/security/senior-secops` | prevent |
| Data from Network Shared Drive (T1039) | Restrict shares by need; segment; monitor unusual access | `agents/networking/network-engineer` | prevent |
| Data from Removable Media (T1025) | Block/audit USB; DLP vs copying to external devices | `agents/security/senior-secops` | prevent |
| Data Staged (T1074) | Monitor large temp archives in %TEMP% (EDR); hunt batch/bash copy-to-central scripts | `agents/security/threat-detection-engineer` | detect |
| Email Collection (T1114) | MFA; monitor suspicious inbox rules (external forwarding); restrict legacy protocols | `agents/security/identity-access-engineer` | prevent |
| Input Capture (T1056) | Endpoint detection for keyloggers/credential-hooking APIs; app control; user training | `agents/security/threat-detection-engineer` | detect |
| Screen Capture (T1113) | EDR alerts on screenshot utilities by unauthorized processes; app allowlist | `agents/security/threat-detection-engineer` | detect |
| Video Capture (T1125) | HW/SW inventory; restrict camera via privacy settings; monitor camera access | `agents/legal/privacy-engineer` | prevent |
