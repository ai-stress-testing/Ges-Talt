# Issue: <title>

**Sprint**: sprint-<m>-<y>-<dd>-<dd> · **Source**: `prd.md` §<n> / `user-journeys/<file>`
**Assignee (parent)**: `agents/<team>/<role>`
**Goal**: one sentence tying this issue to the user goal it serves. If it
doesn't trace to the PRD or a user journey, it doesn't get created.

## RACI (#84)

Formalizes the roles the mesh already implies — record them, don't leave them
tacit. Every initiative names its **Accountable** head (`docs/accountability.md`)
so the "A" resolves without inventing a manager tier.

| Role | Who | Notes |
|---|---|---|
| **Responsible** (does the work) | `agents/<team>/<role>` (the assignee) | one per sub-issue |
| **Accountable** (owns the outcome) | `security/architect` (CISO) / `legal/general-counsel` (CLO) / `pm/delivery-lead` (delivery) — pick the domain head | exactly one A |
| **Consulted** (2-way) | the consultation-proximity clique for this work (`agents/ORCHESTRATION.md`) — e.g. `security/*`, `legal/*` at spec time | record it, it's the C |
| **Informed** (1-way) | status-report recipients (`pm/program-tracker`, the owner) | |

**Named ownership** (per initiative, maps onto existing roster roles):
Executive Sponsor = repo owner · Product Owner = `pm/project-manager` ·
Engineering Lead = `logicians/software-architect` (or `backend/backend-architect`
for a backend-scoped initiative) · Design Lead = `design/ux-architect` ·
Marketing/launch = `design/brand-guardian` (if applicable).

## Spec

What must be true when this issue closes — contracts, constraints,
references. Statements a reviewer can falsify, not prose about intent.

## Sub-issues

Granularity rule: one deliverable, one owner, independently verifiable.
If a sub-issue needs two agents or two deliverables, split it again.
Decomposition overhead is itself a cost — don't split past the point
where the tracking outweighs the deliverable.

### 1. <title>
- **Assignee**: `agents/<team>/<role>` (narrowest fit from `agents/INDEX.md`)
- **Scope**: the single deliverable, stated as a noun.
- **Acceptance criteria**:
  - [ ] Checkable criterion — no "works well", name the observable result.
  - [ ] Another, if needed. Fewer, sharper criteria beat a long vague list.
- **Negative prompt** (do NOT):
  - Files/systems this sub-issue must not touch.
  - Abstractions/dependencies it must not introduce.
  - Scope it must not absorb, even if adjacent and tempting.
- **Verify**: the exact command or observation that proves it done.

### 2. <title>
…same shape.

## Dependencies

Direction, not vibes: `#1 blocks #2` — never just "related".
