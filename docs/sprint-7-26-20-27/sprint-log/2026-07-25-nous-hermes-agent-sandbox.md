# 2026-07-25 — Sandboxed NousResearch Hermes Agent deployment (docker-hermes)

**Session/agent**: main session (orchestrator), delegating to
`ai/ai-engineer`, `ci/containerization-engineer` (both later discarded —
see Decisions), `logicians/falsifier` (x2), `security/appsec-engineer`
(x2).
**Issues touched**: none filed as GitHub issues this run (same rationale
as GT-73 — see Decisions).
**Target repo**: `ai-stress-testing/docker-hermes`, branch
`claude/nous-hermes-agent-sandbox`, cut fresh from `main` (this repo,
`Ges-Talt`, only carries the PRD/process record).

```
run-id: 2026-07-25-nous-hermes-agent-sandbox
prompt: user request — sandboxed Docker deployment of "the Hermes agent
  by Nous group," full host hardware, single host-directory passthrough,
  file-creation capability, network path for LM Studio only. Mid-run
  correction from the user ("This still looks wrong, heres official
  documentation...") redirected the entire implementation — see Decisions.
agents: ai/ai-engineer (sonnet, 51,100 tok, discarded); ci/containerization-engineer
  (sonnet, 26,543 tok, discarded); logicians/falsifier x2 (opus, 44,365 +
  32,167 tok); security/appsec-engineer x2 (sonnet, 36,614 + 24,435 tok)
specs: user request (this run); no PRD file written — see Decisions
verdicts: falsifier round 1 (on discarded harness) FAIL (network/resource/
  uid-permission findings, moot once discarded); appsec round 1 (on
  discarded harness) PASS (no CRITICAL, 2 MEDIUM); falsifier round 2 (on
  the real-image deployment) FAIL (2 confirmed disproofs, D1 cap_drop
  justification didn't apply to capabilities, D4 contradictory boundary
  claims; several BLOCKED items resolved by the orchestrator directly
  fetching the upstream Dockerfile/docs rather than a third agent round)
  -> fixed; appsec round 2 (on the real-image deployment) PASS (no
  CRITICAL/HIGH; 1 MEDIUM, floating :latest tag) -> fixed.
  scripts/verify.py: 14/14 PASS; verify_comms.py/credit.py/audit_skills.py clean.
commits: docker-hermes 6ef0a97, 2900abe, 98205a6, f9f769e, adc63ee
  (branch claude/nous-hermes-agent-sandbox)
```

## Done
- **First implementation (discarded)**: a from-scratch Python harness
  (`agent/*.py`) reimplementing what the orchestrator assumed "Hermes
  tool-calling format" meant — a `<tool_call>`/`<tool_response>` XML-tag
  loop calling LM Studio directly, with three file tools sandboxed to a
  single workspace directory. Fully built, tested (29/29 pytest), and
  passed a falsifier + appsec gate (no CRITICAL findings; path-safety
  containment held). **This was the wrong artifact.** The user provided
  a link to `hermes-agent.nousresearch.com`, revealing that "Hermes
  Agent" is a real, separate NousResearch open-source product
  (`github.com/NousResearch/hermes-agent`, `nousresearch/hermes-agent`
  on Docker Hub) — a full agentic CLI with its own config, sessions,
  memory, skills, and terminal-execution backends — not something to
  reimplement. The custom harness and its Dockerfile/compose wrapper
  were deleted entirely (commit `f9f769e`).
- **Second implementation (shipped)**: a `docker-compose.yml` deploying
  the real `nousresearch/hermes-agent` image, configured to use LM
  Studio as its model provider. Single bind mount (`./hermes-data` ->
  `/opt/data`, matching the image's own persistent-state convention —
  config, sessions, memories, skills, and created files all land there),
  no published ports (interactive CLI, not gateway/API-server mode —
  user's explicit choice), no resource limits (full host hardware, also
  explicit), `host.docker.internal` wired for LM Studio reachability,
  and the image's own optional nested-Docker sandboxing left disabled
  (would require mounting `/var/run/docker.sock`, which is host access,
  not sandboxing).
- **Falsifier round 2 findings, both fixed**:
  1. `cap_drop`/`read_only` had been deferred using a "write patterns
     aren't documented" justification — valid for filesystem hardening,
     not for Linux capabilities, which don't depend on knowing app
     write patterns. Fixed: `cap_drop: ALL` + an explicit allowlist for
     what the image's root-then-drop s6-overlay startup needs.
  2. The compose file's "nothing else [reachable]" comment contradicted
     the README's own (accurate) admission that network egress reaches
     the LAN and internet, not just LM Studio. Fixed: scoped the claim
     to what it actually is (a mount claim, not a reachability claim).
  Also reworded the Docker-backend section (a default, not an enforced
  guarantee — `config.yaml` is writable and could later request
  `terminal.backend: docker`, which would simply have nothing to
  connect to by default) and added a `## Sources` section citing the
  four upstream docs/Dockerfile URLs every factual claim about the
  image rests on.
