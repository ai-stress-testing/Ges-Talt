# Ges-Talt

[![gate](https://github.com/ai-stress-testing/ges-talt/actions/workflows/gate.yml/badge.svg)](https://github.com/ai-stress-testing/ges-talt/actions/workflows/gate.yml)
[![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![deps: stdlib-only](https://img.shields.io/badge/deps-stdlib--only-brightgreen.svg)](docs/for-ai-agents.md)

Personal Claude Code staging environment: agents, skills, and the config that
runs them.

New here (human or agent)? Start with **[`docs/for-ai-agents.md`](docs/for-ai-agents.md)**
— architecture, setup, common commands, and troubleshooting.

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

## What interacting with Ges-Talt might look like

A goal comes in; the orchestrator names the owning role, routes to it, and
records the verdict. Kept deliberately small:

```
you ▸ Add rate limiting to the public API.

Ges-Talt ▸ APIs are critical-path (#74), so this routes to the API owner
           and gets the hardening gate, not a rubber stamp.

           → Agent(subagent_type="backend-api-platform-engineer",
                   "add token-bucket rate limiting to the public API")
           ← implemented: per-key limiter + 429s + retry-after   (sonnet, 41,203 tok)

           → Skill("api-hardening-review")   # required gate for an API
           ← PASS 22/23 · 1 FAIL: limiter trusts a client X-Forwarded-For header

           Fixed the spoofable header, re-ran: PASS 23/23. Verdict recorded
           (ledger + run-manifest). gate.py green. Want me to open a PR?
```

The shape is always the same: **route to the role that owns it → gate at a
depth that matches the blast radius → record the outcome.** A lower-risk
change skips the falsifier/hardening pass and takes the lint/test gate
(`scripts/gate.py`) instead — same loop, cheaper rung.

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
