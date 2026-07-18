# Platform Team

Owns cross-cutting engineering concerns that no single product team owns on
its own: system-wide architecture, internationalization, identity, and the
documentation/onboarding surface that makes the rest of the org legible.

- [`software-architect/`](software-architect/) - cross-system architecture,
  domain modeling, ADRs. Read-only + opus, this repo's other
  reasoning-bound role alongside `logicians/code-reviewer`.
- [`i18n-engineer/`](i18n-engineer/) - internationalization and
  localization engineering.
- [`identity-access-engineer/`](identity-access-engineer/) - auth, SSO,
  sessions, and multi-tenant authorization.
- [`codebase-onboarding-engineer/`](codebase-onboarding-engineer/) -
  read-only repo exploration and execution tracing for new contributors.
- [`technical-writer/`](technical-writer/) - developer documentation and
  docs-as-code pipelines.
- [`lifecycle-manager/`](lifecycle-manager/) - lifecycle policy for
  long-lived artifacts (API versions, containers, dependencies, schemas,
  environments/sessions) - states, owners, and dates, not implementation.

Same `agent.md` + `SPEC.md` convention as every other team in this repo. Add
a role here when it's a durable cross-cutting concern rather than a single
product team's problem.