- **Appsec round 2 finding, fixed**: image pinned to `v2026.7.20`
  instead of the floating `:latest` tag — for supply-chain integrity on
  a container that autonomously executes commands from LLM output.
- **Orchestrator-direct verification (not delegated)**: after falsifier
  round 2 flagged several claims as `BLOCKED` (falsifier's tool set has
  no web access), the orchestrator fetched the real
  `NousResearch/hermes-agent` Dockerfile directly and confirmed:
  `VOLUME ["/opt/data"]` is the image's only declared volume,
  `HERMES_WRITE_SAFE_ROOT=/opt/data` is set at the image level, and
  `PUID`/`PGID` are genuinely documented (not invented, as falsifier
  worried) for the volume-ownership fixup. This resolved the falsifier's
  `BLOCKED-1`/`BLOCKED-2`/`BLOCKED-3` items without a third agent round
  and is what justified adding `read_only: true` (previously withheld
  for lack of exactly this evidence).

## Decisions
- **The discarded harness's implementers (`ai/ai-engineer`,
  `ci/containerization-engineer`) are recorded as ledger `verdict: PASS`
  despite their entire artifact being thrown away.** Same reasoning as
  the `logicians/falsifier` convention established in the GT-73 entry:
  the ledger scores whether the role executed correctly against the
  spec it was given, not whether the artifact shipped. Both built
  exactly what their prompts specified, correctly, and passed their own
  review round. The spec itself was wrong — the orchestrator assigned
  "reimplement Hermes tool-calling" without first checking whether
  "Hermes agent (nous group)" referred to an existing product. That's
  an orchestrator-level miss, not an implementer failure, and scoring
  it as implementer FAIL would misattribute the mistake.
- **This is the second time in two consecutive runs on this repo that a
  significant chunk of delegated work was discarded for a premise
  error the orchestrator could have caught earlier** (GT-73 didn't have
  this problem, but this run built a full custom harness before the
  user supplied a link revealing the real product existed). Worth
  naming directly rather than papering over: before delegating
  implementation of "the X agent by Y," a orchestrator should check
  whether X is a named product with its own docs before assuming it's
  a protocol/format to reimplement. Recording this here so it's not
  re-litigated silently next time; not proposing a process change
  beyond this note, since a single WebSearch at the start of *this* run
  would have caught it and no new verifier or roster change seems
  warranted for what's fundamentally a research-before-delegating
  habit.
- **No GitHub issues filed, no PRD file written**, for the same
  single-sprint/single-request reasoning as GT-73 — the user's request
  plus the (eventually) linked official docs served as the spec. The
  review/adversarial gate still ran twice (once on each artifact) and
  is recorded above.
- **Falsifier round 2's own tool set (`Read`, `Grep`, `Glob`) has no web
  access**, so several of its findings were correctly reported as
  `BLOCKED` pending a fetch rather than guessed at. The orchestrator
  closed those directly (see Done) instead of spawning a third
  falsifier round purely to re-read documents the orchestrator could
  fetch itself in one turn — same "direct verification over a redundant
  round" pattern as GT-73's fractional-`REQUEST_TIMEOUT` fix, extended
  here to research rather than execution.

## Blocked / carried
- **No `docker compose up`/`run` was executed against the real image.**
  Same sandbox constraint as GT-73 (Docker daemon needs root here;
  Docker Hub pulls are blocked by this environment's egress policy).
  The `cap_drop`/`cap_add`/`read_only`/`tmpfs` combination added in
  falsifier round 2's fix is grounded in the Dockerfile (see Done) but
  not empirically confirmed to boot cleanly — flagged in the README
  itself as a named follow-up, with a documented fallback order (drop
  `read_only`/`tmpfs` first, then `cap_drop`/`cap_add`) if it doesn't.
  `testing/reality-checker` is the named owner, not exercised this run.
- **The `setup` wizard flow, the exact provider-selection prompt
  wording, and whether `terminal.backend: docker` fails cleanly or
  degrades silently with no Docker socket present** are all sourced
  from the project's public docs, not from having run the wizard.
  Falsifier round 2 raised a sharp structural question about whether
  `docker compose run --rm hermes setup` is consistent with an
  `ENTRYPOINT`/`CMD` split — resolved by reading the actual Dockerfile
  (`ENTRYPOINT ["/init", ".../main-wrapper.sh"]`, `CMD []`, so `setup`
  is appended as an argument to the wrapper script, not exec'd as a
  standalone binary) and confirming the exact `setup` invocation is
  copied verbatim from the project's own Docker guide — but this is
  still a documentation read, not an execution trace.
