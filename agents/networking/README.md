# Networking Team

Owns connectivity and access boundaries: what can reach what, and how it's
proxied, served, and resolved. The team that keeps `environments/`'s
network policy honest.

- [`network-engineer/`](network-engineer/) — connectivity and access
  boundaries: MCP tunnels, egress allowlists, proxy rules, per-environment
  network policy, DNS. Owns and applies `environments/network-policy.md`.
- [`nginx-specialist/`](nginx-specialist/) — consultant: NGINX reverse-proxy
  and web-server design — topology, TLS floor, rate/connection limits,
  caching, upstream load-balancing + health checks, header/banner hygiene.
  Advises during spec modeling, hands the running config to
  `network-engineer`.

Reverse proxy / web serving / load balancing lives here (not in devops) —
it's a connectivity concern, and the OPSEC recon checklist already assigns
reverse-proxy controls to this team. Same `agent.md` + `SPEC.md` convention
as every other team; add a role when it owns a durable connectivity
subclass.
