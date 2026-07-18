# If Nous Research reviewed the MCP — improvement points & why

Issue #30. "The MCP" here = this repo's **multi-agent control plane** — the
orchestration system (`agents/ORCHESTRATION.md`, `WORKFLOW.md`,
`COMMS.md`, the roster, the feedback loop), which is the reviewable
artifact. (If the literal Model-Context-Protocol wiring was meant: this
repo only *consumes* MCP servers via the harness; there's no MCP server
authored here to review — the plane below is the substantive target.)

This is a role-played critique from Nous Research's **publicly evident
priorities** — open weights and model sovereignty, agentic reasoning with
retained traces, RL-from-outcomes / verifier environments, decentralization,
memory/long-context, and honest evaluation. Not a statement on their behalf.

## Improvement points

1. **Model monoculture → provider lock-in.** Every role pins an Anthropic
   tier (`opus`/`sonnet`/`haiku`); the lint even encodes it. *Why it
   matters:* no open-weight fallback and no model sovereignty — the whole
   org's behavior is hostage to one vendor's changes, and the repo's own
   least-dependency ethos (ponytail) isn't applied to the biggest
   dependency of all. *Fix:* specify a **capability tier**, not a vendor;
   add an eval that swaps an open model into a role and measures the delta.

2. **The feedback loop is convention, not a mechanism.** `feedback-loop.md`
   says "revise success when surprised" — but a human does the revising.
   *Why:* Nous builds RL environments where a **verifier's signal actually
   updates behavior**. Here the ledger + verdict are recorded and then
   read by a person; nothing closes the loop autonomously, so #29's
   feedforward→feedback is aspirational until a controller acts on the
   error signal without a human in the middle.

3. **Reasoning traces are discarded.** Only the final quote + token count
   survive (`agent-ledger.jsonl`); the sub-agent's reasoning is gone.
   *Why:* you cannot debug a wrong verdict, distill a good one, or train
   on either without the trace. Retain traces at least for the adversary
   grader and high-stakes decisions.

4. **The adversary grader shares the producer's blind spots.** The
   falsifier is `opus` — same family as most agents it grades. *Why:* a
   verifier correlated with the producer misses exactly the failures the
   producer is prone to. *Fix:* cross-model / cross-family grading, or an
   ensemble verifier; independence is the whole value of an adversary.

5. **No defense against grader-gaming.** `feedback-loop.md` flags "causal
   not correlated measures" but nothing detects an agent optimizing the
   grader instead of the goal. *Why:* Nous is openly skeptical of
   benchmark/verifier gaming. *Fix:* have `ai/model-evaluator` red-team the
   grader on a cadence.

6. **Star topology = bottleneck and single point of failure.** One
   orchestrator routes everything; the PM chokepoint (AUDIT.md, Audit 2)
   is the same shape one level down. *Why:* the PDF scaffolding this org
   cites argues coordination can be **emergent through proximity**, yet the
   implementation is centrally controlled. Worth naming as a deliberate
   tension: central control is legible but caps throughput and resilience.

7. **No cross-run memory.** Every sub-agent starts cold and re-derives
   context; the ledger stores cost, not lessons. *Why:* the token pressure
   the org treats as a first-class constraint (issue #14) is partly
   self-inflicted by amnesia — memory/long-context is exactly where Nous
   would push. Persistent, queryable agent memory would cut re-derivation.

8. **Ephemeral agents bypass the guardrails.** `ORCHESTRATION.md` permits
   throwaway agents, but the threat model's roster-integrity controls
   (tool-boundary lint, review of tool widening) don't cover an agent that
   never hits the roster. *Why:* an ephemeral agent is an unlogged,
   unlinted privilege grant — the one hole in an otherwise tight model.
   *Fix:* ephemeral agents still declare tools and get logged to the run.

9. **Persona depth vs. token economy — a real tradeoff.** Charters are ~30
   terse lines by design (ponytail). *Why Nous would push back:* they
   invest in character/steerability because thin specs under-determine
   behavior under novel stress. This isn't a clear defect — it's the
   repo's deliberate bet — but the failure mode (an agent improvising
   wrongly off-charter) is real and currently only caught downstream by
   the grader, not prevented up front.

10. **Runs aren't reproducible.** The stack is transparent markdown +
    Python (Nous would approve the openness), but a *run* — the sprint
    chat log — is prose, not a replayable trace. *Why:* reproducibility is
    the base of honest evaluation; a run you can't replay is a run you
    can't verify a claim about.

## What holds up well

Transparency (all plain text, no black-box framework), the observer-writes-
credit separation (`COMMS.md`) which directly answers the scaffolding's
credit-attribution warning, token cost as an explicit selection pressure,
and the opus-read-only invariant (reasoning spend without blast radius) are
all things a Nous review would credit rather than flag.

## The through-line

Most findings are one theme: **the org measures but doesn't yet learn.** It
records cost and verdicts (feedforward with a gauge) but no mechanism turns
those into adapted behavior (true feedback). Points 2, 3, 4, 5, 7 are all
that gap. Closing it — a verifier signal that actually updates selection,
with retained traces and an independent grader — is the highest-leverage
next move, and it's the same gap `feedback-loop.md` admits at its end.
