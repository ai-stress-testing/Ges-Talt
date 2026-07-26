<!-- owner: pm/team-operations · last_validated: 2026-07-26 -->
# Doc metadata + staleness (#89)

Freshness is machine-checked for **generated** files (INDEX, repo-map,
personas — `index_in_sync`, `repo_map_fresh`, `personas_installed`). It was
**not** checked for **hand-authored** docs, so a convention could rot silently
while claiming to be current. Issue #77's "context improves over time, not
stale" was only half-realized. This closes the other half.

## The convention

An authored governance/convention doc carries an HTML-comment marker on its
first line:

```
<!-- owner: <team/role> · last_validated: YYYY-MM-DD -->
```

- **owner** — the `team/role` accountable for the doc's accuracy (a real
  roster role).
- **last_validated** — the date someone last confirmed the doc still matches
  reality. Re-validating = re-reading and bumping the date, not necessarily
  editing.

## What is governed vs exempt

- **Governed** (must carry the marker, must stay fresh): the convention/policy
  docs that steer behavior — `docs/traceability.md`, `docs/blueprinting.md`,
  `docs/prioritization.md`, `docs/definition-of-done.md`,
  `docs/testing-tiers.md`, `docs/risk-register.md`, `docs/accountability.md`,
  `docs/for-ai-agents.md`, `docs/doc-metadata.md`, `docs/model-tiers.md`.
- **Exempt** (no marker; already covered or immutable):
  - **Generated files** — freshness is already verified another way; a second
    marker would double-cover and drift.
  - **Sprint-log entries** — immutable history; a log of what happened on a
    date is never "stale."
  - **Templates** — carry their own `Last validated` field *inside* the
    template body for the target repo to fill; they're not governed as live
    docs of this repo.

## The verifier

`scripts/verifiers/doc_freshness.py` (GT-43 style, fail-closed):

- FAILs if a **governed** doc lacks the marker.
- FAILs if any doc **carrying** the marker has a malformed date or one older
  than the **staleness horizon (180 days)**.
- PASSes when every governed doc is present and fresh; never SKIPs silently on
  an empty set (an empty governed set is itself a FAIL — the guard against a
  glob that matches nothing).

Re-validating a doc is a one-line date bump; the verifier turns "is this doc
still true?" from a hope into a gate.
