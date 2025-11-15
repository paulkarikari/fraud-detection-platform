# 06. Non-Functional Requirements (NFR)

### 1. Service tier classification

- Tier: Mission critical.
- Rationale: platform supports fraud operations and regulated reporting workloads with high control expectations.

### 2. NFR matrix

| NFR area | Requirement | Metric | Target | Validation method | Owner |
|---|---|---|---|---|---|
| Availability | Critical fraud pipelines must run reliably in production windows | Uptime / on-time completion | >= 99.5% | Job telemetry and monthly SLO report | Platform Operations Lead |
| Recovery | Recover from failure with bounded data loss and time | RTO/RPO | RTO <= 60 min, RPO <= 15 min for streaming checkpoints | Recovery drills and incident records | Operations + Data Engineering |
| Performance | Deliver fraud outputs within decision windows | Pipeline latency | < 30 min (streaming paths), < 4 hours (batch paths) | Runtime dashboards and synthetic tests | Data Engineering Lead |
| Scalability | Support event surges during peak transaction periods | Peak throughput | 3x baseline sustained peak without breach | Stress and replay testing | Platform Engineering Lead |
| Security | Prevent critical findings in production posture | Critical findings | 0 unresolved critical findings | Security validation and review logs | Security Lead |
| Auditability | Ensure full traceability of critical changes and outputs | Traceable critical changes | 100% | Audit sample and evidence pack review | Governance Lead |

### 3. Workload profiles

| Workload type | Daily volume | Peak factor | Processing window |
|---|---:|---:|---|
| Batch transaction ingestion | 120M records/day | 1.8x | Hourly + EOD |
| Streaming fraud signal enrichment | 2.5K events/sec | 3.0x | Near-real-time |
| Gold fraud reporting product refresh | 24 scheduled runs/day | 1.5x | 15-60 minutes per run |

### 4. Test and evidence plan

- Test environments: dev for engineering validation, test for integration and pre-production readiness.
- Test scenarios: throughput, failure/recovery, schema drift, access control, and deployment rollback.
- Evidence artifacts and storage location: release logs, run outputs, quality reports, and access evidence stored in project-controlled assurance paths.

### 5. Exception handling

If a target cannot be met:

- Compensating controls: temporary manual review, tighter release gate, or reduced scope.
- Risk owner: accountable domain or platform owner.
- Expiry date: mandatory review date set by governance forum.

### 6. Sign-off

- Architecture: Pending.
- Security: Pending.
- Operations: Pending.
- Business owner: Pending.
