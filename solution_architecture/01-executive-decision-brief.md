# 01. Executive Decision Brief

### 1. Decision Required

- Decision: Approve phased delivery of a governed fraud detection lakehouse on Azure Databricks.
- Approval body: Program sponsor, architecture board, security and risk forum.
- Decision date: 2026-02-19.

### 2. Problem Summary

- Current issue: Fraud analysts, risk teams, and compliance users depend on inconsistent extracts from siloed card, payment, and digital systems. This drives reconciliation overhead, slower investigations, and reduced trust in reported outputs.
- Impact if unresolved: Increased fraud-to-action latency, higher regulatory and audit exposure, recurring manual effort, and avoidable operating cost.

### 3. Options Considered

| Option | Summary | Benefits | Risks/Trade-offs | Recommendation |
|---|---|---|---|---|
| A | Continue with current fragmented pipelines and manual reconciliation | No near-term delivery disruption | Control gaps persist, investigation speed remains poor, higher long-term cost | No |
| B | Implement governed lakehouse on Azure Databricks with Unity Catalog, Terraform, and Databricks Asset Bundles | Unified data products, lineage, policy enforcement, repeatable release process | Requires platform migration effort and operating model adoption | Yes |
| C | Partial modernization (reporting-only layer without full governance and CI/CD controls) | Lower initial effort | Defers core control and operability issues, increases redesign risk later | No |

### 4. Recommendation

- Recommended option: Option B.
- Why now: Fraud pressure and regulatory expectations are increasing while current controls are not scalable.
- Why this option: It delivers measurable control improvement, operational repeatability, and faster trusted analytics with clear audit traceability.

### 5. Funding and Approval Ask

- Funding ask: Approve the two-year delivery and run envelope described in Section 13.
- Resource ask: Architecture, data engineering, platform engineering, governance, security, and operations.
- Approval ask: Approve architecture scope, control boundaries, and phased production rollout.

### 6. Success Metrics

- Fraud data product refresh latency: `T+1 / ad hoc` -> `<30 minutes for streaming-capable flows, <4 hours for batch flows`.
- Critical data quality exceptions in Gold: `manual, inconsistent reporting` -> `<= 2 unresolved critical issues per month`.
- Traceable production changes with approval evidence: `<60%` -> `100%`.

### 7. Risks and Controls (Top 3)

- Data quality drift -> Silver quality gates, contract checks, and quarantine workflows.
- Unauthorized access -> Unity Catalog role model, access recertification, and SoD controls.
- Pipeline instability for near-real-time fraud feeds -> checkpointing, retries, and monitored runbooks.

### 8. Next Steps

1. Finalize approval of control boundary model and operating ownership.
2. Execute Phase 1 foundation with evidence generation enabled from day one.
3. Gate promotion to production on Section 14 readiness outcomes.
