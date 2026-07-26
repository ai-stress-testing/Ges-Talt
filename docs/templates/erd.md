# ERD — <data model / bounded context name>

**Owner**: `data/database-optimizer` · **Traces to**: `prd.md §…` / SRS ·
**Status**: draft | reviewed | approved · **Last validated**: YYYY-MM-DD

Entity-Relationship Diagram, diagram-as-code (`docs/blueprinting.md`). The
`agents/ORCHESTRATION.md` user-journey references an ERD with no artifact —
this is that artifact's template. Prefer Mermaid `erDiagram` (renders in
GitHub) or DBML.

## Diagram

```mermaid
erDiagram
    USER ||--o{ ORDER : places
    ORDER ||--|{ LINE_ITEM : contains
    PRODUCT ||--o{ LINE_ITEM : "appears in"

    USER {
        uuid id PK
        string email UK
        timestamptz created_at
    }
    ORDER {
        uuid id PK
        uuid user_id FK
        string status
        numeric total
    }
    LINE_ITEM {
        uuid id PK
        uuid order_id FK
        uuid product_id FK
        int quantity
    }
    PRODUCT {
        uuid id PK
        string sku UK
        string name
    }
```

## Entities

Per entity: purpose (one line), owning service/bounded context, and lifecycle
(who creates/deletes it).

## Relationships

Cardinality and the rule behind it (`||--o{` = one-to-many). Name the
referential-integrity behavior (cascade / restrict / set-null) — it's a
correctness decision, not a default.

## Notes

- **Normalization** reviewed (and any deliberate denormalization justified).
- **Index strategy** and **retention/deletion policy** live in the database
  design, referenced here, not duplicated (SSOT).
- Multi-tenant tables name their row-isolation model
  (`security/rls-consultant`).
