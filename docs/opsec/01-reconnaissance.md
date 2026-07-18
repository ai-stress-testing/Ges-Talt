# OPSEC — 01. Reconnaissance (MITRE TA0043)

Source issue #22 "Anti-RQN" · owning roles: `security/threat-detection-engineer` + `networking/network-engineer` (supporting: `security/appsec-engineer`, `security/identity-access-engineer`, `legal/privacy-engineer`) · applied at design time (`security/architect` review) and PR gate (`security/senior-secops`).

Reconnaissance is the attacker's information-gathering phase — scanning for live hosts and open services, harvesting victim org/identity data, and mapping technical footprint before ever touching the target for real. OPSEC denies this by shrinking what's observable (hardened, unremarkable configs; minimal-exposure DTOs), feeding false signal back to anyone who does scan (honeypots, decoys), and making sure that even a fully mapped perimeter yields no usable foothold (segmentation, hidden topology, hard MFA). A noisy scan against this surface should look like nothing.

| Technique / Control area | Control | Owner | Phase |
|---|---|---|---|
| Active scanning / decoy infrastructure | Embed honeypots and decoy systems that analyze attacker scan patterns without revealing real infra | `security/threat-detection-engineer` | detect |
| Configuration hardening | Standardize and harden configs (containers); remove unnecessary services | `security/appsec-engineer` | prevent |
| Signature minimization | Change default banners; deploy defensive obfuscation where appropriate | `security/appsec-engineer` | prevent |
| Information exposure (API/data surface) | Minimize exposure of information to the public via DTOs that don't over-expose internal fields | `security/appsec-engineer` | prevent |
| Credential/identity hardening | Require MFA via hardware key or seed-based TOTP | `security/identity-access-engineer` | prevent |
| Network topology exposure | Implement network segmentation; hide network topology; use a reverse proxy | `networking/network-engineer` | prevent |
| Victim data / PII harvesting | Verify PII is not being leaked (logs, API responses, error messages, DTOs) | `legal/privacy-engineer` | detect |
