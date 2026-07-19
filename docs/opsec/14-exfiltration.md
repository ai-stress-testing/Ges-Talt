# OPSEC — 14. Exfiltration (MITRE TA0010)

Source: issue #40 "Stagnant" · Owner: networking/network-engineer + legal/privacy-engineer · Phase mix: prevent/detect

Exfiltration covers the techniques adversaries use to move stolen data out of
the environment, whether through automated bulk transfer, protocol abuse, or
alternate physical/network mediums. Controls here lean on network egress
visibility and data-handling policy working together, since neither alone
catches every path data can leave by.

| Technique (ID) | Control | Owner | Phase |
|---|---|---|---|
| Automated Exfiltration (T1020) | DLP to monitor/block large automated outbound transfers; alert on anomalous bulk movement from critical servers | security/threat-detection-engineer | detect |
| Data Transfer Size Limits (T1030) | Network rules flag repeated small/chunked transfers; behavioral analytics on fixed-small-size patterns | networking/network-engineer | detect |
| Exfiltration Over Alternative Protocol (T1048) | Firewall blocks unauthorized protocols; DPI for tunneling over non-standard ports; monitor encrypted traffic to unexpected IPs | networking/network-engineer | prevent |
| Exfiltration Over C2 Channel (T1041) | Monitor C2 for large volumes/abnormal base64; egress filtering to inspect outbound C2 | security/threat-detection-engineer | detect |
| Exfiltration Over Other Network Medium (T1011) | WIDS for unauthorized Wi-Fi/Bluetooth/cellular; endpoint policies disable unused radios | networking/network-engineer | prevent |
| Exfiltration Over Physical Medium (T1052) | Block write to removable media for non-essential users; DLP scans/logs files copied to physical devices | security/senior-secops | prevent |
| Exfiltration Over Web Service (T1567) | Allowlist approved cloud services; CASB inspects uploads; monitor API calls to code repos/paste sites | legal/privacy-engineer | detect |
| Scheduled Transfer (T1029) | Baselines flag transfers outside business hours or at suspicious intervals; alert on scheduled jobs moving sensitive data | security/threat-detection-engineer | detect |
| Transfer Data to Cloud Account (T1537) | Restrict cloud identity perms vs cross-account copies; audit cloud logs for transfers to external accounts | security/cloud-security-architect | prevent |
