# PRD — Hermes Local LM Studio Connector

**User goal**: make Hermes talk reliably to a locally hosted LM Studio
OpenAI-compatible API, entirely through Docker Compose, with externalized
config and minimal attack surface — a stable interface Hermes never has to
know is swappable for another inference provider later.
**Out of scope**: auth providers, multi-user support, Kubernetes, load
balancing, multiple model providers, agent orchestration, persistent
conversation storage, metrics dashboards.

**Target repo**: `ai-stress-testing/docker-hermes` (implementation ships
there, not in this roster repo). This document records the spec-driven
decomposition per `agents/pm/project-manager`.

## Requirements

1. Backend exposes `POST /v1/chat/completions`, OpenAI-format compatible.
2. Backend forwards chat requests to LM Studio's OpenAI-compatible API.
3. Backend configuration (LM Studio host/port, timeout, default model) is
   entirely environment-variable driven — no code change to reconfigure.
4. Backend returns standardized errors (timeout, model unavailable, invalid
   request) without leaking internal details.
5. `GET /health` returns `{"status": "healthy"}` unconditionally once the
   process is up.
6. `GET /ready` checks backend liveness *and* LM Studio reachability.
7. Graceful shutdown: in-flight requests complete before the container
   exits (SIGTERM handling).
8. Single `docker-compose.yml` brings up hermes + backend + lmstudio (or an
   external LM Studio connection) on a dedicated bridge network
   (`hermes-net`) with `docker compose up -d` and no manual steps beyond
   `.env`.
9. Only the Hermes UI is published to the host; backend and LM Studio stay
   internal to `hermes-net` unless a developer explicitly opts in.
10. Containers run as non-root, drop unneeded capabilities, use read-only
    root filesystem where practical, and restart automatically on crash.
11. JSON logs carry timestamp, request id, latency, status code — never the
    prompt body, by default.
12. Backend is stateless so a future reverse-proxy can front N replicas
    without session affinity (no code change required for that later step).

## Constraints

- Backend added latency budget: <50ms excluding inference time.
- Stack startup: <10s to healthy.
- No Kubernetes, no auth layer, no metrics stack — MVP stays inside the
  PRD's stated non-goals; do not gold-plate.
- Secrets via env vars / Docker secrets only — nothing hardcoded.
- This is a fresh repo (`docker-hermes` currently holds only a README) —
  greenfield, no existing structure to preserve beyond `README.md`.

## Success criteria

- [ ] `docker compose up -d` in `docker-hermes` brings up hermes, backend,
      and lmstudio (or documented external LM Studio target) on
      `hermes-net`, all reporting healthy within 10s.
- [ ] A chat request through Hermes reaches LM Studio via the backend and
      returns a response.
- [ ] `/health` and `/ready` behave per FR-5/FR-6, including `/ready`
      correctly reporting LM Studio unreachable when it is down.
- [ ] Config changes (model, timeout, host/port) require only `.env`
      edits, no code changes.
- [ ] Backend and LM Studio are not published to the host in the default
      compose file; only Hermes UI is.
- [ ] A `logicians/falsifier` pass and a `security/appsec-engineer` (or
      `senior-secops`) pass both record a verdict before this is called
      done (`COMMS.md` attribution, `WORKFLOW.md §5`).
