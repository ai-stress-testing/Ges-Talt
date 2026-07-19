# OPSEC — 13. Command and Control (MITRE TA0011)

Source: issue #39 "Command & Control". Primary owner: `agents/networking/network-engineer`
+ `agents/security/threat-detection-engineer`.
Phase legend: prevent / detect / respond.

Once inside, an adversary needs a channel back out — blending into normal application
traffic, tunneling through allowed protocols, rotating infrastructure, and hiding behind
encryption and encoding. OPSEC here narrows the egress surface (protocol/port binding,
segmentation, egress filtering) and instruments the network anomalies a live channel can't
avoid producing (entropy, DGA lookups, unusual handshakes, multi-hop correlation).

| Technique (ID) | Control | Owner | Phase |
|---|---|---|---|
| Application Layer Protocol (T1071) | DPI + TLS decryption on app-layer payloads; app whitelisting | `agents/networking/network-engineer` | prevent |
| Communication Through Removable Media (T1092) | Endpoint DLP scans removable media; EDR detects external-drive execution | `agents/security/senior-secops` | detect |
| Content Injection (T1659) | HTTPS inspection + web filtering; browser isolation | `agents/networking/network-engineer` | prevent |
| Data Encoding (T1132) | Network analytics for abnormal entropy/char distributions; flag repeated encoding | `agents/security/threat-detection-engineer` | detect |
| Data Obfuscation (T1001) | NGFW threat signatures; ML detection of steganographic anomalies | `agents/security/threat-detection-engineer` | detect |
| Dynamic Resolution (T1568) | DNS sinkholing + threat-intel feeds vs DGA/short-TTL domains | `agents/networking/network-engineer` | prevent |
| Encrypted Channel (T1573) | SSL/TLS inspection w/ cert validation; monitor unusual cipher suites/handshakes | `agents/networking/network-engineer` | detect |
| Fallback Channels (T1008) | IR plans block known C2 IPs/domains; failover-aware monitoring | `agents/security/incident-responder` | respond |
| Hide Infrastructure (T1665) | Passive DNS + netflow analysis; share indicators with ISACs | `agents/security/threat-detection-engineer` | detect |
| Ingress Tool Transfer (T1105) | EDR blocks untrusted executable downloads; app control | `agents/security/senior-secops` | prevent |
| Multi-Stage Channels (T1104) | Correlate network+host logs for multi-hop C2; honeypots | `agents/security/threat-detection-engineer` | detect |
| Non-Application Layer Protocol (T1095) | Block unnecessary protocols (ICMP echo) at firewalls; protocol analyzers | `agents/networking/network-engineer` | prevent |
| Non-Standard Port (T1571) | Strict port-to-service binding; segmentation | `agents/networking/network-engineer` | prevent |
| Protocol Tunneling (T1572) | DNS firewalls + decapsulation; restrict outbound SSH/RDP tunnels | `agents/networking/network-engineer` | prevent |
| Proxy (T1090) | Block known proxy IPs/CDN abuse; egress filtering to trusted proxies only | `agents/networking/network-engineer` | prevent |
| Remote Access Tools (T1219) | Approved-software list; monitor unauthorized RMM; restrict GitHub/OAuth tunnels via CASB | `agents/security/senior-secops` | prevent |
| Traffic Signaling (T1205) | Host IPS for sequential connection patterns; monitor socket filter installs | `agents/networking/network-engineer` | detect |
| Web Service (T1102) | URL filtering + cloud app security; threat-hunt abnormal API calls to known platforms | `agents/security/threat-detection-engineer` | detect |
