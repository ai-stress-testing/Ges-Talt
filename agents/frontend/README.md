# Frontend Team

Owns everything the user's browser/app renders and interacts with. This is
the reference example for **nested roles under one team**:

- [`designer/`](designer/) — UI/UX design intent: layout, interaction,
  accessibility. Produces specs, not code.
- [`react-dev/`](react-dev/) — implementation in React against those specs.
- [`desktop-app-engineer/`](desktop-app-engineer/) — Electron/Tauri desktop
  packaging, IPC security, code signing, and auto-update pipelines.
- [`microanimation-engineer/`](microanimation-engineer/) — motion specs for
  UI micro-interactions: duration, easing, trigger, reduced-motion fallback.
- [`section-508-specialist/`](section-508-specialist/) — accessibility
  audit and remediation against Section 508 / ADA Title II / WCAG AA.

Add more roles the same way — one folder per role, same `agent.md` +
`SPEC.md` convention as everywhere else in this repo. A role doesn't need a
reason to exist beyond "this team now owns a subclass of work distinct
enough to deserve its own persona."
