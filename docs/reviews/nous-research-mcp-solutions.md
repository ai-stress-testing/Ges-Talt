# Solutions to the Nous-lens review

Companion to `nous-research-mcp-review.md`. One solution per finding. Most
share a spine: **externalize what's expensive to keep resident, load it on
demand, let it compound across runs.** That spine is also the answer to #9.

## 1. Model monoculture → decouple role from vendor

Stop pinning vendor model IDs in frontmatter. Introduce a **capability
tier** (`reason` / `build` / `cheap`) that resolves to a concrete model
through one `models.toml` mapping. Roles declare a tier; swapping provider
= editing one file. `ai/model-evaluator` owns a swap-eval: run a role's
acceptance tests against an alternate open-weight model, report the delta,
so sovereignty is *tested*, not asserted. `build_index.py` already reads
`model:` — extend it to validate the tier resolves. Backward-compatible: a
concrete id still allowed. *(GT-33)*

## 2. Feedback is convention → make the controller act

The missing piece is a mechanism that *writes something selection reads*.
Build a **selection score** per role: `reward = w1·verdict_pass − w2·token_cost
− w3·retries`, updated from the ledger after every run into
`docs/selection-weights.json`. The PM reads those scores when choosing an
assignee (cheapest *sufficient* becomes cheapest *sufficient and proven*).
A scheduled controller (routine) recomputes scores and auto-opens an issue
when a role drifts past a threshold. That closes the loop without a human
in the middle — the verdict now changes future behavior. *(GT-32)*

## 3 + 7. Traces & memory → selective, distilled, lifecycle-managed

Keep both cheap by keeping only what you can learn from:
- **Traces** (#3): retain reasoning *only* for the falsifier's disproofs,
  any FAIL, and flagged high-stakes calls — under `docs/traces/`, referenced
  from the ledger. Not every run.
- **Memory** (#7): after a run the observer appends a 1–2 line *distilled
  lesson* to `docs/memory/<team>.md` ("backend-dev: SQLite migrations here
  aren't reversible — check dialect first"). Agents read their team file at
  start. Curated text, not a vector DB (YAGNI).

Both get a retention policy from `devops/lifecycle-manager` — stale traces
and lessons are pruned, not hoarded. Memory *lowers* token cost by cutting
re-derivation; it pays for itself.

## 4. Correlated grader → independence by construction

Rule: the adversary grader resolves to a **different model family** than the
artifact's author (mechanism comes free from #1's tier mapping). If only one
provider is reachable, degrade to a different tier *and* stamp a
`correlated-grader` warning on the verdict so the weakness is visible. Allow
a 2-grader ensemble where disagreement auto-escalates. *(new: GT-34)*

## 5. Grader-gaming → test the thermostat

`ai/model-evaluator` red-teams the grader on a cadence: feed known-bad
artifacts that *must* FAIL and known-good that *must* PASS; measure the
grader's false-negative rate. A plant that slips through = the grader is
degraded or gamed → alert. Vary the falsifier's stress set so an agent can't
memorize the attacks. *(new: GT-35)*

## 6. Star topology → mesh for the routine case

The orchestrator is only needed for the arbitration set (spec ambiguity,
cross-team conflict — already `WORKFLOW.md §2`). Make **direct peer handoff
the default** for everything else (agents already carry handoff targets in
their SPECs) and let a proximity **consultation clique** consult each other
in parallel, escalating only divergence. Measure fan-through: the ledger can
show what fraction of work routed through the center; drive it down. *(new:
GT-36)*

## 8. Ungoverned ephemerals → declare, check, log

An ephemeral agent must still declare inline frontmatter (name/desc/tools/
model); the orchestrator applies the tool-boundary rule (opus read-only,
etc.) *before* spawning, and logs it to the run + ledger with
`ephemeral: true`. Reused ≥3 times → promote to the roster via the PM flow.
Small: a spawn-time check plus a log field. *(new: GT-37)*

## 10. Non-reproducible runs → a run manifest

Each run gets a `run-id` and a structured header in its sprint-chat entry:
prompt, agents spawned (+tier +tokens), specs produced, verdicts, commits.
That's a replayable *decision* manifest (not the full transcript) — with the
ledger and retained traces (#3), a run reconstructs. Cheap: a header
convention. *(new: GT-38)*

---

## 9. Token economy × character depth — the joint optimum

The review framed this as a tradeoff. It isn't one — the tradeoff only
exists if you assume **character depth must live inline in every prompt**,
paying its token cost on every single call. Drop that assumption and the two
axes decouple. Three moves, together, dominate the "always-terse" and
"always-rich" points on *both* axes for the realistic workload:

**A. Progressive depth (load on demand, not as a per-call tax).**
Layer each role:
- **L0 — the terse charter** (~30 lines, today's `agent.md`): loaded every
  call. Handles the common case. Cheap.
- **L1 — a depth pack** (`DEPTH.md`: persona priors, 2–3 worked exemplars, a
  failure-mode playbook, voice): loaded *only* on a **depth trigger** —
  novelty off-charter, a high-stakes call, or a FAIL-retry.

Expected cost per call = `L0 + P(hard)·L1`. Since most calls are easy,
`P(hard)` is small, so expected resident cost stays near L0 while full depth
is *available exactly when it changes the outcome*. You pay for depth only in
the moments depth is what's failing you.

**B. Depth by exemplar, not adjective.** Character encoded as a few sharp
worked examples compresses far more steerable behavior per token than
paragraphs describing a persona. The repo already proves this: the 6-line
ladder block shapes behavior more than any amount of "be lazy but careful"
prose would. Depth packs are exemplars + invariants, not verbose bios.

**C. Depth that compounds instead of re-inflating.** Character accretes in
the external memory (#7) and traces (#3) as *distilled lessons*, referenced
not repeated. An agent's depth grows across runs while its per-call prompt
stays flat — depth becomes a growing external store, fully decoupled from
resident token cost.

**Why this is an optimum, not a compromise.** Plot each role on (resident
cost/call, behavioral coverage). "Always inline" buys coverage by paying
cost every call. "Always terse" saves cost by capping coverage. Tiered +
externalized + compounding depth moves to a *different curve*: for a workload
that is mostly-easy-with-rare-hard (every real workload), it is
Pareto-superior — lower expected cost **and** higher worst-case coverage than
either fixed point. It wins on both axes because it stops treating depth as a
constant and starts treating it as a resource allocated where marginal value
is highest.

**And it self-corrects.** The ledger records depth-pack load frequency. A
role that loads L1 on nearly every call has a miscalibrated L0 (its common
case needs more resident context) — the feedback loop (#29) catches that and
revises the setpoint. A role that never loads L1 under novelty may be
over-confident — the falsifier catches *that*. The optimum isn't set once; it
is found per role, by measurement. *(new: GT-39 — the marquee item.)*

---

## Cost triage

- **Cheap conventions, land anytime:** #8, #10, and #9's L0/L1 scaffold
  (`DEPTH.md` in TEMPLATE + a depth-trigger rule) — mostly doc/convention.
- **Real builds, need a sprint each:** #1 (tier mapping + swap eval), #2 (the
  acting controller), #3+#7 (traces + memory + retention), #9 full.
- **Rules that ride on #1:** #4, #5, #6.

All queued GT-32..GT-39. None built here — this is the solution design you
asked for; say which to schedule and the PM flow cuts the specs.
