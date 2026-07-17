# Ges-Talt

Personal Claude Code staging environment: agents, skills, and the config that
runs them.

## Philosophy

**Project-Subclass driven, not feature-driven.** Agents aren't organized
around one-off features ("the auth agent", "the checkout agent"). They're
organized around durable org roles — the way Amazon or Spotify split a
company into teams, not around whatever shipped last sprint. A team owns a
subclass of problems (frontend, backend, networking, logic review...)
forever; features come and go through them.

**Brains and hands, split.**
- [`agents/`](agents/) — the brains. Personas, capabilities, models, system
  prompts, tools, acceptance criteria. What an agent *is* and *decides*.
- [`environments/`](environments/) — the hands. Where an agent runs: MCP
  tunnels, networking permissions, session lifecycle. What an agent *can
  reach*. (Deferred past Sprint0 — see below.)

**Token-efficient by construction.** Every agent gets the cheapest model
that can do its job, the narrowest tool set its job requires, and a lean
system prompt — no vibe copy, no restated-code-comments-as-prose. Reasoning
depth (Opus) is reserved for roles that are actually reasoning-bound, not
handed out by default. See the `logicians/logician` agent for the pattern:
read-only tools + the strongest model, because the spend buys reasoning
depth, not blast radius.

## Layout

```
agents/<team>/<role>/
  agent.md   — loadable Claude Code subagent (frontmatter + lean system prompt)
  SPEC.md    — the full card: persona, capabilities, model + tool rationale,
               acceptance criteria, handoffs
environments/
  (deferred — see environments/README.md)
```

Teams can nest sub-roles (see `agents/frontend/`: `designer/` and
`react-dev/` under one team). Start a new team the same way `pm/`,
`backend/`, `networking/`, and `logicians/` were started here — one role is
enough to start; add siblings as the subclass grows.

## Provenance

Structural inspiration from two of my other repos:
- **agency-agents** — the division/catalog pattern (one persona file per
  role, a source-of-truth registry, lint scripts to keep the catalog
  honest). Borrowed the shape, not the prompt style — those agents are
  intentionally verbose; these are not.
- **ponytail** — the token-economy ethos (ladder-based reasoning, terse
  output, least-privilege by default). Borrowed the voice: every agent.md
  in this repo is written the way ponytail would write one.

## Status

Sprint0 in progress — see [SPRINT0.md](SPRINT0.md) for scope and acceptance
criteria.
