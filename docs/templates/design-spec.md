# Design Spec — <feature / surface name>

**Owner**: `design/ui-designer` (system) / `frontend/designer` (feature) ·
**Traces to**: `prd.md §…` / `user-journeys/<file>` · **Status**: draft |
reviewed | approved · **Last validated**: YYYY-MM-DD

The SSOT for UX intent (issue #76). Implementation (`frontend/react-dev`)
builds to this; a UI review checks the built surface against it. Template for
a target repo, not a filled-in artifact for this meta-repo.

## Components

Each reusable component: name, purpose, the design tokens it consumes, and the
props/variants it exposes. Reference the design system (`design/ui-designer`),
don't re-specify shared tokens here.

## States

Every component and view enumerates its states — not just the happy path:

- **Default / populated**
- **Loading**
- **Empty** — first-run and after-clearing
- **Error** — per failure mode, with the recovery affordance
- **Edge** — long strings, overflow, zero/huge counts, offline

## Behaviors

Interactions and their outcomes: what each control does, transitions between
states, focus/keyboard order, and validation timing.

## Design tokens

The tokens this surface relies on (color, spacing, type, motion). Motion
carries a reduced-motion fallback (`frontend/microanimation-engineer`).

## Interaction rules

Gestures, shortcuts, drag/drop, undo — the rules a developer can't infer from
a static mock.

## Acceptance mappings

| AC (from the issue) | Component/state that satisfies it | Verified by |
|---|---|---|
| … | … | `testing/evidence-collector` screenshot / E2E |

## Error / empty / edge-state checklist

- [ ] Every view has a designed empty state.
- [ ] Every async action has a loading and an error state.
- [ ] Every error state names its recovery path.
- [ ] Long-content / overflow / truncation is specified.
- [ ] Keyboard and screen-reader paths are specified (hands to
      `frontend/section-508-specialist` / `testing/accessibility-auditor`).
