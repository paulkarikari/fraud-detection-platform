# 08. Data Governance Model

### 1. Governance objectives

- Define ownership and stewardship for governed fraud data products.
- Enforce policy-aligned access, quality, and lifecycle controls.
- Maintain lineage evidence for critical outputs.

### 2. Domain and ownership model

| Domain | Business owner | Technical owner | Steward | Criticality |
|---|---|---|---|---|
| Fraud transactions | Fraud Operations Lead | Data Engineering Lead | Data Steward (Fraud) | Tier 1 |
| Fraud alerts and cases | Risk and Fraud Lead | Data Product Owner | Data Steward (Risk) | Tier 1 |
| Regulatory fraud reporting | Compliance Reporting Lead | Analytics Engineering Lead | Governance Steward | Tier 1 |

### 3. Data classification policy mapping

| Classification | Access policy | Handling controls | Retention policy |
|---|---|---|---|
| Public | Open within enterprise guidance | Standard controls | As per enterprise policy |
| Internal | Business group access | Baseline logging and monitoring | 3 years |
| Confidential | Approved role-based access | Masking, approval workflow, restricted extracts | 7 years |
| Restricted | Named access with explicit approvals | Enhanced monitoring, strict SoD, controlled usage | 7 years or legal hold |

### 4. Catalog and namespace design

- Catalog strategy: domain-aligned catalogs with environment isolation.
- Schema strategy: Bronze, Silver, and Gold schemas per domain and environment.
- Naming standard: consistent domain-first naming with environment context.
- Ownership metadata standard: each governed asset stores owner, steward, and classification metadata.

### 5. Access control model

- Entitlement model: role-based model anchored in Azure Entra ID groups and Unity Catalog grants.
- Access request and approval workflow: request -> business owner approval -> governance validation -> implementation.
- Recertification cadence and owner: monthly recertification led by governance and security owners.

### 6. Data quality policy

| Data product | Critical checks | Threshold | Failure action | Owner |
|---|---|---|---|---|
| Gold fraud transaction history | Completeness, uniqueness, key validity | >= 99.9% pass | Block publication and open incident | Data Product Owner |
| Gold fraud alert feed | Latency, duplicate rate, schema conformance | <= 30 min latency, <= 0.1% duplicates | Alert + controlled replay | Data Engineering Lead |
| Regulatory fraud extract | Reconciliation and lineage completeness | 100% traceable source mapping | Block release to consumers | Governance Lead |

### 7. Lineage and traceability requirements

- Mandatory lineage scope: all regulated Gold outputs and critical Silver transformations.
- Lineage evidence generation cadence: weekly baseline plus per-release verification.
- Escalation path for lineage gaps: data owner -> governance lead -> architecture board.

### 8. Lifecycle and retention controls

- Archival policy: aged data archived to approved lower-cost tier with metadata preservation.
- Deletion policy: policy-driven deletion with approval and evidence logging.
- Legal hold handling: legal hold policy overrides standard deletion controls.

### 9. Governance operating cadence

- Weekly: quality and lineage operations review.
- Monthly: access recertification and control performance review.
- Quarterly: policy and ownership revalidation.
