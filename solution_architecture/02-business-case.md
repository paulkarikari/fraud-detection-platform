# 02. Business Case

### 1. Executive Summary

- Investment objective: Replace fragmented fraud analytics data flows with a governed, auditable, and repeatable platform.
- Strategic outcome: Faster and more defensible fraud operations and regulatory reporting.
- Requested decision: Proceed.

### 2. Context and Drivers

- Business drivers: Improve investigation speed, reduce manual reconciliation, lower avoidable platform cost, and improve trust in fraud and risk outputs.
- Regulatory/control drivers: Enforce least privilege, retention, lineage, and change accountability for regulated banking data.

### 3. Scope

#### In Scope

- Batch and streaming ingestion for card, payment, and digital channel events.
- Medallion model (Bronze/Silver/Gold) with Delta Lake on Azure Databricks.
- Unity Catalog governance, masking, lineage, and access controls.
- Environment-separated delivery with Terraform and Databricks Asset Bundles.

#### Out of Scope

- Refactoring upstream core banking transaction engines.
- Real-time customer decisioning in front-office channels.
- BI platform replacement.

### 4. Benefits

| Benefit | Type (Revenue/Cost/Risk/Control) | Baseline | Target | Owner |
|---|---|---:|---:|---|
| Reduced investigation delay for priority fraud events | Risk/Control | 4-12 hours triage lag | < 60 minutes for priority streaming events | Fraud Operations Lead |
| Reduced manual reconciliation effort | Cost/Control | 20+ analyst hours/week | < 6 analyst hours/week | Data Product Owner |
| Improved audit traceability | Control | Partial lineage and change evidence | 100% lineage for Gold fraud outputs and release evidence | Governance Lead |
| Better production stability | Risk/Cost | Unplanned reruns and ad hoc fixes | > 99.5% on-time critical pipeline completion | Platform Operations Lead |

### 5. Cost and Investment

| Cost component | Year 1 | Year 2 | Notes |
|---|---:|---:|---|
| Platform (Databricks + storage + observability) | USD 420,000 | USD 500,000 | Includes growth and resilience overhead |
| Delivery (engineering + architecture + governance) | USD 780,000 | USD 390,000 | Higher spend in initial modernization year |
| Assurance and control operations | USD 120,000 | USD 140,000 | Access recertification, audits, control testing |
| Total | USD 1,320,000 | USD 1,030,000 | Subject to quarterly reforecast |

### 6. Risks and Dependencies

| Risk/Dependency | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Source schema volatility | M | H | Contract baselines and schema drift gates | Data Engineering Lead |
| Identity model delays | M | H | Early security design checkpoint and explicit ownership | Security Lead |
| Environment readiness lag | M | M | IaC-first provisioning and gated release path | Platform Engineering Lead |
| Operating model adoption gap | M | M | Defined RACI, runbook drills, and KPI review cadence | Operations Lead |

### 7. Timeline and Milestones

| Milestone | Target date | Outcome |
|---|---|---|
| Phase 1 foundation complete | 2025-10-31 | Core platform, governance baseline, initial ingestion controls |
| Phase 2 governed onboarding complete | 2025-11-20 | Fraud domain data products and quality gates in non-prod |
| Phase 3 hardening complete | 2025-11-26 | Security, resilience, and readiness criteria met for production |
| Production go-live decision | 2025-11-28 | Go/no-go based on readiness checklist and risk posture |

### 8. Recommendation and Ask

- Recommendation: Proceed with Option B under phased governance gates.
- Funding ask: Approve two-year envelope with quarterly FinOps and architecture review.
- Governance ask: Approve section 03 through section 14 control model and operating ownership.
