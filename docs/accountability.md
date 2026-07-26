<!-- owner: pm/delivery-lead · last_validated: 2026-07-26 -->
# Accountability layer (#92, adopted from #78)

#78 has an explicit exec/leadership tier; Ges-Talt has none — which is exactly
why the RACI "A" (#84) had nowhere to resolve. This names the **Accountable**
heads **by elevating existing roles**, *without* adding a manager tier. A
manager tier would reintroduce the star-topology chokepoint the mesh
deliberately rejects (issue #59's original failure). Accountability is a
*hat an existing role wears*, not a new node work routes through.

## The heads (elevated, not added)

| Accountable head | Is the existing role | Accountable for |
|---|---|---|
| **CISO** | `security/architect` | security posture, threat model, the security "A" on any critical-path release |
| **CLO** | `legal/general-counsel` | legal exposure, the risk register's legal domain, compliance sign-off |
| **Delivery director** | `pm/delivery-lead` | portfolio priority, release go/no-go accountability, the delivery risk statement |
| **Product owner** | `pm/project-manager` | the PRD, scope, acceptance criteria |
| **Engineering lead** | `logicians/software-architect` | cross-system architecture, ADR sign-off |
| **Design lead** | `design/ux-architect` | information architecture, design-spec sign-off |

## The rule (mesh-preserving)

- **One A per initiative**, drawn from the table above by domain. It is the
  RACI "A" (`docs/templates/issue-spec.md`).
- **Work does not route *through* the A.** Peers still hand off peer-to-peer
  (`agents/ORCHESTRATION.md`); the A owns the *outcome* and signs the verdict,
  it is not a queue every task waits in. No rising fan-through — if everything
  starts flowing through one head, that's the chokepoint and it's a bug.
- **The A is the escalation terminus**, not the default path. Attempt-4 FAIL
  still escalates to `pm/project-manager` (`WORKFLOW.md`); cross-domain
  conflict escalates to the relevant head above.

## Role-gap evaluation (#78-exposed, keep/skip — owner-gated)

#78 and the #75/#76 audits suggest role gaps. Per the roster rule (a durable
subclass earns a role, else skip), here is the keep/skip **recommendation** —
**no role is added without explicit owner approval**:

| Candidate gap | Recommendation | Rationale |
|---|---|---|
| **support / IT-ops** | **SKIP for now** | No product in a meta-repo means no end-user support surface. Revisit when the agency runs a live product for a target repo. |
| **research-scientist** | **KEEP — thin** | A genuine gap adjacent to `academic/` and `ai/`: evaluating novel techniques before adoption. Recommend one read-only `academic/research-scientist` (reason tier), not the #78 sr/mid/jr ladder. Owner-gated. |
| **unified GRC lens** | **KEEP as a lens, not a role** | Governance-Risk-Compliance is already covered by `security/compliance-auditor` + `legal/*` + this risk register. Recommend federating them under the CLO head (above) rather than adding a `grc-manager` role. |
| **marketing / launch** (from #75) | **KEEP — thin** | `design/brand-guardian` covers brand voice but no one owns launch/positioning. Recommend a thin `pm/launch-coordinator` *or* extending `pm/program-tracker`'s charter. Owner-gated. |

**Decision status**: recommendations only. Any role actually added goes through
the `pm/project-manager` flow (`docs/templates/issue-spec.md`) and must leave
`python3 scripts/build_index.py` exit 0. This document adds **zero roles**; it
names accountability over the roster that exists and records the gap analysis
for the owner's call.

## Non-goals

- No manager tier, no seniority ladder (#78's chokepoint — rejected in
  `docs/reviews/delivery-audit-2026-07.md`).
- No auto-added roles. Roster shape is the owner's decision.
