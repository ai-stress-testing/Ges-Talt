# DevOps Team

Owns the automation, reliability, and cost-efficiency of everything running
in production - distinct from `backend/` (what the service does) and
`networking/` (what can talk to what).

- [`devops-automator/`](devops-automator/) - Infrastructure as Code, CI/CD
  pipelines, zero-downtime deployment strategies.
- [`sre/`](sre/) - SLOs, error budgets, observability, toil reduction,
  chaos/capacity engineering.
- [`finops-engineer/`](finops-engineer/) - cloud cost allocation, waste
  elimination, rightsizing, commitment planning.

Same `agent.md` + `SPEC.md` convention as every other team in this repo. Add
a role here when it owns a durable subclass of production-operations work,
not a one-off deployment task.
