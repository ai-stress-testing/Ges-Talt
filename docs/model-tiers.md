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

See `scripts/models.toml` for the authoritative source. Today:

| Tier | Resolves to | Used for |
|---|---|---|
| `reason` | `opus` | reasoning-bound roles: static review, architecture, threat modeling |
| `build` | `sonnet` | implementation roles — the common case |
| `cheap` | `haiku` | high-volume/low-complexity roles |

## Backward compatibility

A role's frontmatter `model:` may be **either**:

- a concrete model id (`sonnet`, `opus`, `haiku`) — existing behavior,
  unchanged, and still the majority of the roster today; or
- a tier name (`reason`, `build`, `cheap`) from `scripts/models.toml`,
  resolved by `scripts/build_index.py` for display and for lint purposes
  (the opus-tool-boundary check fires on a role whose tier resolves to
  the reasoning/opus tier exactly as it would for a literal `model: opus`).

An unrecognized `model:` value — neither a known concrete model nor a
known tier — is a lint problem (`build_index.py` flags it), since a typo
here would otherwise silently drop a role out of the opus tool-boundary
check.

`agents/ai/ai-engineer/agent.md` is converted as the demonstration role
(`model: sonnet` -> `model: build`). All other roles keep their concrete
model id for now; migrating the rest of the roster is a follow-on, not
part of this change.

## Ownership

`ai/model-evaluator` owns a future **swap-eval**: run a role's acceptance
tests against an alternate (including open-weight) model for its tier and
report the delta, so sovereignty is *tested* — a tier swap is validated
against real acceptance criteria before it's adopted — not merely
asserted by editing `models.toml`. That swap-eval itself is not built by
this change; this change only makes the tier indirection exist and lints
it.
