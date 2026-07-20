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
- [`secrets-crypto-engineer/`](secrets-crypto-engineer/) — key material
  and secrets lifecycle: KMS/HSM integration, key generation/rotation/
  revocation, envelope encryption (DEK wrapped by KEK), secrets storage
  and injection, crypto-agility. Distinct from `identity-access-engineer`
  (authN/authZ, not key material).
- [`senior-secops/`](senior-secops/) — PR-level gate: secrets/sensitive-
  data scan first, then implements or audits controls (auth, headers,
  CORS, rate limiting, CSP, logging) against the org's security standard.
- [`compliance-auditor/`](compliance-auditor/) — SOC 2 / ISO 27001 /
  HIPAA / PCI-DSS readiness assessment, gap tracking, evidence packages.
- [`regulated-data-specialist/`](regulated-data-specialist/) — technical
  scoping of regulated data: maps PCI-DSS cardholder-data/PHI flows,
  shrinks the compliance boundary via tokenization and data minimization.
  Distinct from `compliance-auditor` (readiness assessment) and
  `legal/data-protection-officer` (privacy program/obligations) — this
  role does the technical scoping and tokenization design, then hands
  implementation to the owning backend role.
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

**Spec-time consultants** (advisory — pulled in during spec modeling per
issue #50, then hand implementation to the owning role):

- [`rbac-abac-consultant/`](rbac-abac-consultant/) — designs the
  access-control model (RBAC/ABAC/hybrid, least privilege, SoD) →
  `identity-access-engineer` implements.
- [`rls-consultant/`](rls-consultant/) — designs deny-by-default Row-Level
  Security predicates for tenant/row isolation → backend/DBA implements.
- [`pq-crypto-consultant/`](pq-crypto-consultant/) — hybrid classical+PQ
  key exchange (X25519/P-256 + ML-KEM/Kyber) and migration path →
  `secrets-crypto-engineer` implements.
- [`side-channel-analyst/`](side-channel-analyst/) — flags timing/cache/
  oracle/response-distinguishability leaks, specifies constant-time /
  indistinguishable-response requirements → `testing/` measures, implementer fixes.
- [`red-team-critic/`](red-team-critic/) — opus, read-only: presumes a
  blue-team control already beaten and reasons to the concrete bypass (the
  `logicians/falsifier` pattern aimed at defenses; the 1:1 blue↔red pairing
  is in [`docs/opsec/red-team.md`](../../docs/opsec/red-team.md)). Distinct
  from `penetration-tester` (active, authorized testing).

**Skipped**: `blockchain-security-auditor` — smart-contract/DeFi audit
work is off-mission for this enterprise-engineering workspace; no cloud/
web-app system here has a smart-contract attack surface to credibly
reframe it around.

## OPSEC playbook (issue #21)

The team's applied controls live in [`docs/opsec/`](../../docs/opsec/) —
defensive checklists organized against the MITRE ATT&CK matrix, one file
per tactic, each row owned by a specific role at a specific phase
(prevent/detect/respond). The gate rule: **every major output passes
through OPSEC** — the relevant tactic checklist is run before the output
ships, as the security step of the verdict loop. `architect` runs it at
design time, `senior-secops` at the PR gate, `threat-detection-engineer`
builds the detections, `incident-responder` owns the response playbooks.
All 15 tactics (Reconnaissance → Impact) are in place, plus the efficacy
verifiers (`docs/opsec/hard-verifiers.md`) and the standing red-team
critique (`docs/opsec/red-team.md`).

Add more roles the same way — one folder per role, `agent.md` + `SPEC.md`,
narrowest tools and cheapest sufficient model, and a row added to this
list.
