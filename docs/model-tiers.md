<!-- owner: ai/multi-agent-systems-architect · last_validated: 2026-07-26 -->
# Model tiers (GT-33)

## Why

Pinning a vendor model id (`sonnet`, `opus`, `haiku`) directly in every
role's frontmatter is a monoculture: swapping provider or model means
editing dozens of `agent.md` files, and there is no single point where
"what does `reason` mean today" is decided. `scripts/models.toml` is that
single point — a role declares a **capability tier**, not a vendor, and
the tier resolves to a concrete model in one place. Provider sovereignty
= edit one file, not the roster.

## The mapping

`scripts/models.toml` is the authoritative source. Current generation
(the Claude 5 family + Opus 4.8):

| Tier | Resolves to | Used for |
|---|---|---|
| `reason` | `claude-opus-4-8` | reasoning-bound roles: static review, architecture, threat modeling |
| `build` | `claude-sonnet-5` | implementation roles — the common case |
| `cheap` | `claude-haiku-4-5-20251001` | high-volume/low-complexity roles |
| `local` | `qwen-3.5-32b-local` | air-gapped/local SLM work: bulk extraction, summarization, pattern-level remediation (#91) |

Aliases (readable shorthands, resolve to the same current ids):
`opus` → `claude-opus-4-8`, `sonnet` → `claude-sonnet-5`,
`haiku` → `claude-haiku-4-5-20251001`, `fable` → `claude-fable-5`.

**Updating for a new model generation** is a one-line-per-tier edit in
`scripts/models.toml` — nothing in the roster changes, because roles
declare tiers/aliases, not raw ids. That is the model-sovereignty payoff
the Nous review asked for, made concrete.

## What a role may write

A role's frontmatter `model:` may be **any** of:

- an **alias** (`opus`/`sonnet`/`haiku`/`fable`) — the readable default the
  roster uses today, so a model bump doesn't churn 80+ files;
- a **tier** (`reason`/`build`/`cheap`) — declares intent, not a vendor;
- a **concrete id** (`claude-opus-4-8`, …) — when a role must pin a model.

All three resolve to the canonical id; `build_index.py` displays the
readable label and counts by it. An unrecognized value is a lint problem —
a typo would otherwise silently drop a role out of the **reason-tier**
read-only check (the check keys on whichever id `reason` maps to, not the
literal string "opus", so it survives a generation bump).

`agents/ai/ai-engineer/agent.md` is converted as the demonstration role
(`model: sonnet` -> `model: build`). All other roles keep their concrete
model id for now; migrating the rest of the roster is a follow-on, not
part of this change.

## Escalation ladder (#91, adopted from #78)

#78's alternative org repeats the *same function* at 4–5 model tiers (sr/mid/
jr/entry → fable/qwen/terra/luna). That is the insight worth taking — **cheaper
model tiers for cheaper work** — without the cost: 4–5 roles per function is
duplication and a chokepoint. Ges-Talt adopts the *granularity* **within a
single role**, not by cloning the role.

**The convention.** A role may route a task to the **cheapest tier that can do
it and escalate only on complexity**, rather than pinning one model for every
invocation:

```
local  →  cheap  →  build  →  reason
(bulk)    (haiku)   (sonnet)  (opus)
```

- **Default down.** Start at the cheapest tier the task plausibly fits (a
  bulk-extraction pass starts at `local`/`cheap`, not `build`).
- **Escalate on a trigger, not by default.** Escalate one rung when the task
  exhibits a complexity signal — ambiguity, a failed cheaper attempt, a
  critical-path blast radius (which also pulls in the #74 review tier), or a
  `DEPTH.md` depth trigger (`docs/depth-packs.md`). An always-escalating role
  is a *miscalibration*, visible in the ledger.
- **Measured, self-correcting.** Every escalation is a real delegated run in
  `docs/agent-ledger.jsonl`; `scripts/credit.py` → `docs/credit.md` surfaces a
  role whose escalation frequency doesn't match its work, so the ladder tunes
  itself through the feedback loop (`docs/feedback-loop.md`) instead of being
  asserted once.

**What this is not.** Not 4–5 roles per function (#78's duplication — rejected).
Not a requirement that local infra exist: the `local` tier is a declarable
abstraction now; provisioning a real local model is a follow-on, and until then
a role that would use `local` falls back to `cheap` without any roster change
(one edit in `models.toml`).

## Ownership

`ai/model-evaluator` owns a future **swap-eval**: run a role's acceptance
tests against an alternate (including open-weight) model for its tier and
report the delta, so sovereignty is *tested* — a tier swap is validated
against real acceptance criteria before it's adopted — not merely
asserted by editing `models.toml`. That swap-eval itself is not built by
this change; this change only makes the tier indirection exist and lints
it.
