# Data Team

Owns the pipelines, storage, and data quality that everything else reads
from - distinct from `backend/` (which owns the services that call into
this data) and `ai/` (which owns the models that consume it).

- [`data-engineer/`](data-engineer/) - ETL/ELT pipelines, medallion
  lakehouse architecture, streaming ingestion, data contracts.
- [`database-optimizer/`](database-optimizer/) - operational database
  schema, indexing, and query performance.
- [`database-administrator/`](database-administrator/) - operational
  database availability and recoverability: replication/failover, backup
  and point-in-time recovery, connection pooling, schema-change safety.
- [`ai-data-remediation-engineer/`](ai-data-remediation-engineer/) -
  surgical, pattern-level fixes for data broken at scale, via local SLMs.

Same `agent.md` + `SPEC.md` convention as every other team in this repo. Add
a role here when it owns a durable subclass of data-infrastructure work.
