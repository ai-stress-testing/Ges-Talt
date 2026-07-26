# SRS — <feature / system name>

**Owner**: `logicians/software-architect` · **Traces to**: `prd.md §…`
**Status**: draft | reviewed | approved · **Last validated**: YYYY-MM-DD

Software Requirements Specification. This is the **template the agency hands a
target repo**, not a filled-in artifact for Ges-Talt itself. Every requirement
below **must cite its PRD source** — a requirement with no `§n` is scope no one
authorized (`docs/traceability.md`, forward half). Every requirement must also
be verifiable (downstream half): name how it's tested.

## 1. Functional requirements

| ID | Requirement (falsifiable) | PRD source | Verified by |
|---|---|---|---|
| FR-1 | The system shall … | §n | test/verifier/metric |
| FR-2 | … | §n | … |

## 2. Non-functional requirements

| ID | Requirement | Target (measurable) | PRD source | Verified by |
|---|---|---|---|---|
| NFR-1 | Latency | p95 < 200 ms | §n | perf benchmark |
| NFR-2 | Availability | 99.9% | §n | SLO |

## 3. Performance targets

Throughput, latency, resource ceilings — each a number, not "fast". Owned
downstream by `testing/performance-benchmarker`.

## 4. Security requirements

Auth, authz, data protection, secrets. Anything critical-path here triggers
the falsifier gate (#74) and, for APIs, the `api-hardening-review` skill.

## 5. Operational constraints

Deployment, observability, rollback, capacity — what the running system must
satisfy in production (hands to `cd/sre`, `cd/release-engineer`).

## 6. Compliance requirements

Regulatory/contractual obligations that bind this feature (GDPR, PCI, WCAG,
export). Owned by `legal/*`; each maps to a control, not a promise.

## Traceability

Every row above appears in `docs/traceability.md`'s chain: PRD → **SRS** →
Design → Architecture → API/DB → impl → AC → test. This document is the SRS
link; it references the others, it does not duplicate them (SSOT).
