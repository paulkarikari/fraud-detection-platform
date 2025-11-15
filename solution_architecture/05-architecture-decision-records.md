# 05. Architectural Decision Records (ADR)

### Metadata

| ADR ID | Title | Status | Date | Owners | Related artifacts |
|---|---|---|---|---|---|
| ADR-001 | Platform Selection (Azure Databricks Lakehouse) | Accepted | 2026-02-06 | Architecture Board | 04, 06, 07 |
| ADR-002 | Streaming vs Batch Ingestion (Hybrid) | Accepted | 2026-02-06 | Data and Platform Architecture | 04, 06, 10 |
| ADR-003 | Security and Governance Model | Accepted | 2026-02-06 | Security and Governance | 07, 08, 12 |

### 1. Context

Fraud workloads require both speed and control. The architecture must support high-volume data, auditable governance, and repeatable multi-environment deployment.

### 2. Decision drivers

- Regulatory scrutiny and audit requirements.
- Need for consistent, governed fraud data products.
- Need for repeatable and controlled release management.

### 3. Options considered

| Option | Benefits | Risks/Trade-offs | Assessment |
|---|---|---|---|
| Legacy fragmented data flows | Minimal immediate change | Control and scalability limits remain | Rejected |
| Governed Databricks lakehouse with hybrid ingestion | Unified processing and control model | Requires migration and capability build-out | Accepted |

### 4. Decision

The project adopts Azure Databricks, Delta Lake, and Unity Catalog as the core platform, with hybrid ingestion (streaming where available, batch where required) and delivery via Terraform plus Databricks Asset Bundles.

### 5. Consequences

#### Positive

- Centralized governance, traceability, and repeatable deployment.
- Faster fraud signal availability for streaming-capable sources.
- Better control posture across environments.

#### Negative

- Increased initial setup and operating discipline requirements.
- Dependency on governance operating cadence and access recertification.

#### Follow-up actions

- Maintain ADR updates for future scope expansions.
- Validate NFR and control assumptions before production go-live.
- Keep deployment and evidence pipelines aligned with control requirements.

### 6. Control and assurance impact

- Controls affected: identity, SoD, lineage, quality gates, release approvals.
- Evidence required: access review logs, change approvals, lineage reports, quality run evidence.
- Residual risk statement: residual risk is acceptable subject to active control monitoring and exception governance.

### 7. Implementation notes

- Rollout sequence: foundation -> governed onboarding -> hardening -> production cutover.
- Dependencies: identity model, source contracts, environment readiness.
- Rollback strategy: controlled rollback to prior stable bundle and data recovery via Delta history and replay.

### 8. Review trigger

- Trigger: major control model change, material risk posture change, or platform strategy change.
- Review date: 2026-06-30.
