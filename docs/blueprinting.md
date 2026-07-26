<!-- owner: design/ux-architect · last_validated: 2026-07-26 -->
# Blueprinting — communicating system intent before implementation (#83)

Reactivates GT-20 (deferred; the triage doc conceded "nobody owns a cross-team
service blueprint"). Intent must be communicable **before** code exists. This
is the convention that says *which diagram answers which question* — one
question, one authoritative diagram (SSOT — issue #76's "answer once").

**Diagram-as-code, not binary.** Every blueprint is text-first (Mermaid,
PlantUML, DBML, or the actor/steps shape of `docs/templates/user-journey.md`)
so it is version-controlled, diffable, and reviewable in a PR. A `.drawio`/
`.fig` binary is allowed only as an *export* of a text source, never the
source itself.

## Which diagram answers which question

| Diagram | Answers | Owner | Notation |
|---|---|---|---|
| **Context** | what is inside vs outside the system; who/what it talks to | `logicians/software-architect` | Mermaid `flowchart` (C4-context) |
| **Service blueprint** | the user-facing journey mapped to the backstage services that serve each step | `design/ux-architect` | `user-journey.md` shape + swimlanes |
| **Sequence** | the order of calls for one flow across components | `backend/backend-architect` | Mermaid `sequenceDiagram` |
| **Data-flow** | where data originates, moves, is transformed, and rests | `data/data-engineer` | Mermaid `flowchart` |
| **Component relationship** | how modules/services depend on each other | `logicians/software-architect` | Mermaid `flowchart` / C4-component |
| **Dependency map** | external/internal dependencies and their direction | `backend/backend-architect` | Mermaid `flowchart` |
| **ERD** | entities, attributes, and relationships in the data model | `data/database-optimizer` | DBML / Mermaid `erDiagram` (`docs/templates/erd.md`) |

## The rule

- **One question per diagram.** If a diagram answers two, split it — a diagram
  that shows both sequence and data model is read as neither.
- **Every diagram traces up.** A blueprint cites the `prd.md §n` / SRS / ADR it
  realizes (`docs/traceability.md`), and its components appear downstream in the
  impl tasks. A diagram with no upstream purpose is decoration.
- **Blueprints precede implementation.** The `Design/Systems` exit criteria
  (issue #76) aren't met until the relevant diagrams exist.

## What this is not

- Not a mandate to diagram everything — only what a reader can't infer from the
  code. A trivial CRUD endpoint needs no sequence diagram.
- Not a new tool dependency — Mermaid renders in GitHub and in Artifacts
  natively; no binary editor is required.
