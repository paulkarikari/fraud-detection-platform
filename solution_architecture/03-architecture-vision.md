# 03. Architecture Vision

### 1. Executive summary

This platform establishes a governed fraud analytics and monitoring foundation on Azure Databricks for a regulated banking context. It standardizes data flow from source systems to contract-grade Gold products while enforcing control boundaries for identity, network, and policy. The architecture is designed for repeatable releases across dev, test, and prod, with traceable evidence for security, risk, and audit stakeholders. It prioritizes operational reliability, explicit ownership, and control automation over ad hoc delivery.

### 2. Problem statement

- Current-state limitations: fragmented data pipelines, inconsistent quality controls, weak lineage visibility, and non-repeatable deployment patterns.
- Business and regulatory impact: delayed fraud investigation, inconsistent risk reporting, and high audit response effort.
- Consequences of no change: higher fraud exposure, recurring compliance risk, and sustained operational inefficiency.

### 3. Desired outcomes and success criteria

| Outcome | Metric | Baseline | Target | Owner |
|---|---|---:|---:|---|
| Faster workload onboarding | Time to onboard new fraud data domain | 8-10 weeks | 3-4 weeks | Platform Engineering Lead |
| Improved control posture | Open critical control exceptions | 6 | <= 1 | Governance Lead |
| Higher reliability | On-time critical jobs | 94% | >= 99.5% | Operations Lead |

### 4. Scope

#### In scope

- Fraud domain pipelines and data products across batch and streaming patterns.
- Dev, test, and prod environments with isolated boundaries.
- Integration with source systems, governance controls, and downstream analytics consumers.

#### Out of scope

- Upstream source platform redesign.
- Cross-bank enterprise model replacement beyond fraud domain in this release.
- Real-time customer decision engine deployment.

### 5. Architectural stances

- Governance is architectural, not post-implementation.
- Control plane and data plane boundaries are explicit.
- Least privilege and traceability are default conditions.
- Gold datasets are product contracts, not unmanaged extracts.
- Deployments are repeatable, environment-aware, and evidence-producing.

### 6. Constraints and assumptions

#### Constraints

- Regulatory constraints: auditable lineage, policy-based retention, and access accountability for regulated data.
- Enterprise constraints: Azure Entra ID, private networking, no secret material in source control, and IaC-first provisioning.

#### Assumptions

- Source systems provide stable transaction identifiers and acceptable data freshness.
- Compliance stakeholders provide retention and classification policy decisions before production cutover.
- Platform teams own operating KPIs and evidence generation as part of run operations.

### 7. Stakeholders and decision forums

| Stakeholder group | Interest | Decision rights | Engagement cadence |
|---|---|---|---|
| Architecture board | Design integrity and target-state coherence | Approve target architecture and ADRs | Fortnightly |
| Security and risk forum | Control adequacy and residual risk | Approve control model and exceptions | Weekly |
| Platform operations review | Operability and support readiness | Approve run model and incident posture | Weekly |
| Program steering group | Delivery outcomes and funding | Approve roadmap, release, and cutover decisions | Monthly |

### 8. Risks and dependencies (summary)

- Top risks: schema drift, over-privileged access, and pipeline failure during high-volume windows.
- Top dependencies: source data contract alignment, identity group model readiness, and non-prod/prod environment parity.

### 9. Decision requests

- Approve target architecture scope.
- Approve identity, network, and governance control boundary model.
- Approve phased roadmap and production gate criteria.

### 10. Next artifacts

- `fraud-detection-platform/solution_architecture/04-reference-architecture.md`
- `fraud-detection-platform/solution_architecture/05-architecture-decision-records.md`
- `fraud-detection-platform/solution_architecture/06-non-functional-requirements.md`
- `fraud-detection-platform/solution_architecture/07-security-and-control-architecture.md`
