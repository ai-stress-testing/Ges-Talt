# Network policy — egress allowlists

THREAT-MODEL C1. **Default deny all egress**; a team reaches only the
destinations declared below. This is the single highest-value control
against exfiltration (OPSEC 14) and C2 (OPSEC 13): if a compromised agent
can't reach an undeclared host, it can't phone home or ship data out.

Owner: `networking/network-engineer`. Widening a team's allowlist is
access-widening → `pm/project-manager` sign-off + `security/architect`
review (per `agents/WORKFLOW.md §2`).

## Verifier

The allowlist is not trusted because it's written down — it's verified: the
egress-allowlist hard-verifier (`docs/opsec/hard-verifiers.md`) probes a
non-allowlisted host from each team's context and asserts the connection is
blocked. A reachable undeclared host is a FAIL, not a note.

## Allowlists (declare the minimum, never "*")

| Team | Allowed egress | Why |
|---|---|---|
| default (all) | none | Deny is the floor; every row below is an explicit exception. |
| ai | the configured model-provider endpoint(s) only | Inference calls; nothing else. |
| backend | its own datastores + explicitly declared upstream APIs | Per-service, per-ticket; no blanket internet. |
| data | declared warehouse/lake endpoints | ETL sources/sinks named in the pipeline. |
| devops | package registries + cloud control-plane APIs (scoped) | Builds and deploys; pinned registries only. |
| networking | as required to configure the perimeter it owns | The one team that edits this file. |
| frontend / mx | build-time package registries only | No runtime egress from the build. |
| logicians / academic / pm / legal / testing (review roles) | none | Read the repo; reach nothing outbound. |
| security | threat-intel feeds + scanners it operates (declared) | Detection/hunting sources, named. |

Rules:
- No `0.0.0.0/0`, no wildcard destination, no "to be safe" pre-opens.
- A new external dependency = a new allowlist row with a ticket, not a code
  change that silently assumes reachability (`backend/backend-dev`'s Never
  list already forbids this).
- Read-only review teams get **none** — a reviewer that needs the network is
  scoped wrong.
