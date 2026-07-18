# Security Team

Owns the org's security posture end to end: design-time threat modeling,
pre-merge code and control review, cloud/infrastructure hardening,
compliance readiness, live detection, and incident response. Distinct
roles split by *when* they engage (before code exists, at merge time, in
production, after a breach) and by *what* they touch (app code vs. cloud
infra vs. the network/detection layer).

- [`architect/`](architect/) — design-time threat modeling and
  trust-boundary review. Read-only; opus-backed for the one genuinely
  reasoning-bound job in the team.
- [`appsec-engineer/`](appsec-engineer/) — secure SDLC: threat modeling
  a feature, code-level review and fixes, SAST/DAST/SCA in CI.
- [`cloud-security-architect/`](cloud-security-architect/) — zero-trust
  IAM/network design, policy-as-code guardrails, IaC and pipeline
  hardening.
- [`identity-access-engineer/`](identity-access-engineer/) — auth/authz
  implementation: OAuth/OIDC, enterprise SSO (SAML/OIDC) + SCIM,
  passkeys/WebAuthn, session and multi-tenant RBAC/ABAC. Moved here when
  `platform/` was dissolved — IAM is a security concern.
- [`senior-secops/`](senior-secops/) — PR-level gate: secrets/sensitive-
  data scan first, then implements or audits controls (auth, headers,
  CORS, rate limiting, CSP, logging) against the org's security standard.
- [`compliance-auditor/`](compliance-auditor/) — SOC 2 / ISO 27001 /
  HIPAA / PCI-DSS readiness assessment, gap tracking, evidence packages.
- [`penetration-tester/`](penetration-tester/) — authorized offensive
  testing of the org's own systems, strictly within a signed engagement
  scope.
- [`threat-detection-engineer/`](threat-detection-engineer/) — builds and
  tunes the SIEM detection layer, maps MITRE ATT&CK coverage, runs hunts.
- [`threat-intelligence-analyst/`](threat-intelligence-analyst/) — tracks
  adversary groups/campaigns, produces confidence-rated intelligence,
  drafts candidate detection rules.
- [`incident-responder/`](incident-responder/) — breach triage,
  containment, forensics, post-mortems. Handoffs are written generically
  (devops/on-call, `pm/project-manager`) since this team doesn't assume
  which other teams exist elsewhere in the org.

**Skipped**: `blockchain-security-auditor` — smart-contract/DeFi audit
work is off-mission for this enterprise-engineering workspace; no cloud/
web-app system here has a smart-contract attack surface to credibly
reframe it around.

Add more roles the same way — one folder per role, `agent.md` + `SPEC.md`,
narrowest tools and cheapest sufficient model, and a row added to this
list.
