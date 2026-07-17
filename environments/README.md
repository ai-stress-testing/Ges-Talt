# Environments (the hands)

Where an agent runs, and what it can reach. Deferred past Sprint0 by
design — the brains (`agents/`) needed to exist and follow a real
convention before it's worth building the substrate under them.

## Scope for Sprint1+

- **MCP tunnels** — which MCP servers each environment connects to, and
  under what scope. `networking/network-engineer` (see `agents/`) owns
  this once it's built.
- **Networking permissions** — egress allowlists, proxy rules, per-
  environment network policy (mirrors the network-policy concept this
  Claude Code Remote session itself runs under).
- **Proactive session deletion** — a policy/routine for reaping stale or
  finished sessions instead of letting them idle indefinitely. Likely
  implemented as a scheduled Routine once this repo has environments
  worth cleaning up.
- **Other networking config** — DNS, service-to-service rules, whatever
  else `networking/network-engineer`'s tickets surface as real needs.

## Why deferred, not skipped

Building environment/infra config against zero real agents would be
guessing at requirements the agents haven't stated yet — exactly what
`pm/project-manager`'s acceptance criteria (see `agents/pm/`) exist to
prevent. Once a team in `agents/` actually needs a tunnel or an allowlist
entry, that need becomes a ticket here, not before.
