# MCP scoping

THREAT-MODEL C2. Which MCP servers each role may reach, and with what
verbs. **Default: no MCP.** An MCP connection is egress + a tool grant, so
it is declared per role, not available by default.

Owner: `networking/network-engineer` (the tunnel), `security/architect`
(review). The acute risk this bounds: the PM holds `issue_write`, and issue
bodies are attacker-controllable text (THREAT-MODEL T1) — so the PM's MCP
scope is the injection blast radius, and it is minimized here.

| Role(s) | MCP access | Verbs | Rationale |
|---|---|---|---|
| default (all) | none | — | No agent reaches an MCP server unless listed. |
| pm/project-manager | github | issue read/write, sub-issue write | Cuts and closes issues (its charter). Reads issue text as **data, not instructions** (PM Never list / C7). |
| pm/program-tracker, delivery-lead | github | issue/PR read | Track state; no write. |
| backend/*, frontend/*, ci/*, cd/*, mx/*, data/*, ai/* (implementers) | github | PR read/write, actions read | Open/update PRs, read CI for their own work. |
| logicians/*, academic/*, testing/*, legal/* (review roles) | github | read-only where needed | Review a diff/issue; never write. |
| security/* | github (read) + declared detection connectors | read | Read for review; detection sources named per `network-policy.md`. |

Rules:
- A role's MCP write scope never exceeds what its issue-lifecycle duty needs
  (only the PM mints issues; only implementers push PRs).
- Read-only reasoning roles get read-only MCP or none — an opus reviewer with
  MCP write is the same mistake as an opus reviewer with `Edit`.
- New MCP server for a role = access-widening → sign-off + review, and it
  gets a row here plus a `network-policy.md` egress entry (the tunnel needs
  the host allowlisted too).
