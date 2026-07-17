# Agents (the brains)

Organized by **team → role**, not by feature. A team owns a durable
subclass of problems (frontend, backend, networking, logic review); roles
are the specific personas within it. Teams may have one role or several
nested ones — see `frontend/` for the nested case.

## Convention

Every role gets its own folder: `agents/<team>/<role>/`, containing:

- **`agent.md`** — the loadable Claude Code subagent. YAML frontmatter
  (`name`, `description`, `tools`, `model`) + a lean system prompt. This is
  what actually runs. Keep it short — persona, responsibilities, handoff,
  a short "never" list. No restated code comments, no vibe copy.
- **`SPEC.md`** — the full card: persona narrative, capabilities,
  model choice + why, tool list + why (least privilege), acceptance
  criteria for this agent's output, and who it hands off to.

`agent.md` is the contract an orchestrator reads to invoke the agent.
`SPEC.md` is the contract a human reads to decide whether the agent is
built right. They shouldn't duplicate each other's prose — `SPEC.md` can
just say "see agent.md" for the prompt itself.

## Adding a new agent

1. Copy `agents/TEMPLATE/` to `agents/<team>/<role>/` (new team, or a new
   role under an existing one).
2. Fill in both files. Pick the cheapest model that can do the job and the
   narrowest tool set the job needs — don't default to Opus + all-tools.
3. Add a row to the roster table below.

## Roster

| Team | Role | Model | Tools | One-liner |
|---|---|---|---|---|
| pm | [project-manager](pm/project-manager/) | sonnet | Read, Grep, Glob, TaskCreate/Update/List | Plans and sequences work across teams; writes acceptance criteria; never touches code. |
| frontend | [designer](frontend/designer/) | sonnet | Read, Grep, Glob, Write, Artifact | Owns UI/UX design intent; produces specs, not production code. |
| frontend | [react-dev](frontend/react-dev/) | sonnet | Read, Edit, Write, Bash, Grep, Glob | Implements React UI against a design spec and ticket. |
| backend | [backend-dev](backend/backend-dev/) | sonnet | Read, Edit, Write, Bash, Grep, Glob | Implements server-side logic, APIs, schema/migrations. |
| networking | [network-engineer](networking/network-engineer/) | sonnet | Read, Edit, Write, Bash, Grep, Glob | Owns connectivity and access boundaries: MCP tunnels, proxies, allowlists, DNS. |
| logicians | [logician](logicians/logician/) | opus | Read, Grep, Glob | Read-only correctness/logic review — invariants, edge cases, spec contradictions. |

Model and tool choices are per-agent decisions, not fixed by team — a
future `frontend/a11y-specialist` might need Opus-level reasoning on a
tricky WCAG edge case even though `react-dev` doesn't. Justify the choice
in that agent's `SPEC.md`, don't just copy the row above.
