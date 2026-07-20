# OPSEC — 15. Impact (MITRE TA0040)

Source: issue #41 "Coloumb" · Owner: security/incident-responder + cd/sre · Phase mix: prevent/detect/respond

Impact covers techniques that manipulate, interrupt, or destroy systems and
data to disrupt availability or integrity — ransomware, wipes, DoS, defacement,
and financial theft. These controls sit at the end of the kill chain, so
recovery posture (immutable backups, restore drills, auto-restart) matters as
much as prevention.

| Technique (ID) | Control | Owner | Phase |
|---|---|---|---|
| Account Access Removal | PAM w/ break-glass accounts; monitor anomalous credential changes/mass deletions | security/senior-secops | detect |
| Data Destruction | Immutable versioned backups + strict access; recovery drills | security/incident-responder | respond |
| Data Encrypted for Impact (ransomware) | EDR w/ ransomware behavior blocking; offline encrypted backups | security/threat-detection-engineer | prevent |
| Data Manipulation | FIM + cryptographic hashing to detect unauthorized changes to stored/transmitted/runtime data | security/threat-detection-engineer | detect |
| Defacement | WAF + content-change alerts; restrict internal customization via GPO | security/senior-secops | prevent |
| Disk Wipe | MFA for disk-level ops; host IPS blocks raw disk writes | security/senior-secops | prevent |
| Email Bombing | Rate limiting + spam filtering + throttling; threat intel blocks malicious sender IPs | networking/network-engineer | prevent |
| Endpoint Denial of Service | Auto-scaling + rate limiting + WAF to absorb floods | cd/sre | prevent |
| Financial Theft | Segregate financial systems; transaction limits; dual approval for transfers | backend/payments-billing-engineer | prevent |
| Firmware Corruption | Secure boot + signed firmware; audit firmware versions; BIOS write-protection | security/cloud-security-architect | prevent |
| Inhibit System Recovery | Immutable backup repos; restrict backup service accounts; weekly restore tests | security/incident-responder | respond |
| Network Denial of Service | ISP/DDoS scrubbing; anycast routing | networking/network-engineer | prevent |
| Resource Hijacking | Monitor cloud spend/compute anomalies; least-privilege on SaaS/VM | security/cloud-security-architect | detect |
| Service Stop | Auto-restart policies; SIEM alerts on service state | cd/sre | respond |
| System Shutdown/Reboot | Restrict to admins; centrally log events | security/senior-secops | prevent |
