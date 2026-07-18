# OPSEC — 02. Resource Development (MITRE TA0042)

Source issue #23 "Resource Perimeter" · owning roles: `security/threat-intelligence-analyst` + `networking/network-engineer` (supporting: `security/threat-detection-engineer`, `security/identity-access-engineer`) · applied at design time (`security/architect` review) and PR gate (`security/senior-secops`).

Resource Development is the attacker's staging phase — acquiring or compromising infrastructure, accounts, and capabilities they'll later launch an attack from (domains, servers, botnets, certificates, malware, stolen accounts). OPSEC denies this by making the org's own perimeter and identity/DNS estate resistant to being acquired, spoofed, or piggybacked on, and by burning attacker-controlled staging infrastructure through continuous threat-intel correlation before it's ever used. Grouped below by MITRE sub-technique family, in the order the source technique list presented them.

## Acquire Access (T1650)

| Technique / Control area | Control | Owner | Phase |
|---|---|---|---|
| T1650 Assume Breach | Continuous auth & risk-based conditional access | `security/identity-access-engineer` | prevent |

## Acquire Infrastructure (T1583)

| Technique / Control area | Control | Owner | Phase |
|---|---|---|---|
| T1583.001 Domains | DNS filtering & reputation scoring | `networking/network-engineer` | prevent |
| T1583.002 DNS Server | Inspect all DNS traffic, block tunneling | `networking/network-engineer` | prevent |
| T1583.003 Virtual Private Server | Allowlist approved cloud IP ranges | `networking/network-engineer` | prevent |
| T1583.004 Server | Geofencing & IP reputation blocks | `networking/network-engineer` | prevent |
| T1583.005 Botnet | Rate limiting & DDoS mitigation | `networking/network-engineer` | prevent |
| T1583.006 Web Services | Inspect payloads/frequency to any web service | `security/threat-detection-engineer` | detect |
| T1583.007 Serverless | Correlate serverless invocations with business workflows | `security/threat-detection-engineer` | detect |
| T1583.008 Malvertising | Block ads/trackers at network level; browser isolation | `networking/network-engineer` | prevent |

## Compromise Accounts (T1586)

| Technique / Control area | Control | Owner | Phase |
|---|---|---|---|
| T1586.002 Email Accounts | Alert on inbox rule changes, forwarding, suspicious OAuth grants | `security/threat-detection-engineer` | detect |
| T1586.003 Cloud Accounts | Monitor all API calls for anomalous patterns, esp. key creation | `security/threat-detection-engineer` | detect |

## Compromise Infrastructure (T1584)

| Technique / Control area | Control | Owner | Phase |
|---|---|---|---|
| T1584.001 Domains | Enforce DNSSEC, registry locks, WHOIS change alerts | `networking/network-engineer` | prevent |
| T1584.002 DNS Server | Restrict zone transfers; validate DNSSEC on resolvers | `networking/network-engineer` | prevent |
| T1584.003/.004 Virtual Private Server / Server | Asset inventory & auto-remediation for untagged resources | `security/threat-detection-engineer` | detect |
| T1584.005 Botnet | Micro-segmentation to contain compromised hosts | `networking/network-engineer` | respond |
| T1584.006 Web Services | Rotate tokens frequently; OAuth scope reviews | `security/identity-access-engineer` | prevent |
| T1584.007 Serverless | Detect new function deployments & unusual invocation patterns | `security/threat-detection-engineer` | detect |
| T1584.008 Network Devices | Monitor config hashes; require MFA for admin sessions | `security/identity-access-engineer` | prevent |

## Develop Capabilities (T1587)

| Technique / Control area | Control | Owner | Phase |
|---|---|---|---|
| T1587.001 Malware | EDR behavioral rules & YARA hunting | `security/threat-detection-engineer` | detect |
| T1587.002 Code Signing Certificates | Block self-signed code; enforce trusted PKI signing | `security/identity-access-engineer` | prevent |
| T1587.003 Digital Certificates | Decrypt/inspect SSL; monitor Certificate Transparency logs | `networking/network-engineer` | detect |
| T1587.004 Exploits | Prioritize CISA KEV patching; enforce ASLR/DEP | `security/threat-intelligence-analyst` | prevent |

## Establish Accounts (T1585)

| Technique / Control area | Control | Owner | Phase |
|---|---|---|---|
| T1585.001 Social Media Accounts | Proactively register brand variants; account creation policies | `security/threat-intelligence-analyst` | prevent |
| T1585.002 Email Accounts | Enforce DMARC p=reject; monitor external email reports | `networking/network-engineer` | prevent |
| T1585.003 Cloud Accounts | Alert on trial account creation; require business justification | `security/identity-access-engineer` | detect |

## Financial / Sensitive-Data Request Validation (T1683)

| Technique / Control area | Control | Owner | Phase |
|---|---|---|---|
| T1683.001/.002 Out-of-band request validation | Validate out-of-band any request involving funds or sensitive data | `security/identity-access-engineer` | prevent |

## Obtain Capabilities (T1588)

| Technique / Control area | Control | Owner | Phase |
|---|---|---|---|
| T1588.001-.006 Malware/tools/vulnerabilities/exploits/certificates/vehicles | Correlate threat intel with CISA KEV and your vuln scanner | `security/threat-intelligence-analyst` | detect |
| T1588.007 Artificial Intelligence | Deploy AI-based detectors; enforce human review for high-risk changes | `security/threat-detection-engineer` | prevent |

## Stage Capabilities (T1608)

| Technique / Control area | Control | Owner | Phase |
|---|---|---|---|
| T1608.001/.002 Upload Malware / Upload Tool | Sandbox inbound files; alert on execution of newly written files | `security/threat-detection-engineer` | detect |
| T1608.003 Install Digital Certificate | Require change approval for new server certs | `security/identity-access-engineer` | prevent |
| T1608.004 Drive-by Target | Enforce web isolation; block unnecessary plugins | `networking/network-engineer` | prevent |
| T1608.005 Link Target | Rewrite/inspect every URL at click-time with sandboxing | `networking/network-engineer` | prevent |
