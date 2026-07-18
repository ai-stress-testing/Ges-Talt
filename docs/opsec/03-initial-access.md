# OPSEC — 03. Initial Access (MITRE TA0001)

Source: issue #24 "Initial Lock" · Primary owner: `agents/security/appsec-engineer` +
`agents/security/senior-secops` · MITRE TA0001

Initial Access is the attacker's first foothold — phishing, exploiting a public-facing
app, walking in on a trusted credential, a compromised vendor update, or a rogue device
on the wire. OPSEC denies the foothold by retiring each "first line of defense" folk
control (user training, patch cadence, perimeter trust) in favor of a control that holds
even when the classic line fails, backed by a playbook that assumes it will. Each row
below is one control or playbook action from one of the eleven mindset shifts in #24;
playbook actions are always `respond`, owned by the incident responder.

| Technique / Control area | Control | Owner | Phase |
|---|---|---|---|
| 1. User Awareness → Resilient by Design | Secure Email Gateway with attachment/URL sandboxing | `agents/security/senior-secops` | prevent |
| 1. User Awareness → Resilient by Design | Block internet-sourced Office macros by default | `agents/security/senior-secops` | prevent |
| 1. User Awareness → Resilient by Design | Enforce DMARC/SPF/DKIM on all sending domains | `agents/networking/network-engineer` | prevent |
| 1. User Awareness → Resilient by Design | Playbook: isolate the host, reset credentials, scan for lateral movement, non-blaming user coaching | `agents/security/incident-responder` | respond |
| 2. Patching → Rapid Recon & Response | Deploy WAF/RASP in front of public-facing apps | `agents/security/appsec-engineer` | prevent |
| 2. Patching → Rapid Recon & Response | Enforce strict input validation at every trust boundary | `agents/security/appsec-engineer` | prevent |
| 2. Patching → Rapid Recon & Response | Network segmentation to contain a compromised app tier | `agents/networking/network-engineer` | prevent |
| 2. Patching → Rapid Recon & Response | Maintain a current asset/attack-surface inventory | `agents/security/cloud-security-architect` | prevent |
| 2. Patching → Rapid Recon & Response | Playbook: emergency patch critical CVEs within 48h, trigger IR on exploit detection, drive root-cause analysis | `agents/security/incident-responder` | respond |
| 3. Trusted Access → Assume Compromise | Phishing-resistant MFA on all access paths | `agents/security/identity-access-engineer` | prevent |
| 3. Trusted Access → Assume Compromise | ZTNA in place of implicit network trust | `agents/security/cloud-security-architect` | prevent |
| 3. Trusted Access → Assume Compromise | Monitor for impossible-travel and abnormal login patterns | `agents/security/threat-detection-engineer` | detect |
| 3. Trusted Access → Assume Compromise | Playbook: disable suspicious sessions, force re-auth, investigate source IP/user-agent anomalies | `agents/security/incident-responder` | respond |
| 4. Password Protection → Identity Threat Detection | Privileged Access Management (PAM) for all admin credentials | `agents/security/identity-access-engineer` | prevent |
| 4. Password Protection → Identity Threat Detection | Conditional access policies on sign-in risk/device state | `agents/security/identity-access-engineer` | prevent |
| 4. Password Protection → Identity Threat Detection | User and Entity Behavior Analytics (UEBA) | `agents/security/threat-detection-engineer` | detect |
| 4. Password Protection → Identity Threat Detection | Playbook: rotate credentials, review privileged group membership, run identity forensics against Azure AD/Okta logs | `agents/security/incident-responder` | respond |
| 5. Procurement → Continuous Verification | Require SBOM from vendors for all delivered software | `agents/security/appsec-engineer` | prevent |
| 5. Procurement → Continuous Verification | Sign and verify all updates before install | `agents/devops/gitops-engineer` | prevent |
| 5. Procurement → Continuous Verification | Code integrity enforcement (WDAC) on endpoints | `agents/security/senior-secops` | prevent |
| 5. Procurement → Continuous Verification | Playbook: isolate, revert to known-good images, notify stakeholders, review vendor security posture/SLAs | `agents/security/incident-responder` | respond |
| 6. Block Malicious Sites → Browser Hardening | Remote browser isolation for high-risk browsing | `agents/security/senior-secops` | prevent |
| 6. Block Malicious Sites → Browser Hardening | Ad-blocking and anti-exploit hardening on all browsers | `agents/security/senior-secops` | prevent |
| 6. Block Malicious Sites → Browser Hardening | URL filtering by reputation at the perimeter | `agents/networking/network-engineer` | prevent |
| 6. Block Malicious Sites → Browser Hardening | Playbook: clear sessions, scan endpoint for persistence, block domain network-wide, update threat-intel feeds | `agents/security/incident-responder` | respond |
| 7. Third-Party Trust → Least Privilege for Partners | Separate guest/partner networks from corporate segments | `agents/networking/network-engineer` | prevent |
| 7. Third-Party Trust → Least Privilege for Partners | Federated identity with just-in-time (JIT) partner access | `agents/security/identity-access-engineer` | prevent |
| 7. Third-Party Trust → Least Privilege for Partners | Monitor partner account activity | `agents/security/threat-detection-engineer` | detect |
| 7. Third-Party Trust → Least Privilege for Partners | Playbook: revoke partner access, review partner actions, run a third-party risk assessment | `agents/security/incident-responder` | respond |
| 8. Block USB → Endpoint Detection & Control | Application allowlisting (AppLocker) on endpoints | `agents/security/senior-secops` | prevent |
| 8. Block USB → Endpoint Detection & Control | Disable AutoRun on removable media | `agents/security/senior-secops` | prevent |
| 8. Block USB → Endpoint Detection & Control | Monitor USB mount events and resulting process creation | `agents/security/threat-detection-engineer` | detect |
| 8. Block USB → Endpoint Detection & Control | Playbook: isolate the machine, inspect the media, revoke credentials used on the host, review physical security | `agents/security/incident-responder` | respond |
| 9. Physical Security → Device Attestation | Network Access Control (NAC) device-posture checks | `agents/networking/network-engineer` | prevent |
| 9. Physical Security → Device Attestation | Monitor for unknown MAC addresses/device types on the network | `agents/security/threat-detection-engineer` | detect |
| 9. Physical Security → Device Attestation | Restrict unused physical network ports | `agents/networking/network-engineer` | prevent |
| 9. Physical Security → Device Attestation | Playbook: locate/remove the rogue device, block its MAC, review footage/access logs, update inventory | `agents/security/incident-responder` | respond |
| 10. Web Filtering → Network Traffic Analysis | TLS inspection at the network perimeter | `agents/networking/network-engineer` | prevent |
| 10. Web Filtering → Network Traffic Analysis | Behavioral IDS/IPS on egress traffic | `agents/security/threat-detection-engineer` | detect |
| 10. Web Filtering → Network Traffic Analysis | Monitor for unusual web-traffic data patterns | `agents/security/threat-detection-engineer` | detect |
| 10. Web Filtering → Network Traffic Analysis | Playbook: block the payload, trace the flow to compromised users, update proxy rules, run forensics | `agents/security/incident-responder` | respond |
| 11. Perimeter Trust → Zero Trust Wireless | WPA3-Enterprise on all corporate wireless | `agents/networking/network-engineer` | prevent |
| 11. Perimeter Trust → Zero Trust Wireless | 802.1X port-based network access control | `agents/networking/network-engineer` | prevent |
| 11. Perimeter Trust → Zero Trust Wireless | Segment guest wifi from corporate wifi | `agents/networking/network-engineer` | prevent |
| 11. Perimeter Trust → Zero Trust Wireless | Monitor for rogue access points | `agents/security/threat-detection-engineer` | detect |
| 11. Perimeter Trust → Zero Trust Wireless | Playbook: deauth suspicious clients, rotate wifi credentials, eliminate rogue APs, investigate exfiltration | `agents/security/incident-responder` | respond |
