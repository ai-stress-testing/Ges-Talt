# Sprint0

Start small: define the repo split and prove the convention with a handful
of real agents, not a full org chart.

## Scope

- [x] Split the repo into `agents/` (brains) and `environments/` (hands).
- [x] Define the per-agent folder convention: `agent.md` (loadable Claude
      Code subagent) + `SPEC.md` (persona, capabilities, model + tool
      rationale, acceptance criteria, handoffs).
- [x] Scaffold a template (`agents/TEMPLATE/`) so new agents follow the same
      shape without re-deriving it.
- [x] Stand up five teams with one role fleshed out each: `pm`, `frontend`
      (two roles, to demonstrate nesting: `designer` + `react-dev`),
      `backend`, `networking`, `logicians`.
- [x] Write `agents/README.md` as the roster + conventions doc.
- [x] Stub `environments/` with a roadmap instead of building it out.

## Explicitly out of scope for Sprint0

- Environments work itself: MCP tunnels, networking permissions/allowlists,
  proactive session deletion. Tracked in `environments/README.md` as
  Sprint1+.
- Install/build tooling that renders `agent.md` files into a live
  `.claude/agents/` directory (agency-agents' `convert.sh`/`install.sh` is
  the reference pattern if/when this repo needs it — not needed yet with
  six agents).
- Lint/CI scripts to keep the roster honest (agency-agents'
  `check-divisions.sh` / `lint-agents.sh` pattern). Worth adding once the
  roster is large enough that drift is likely, not before.

## Acceptance criteria

- [ ] Every agent under `agents/` has both `agent.md` and `SPEC.md`.
- [ ] Every `agent.md` has valid frontmatter (`name`, `description`,
      `tools`, `model`) and a system prompt under ~40 lines.
- [ ] Every `SPEC.md` states a model choice with a one-line rationale, a
      tool list with a one-line rationale, and a checkable acceptance
      criteria list (no "make it good"-style criteria).
- [ ] `agents/frontend/` demonstrates team → role nesting.
- [ ] `agents/README.md` roster table lists all six agents accurately.
- [ ] `environments/README.md` exists and scopes what's deferred, so
      Sprint1 has a concrete starting point instead of a blank page.
