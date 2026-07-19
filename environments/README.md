# Environments (the hands)

Where an agent runs and what it can reach. This is the substrate the roster
(`agents/`, the brains) runs on. Every file here implements a control from
`THREAT-MODEL.md` and is gated by the OPSEC network/secrets checklists
(`docs/opsec/`). Owned by `networking/network-engineer` (egress, MCP,
sessions) and `security/architect` (review of anything access-widening);
`security/secrets-crypto-engineer` owns the secret-injection path.

Principle: **default deny, declare to open.** Nothing is reachable, writable,
or persistent unless a file here says so — matching the roster's
least-privilege ethos applied to the runtime, not just the tool grants.

## Config

| File | Control | What it fixes |
|---|---|---|
| [network-policy.md](network-policy.md) | THREAT-MODEL C1 | Per-team egress allowlists; the exfil path (OPSEC 14) |
| [mcp-scoping.md](mcp-scoping.md) | THREAT-MODEL C2 | Which MCP servers each role may reach; the PM-injection blast radius |
| [permissions.md](permissions.md) | THREAT-MODEL C3 | Path-scoped writes; "PM writes docs/ only", mechanically |
| [secrets.md](secrets.md) | THREAT-MODEL C4 | Secrets never in repo/docs/image; runtime injection only |
| [session-lifecycle.md](session-lifecycle.md) | THREAT-MODEL C5 | Proactive reaping of stale sessions — **designed, not armed** |

Controls C6 (tool-widening lint) and C7 (external text is data) are already
live in `scripts/build_index.py` and the PM charter respectively.

## What's declarative vs live

These are declarative policy the runtime enforces (the Claude Code Remote /
Cowork environment, or any orchestrator adopting the convention). The lints
that can run in-repo already do (`build_index.py` tool boundaries, a secret
scan per `secrets.md`); the network/session enforcement is the runtime's job,
specified here precisely enough to configure it. The one deliberately unarmed
piece is session reaping — it deletes things, so it ships as a spec the owner
arms, not a live cron (see `session-lifecycle.md`).
