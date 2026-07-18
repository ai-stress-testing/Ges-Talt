# DevOps Team

Owns the path to production and what happens once code is there — with a
deliberate bias toward **catching failure before it ships**, not managing
it after. Distinct from `backend/` (what the service does) and
`networking/` (what can talk to what).

- [`devops-automator/`](devops-automator/) - Infrastructure as Code, CI/CD
  pipelines, zero-downtime deployment strategies; wires security scanning
  and monitoring into the pipeline so failures surface pre-ship.
- [`gitops-engineer/`](gitops-engineer/) - git as the source of truth for
  deployable state: declarative manifests, drift detection, PR-as-deploy,
  rollback-by-revert. Keeps bad state from reaching prod out-of-band.
- [`sre/`](sre/) - SLOs, error budgets, observability, toil reduction,
  chaos/capacity engineering.
- [`finops-engineer/`](finops-engineer/) - cloud cost allocation, waste
  elimination, rightsizing, commitment planning.

## Where error-handling gets moved off prod

The shift-left goal is shared, not one role's job: `testing/` verifies
empirically before ship, `security/appsec-engineer` + `senior-secops`
gate the PR, `gitops-engineer` makes prod a reflection of reviewed git
(so nothing lands un-reviewed and rollback is one revert), and `sre` owns
the error budget that decides when to stop shipping. What is **not yet
owned**: progressive-delivery / release-gate discipline (canary, staging
parity, failing a release before full rollout) — tracked as a gap, see
the backlog.

Same `agent.md` + `SPEC.md` convention as every other team in this repo. Add
a role here when it owns a durable subclass of production-operations work,
not a one-off deployment task.
