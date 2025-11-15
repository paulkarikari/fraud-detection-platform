# 07. Security and Control Architecture

### 1. Security objectives

- Protect confidentiality, integrity, and availability of regulated fraud data.
- Enforce least privilege with auditable role boundaries.
- Generate continuous control evidence for internal and external assurance.

### 2. Identity and access architecture

| Control area | Standard | Implementation pattern | Evidence |
|---|---|---|---|
| Human access | Role-based group assignments | Azure Entra ID groups mapped to Unity Catalog grants | Access review exports |
| Workload identity | Non-human identity controls | Managed identities for pipelines and service workloads | Identity inventory and assignment logs |
| Privileged access | Approval and traceability | Controlled elevation workflow with recorded approvals | Approval trail and privileged action logs |

### 3. Network and data protection model

- Network segmentation and private connectivity pattern: VNet-injected Databricks, private endpoints for storage and secrets, segmented network rules.
- Egress control approach: restricted outbound paths with approved dependencies only.
- Encryption model: TLS in transit, Azure-managed encryption at rest, and Key Vault-backed secret operations.

### 4. Segregation of duties (SoD)

| Role | Allowed actions | Prohibited actions | Review frequency |
|---|---|---|---|
| Platform admin | Infrastructure and workspace baseline control | Approving own production data access grants | Monthly |
| Data product owner | Define and publish governed data products | Granting privileged platform administration | Monthly |
| Security approver | Approve access and exception controls | Deploying unreviewed data-product code | Monthly |

### 5. Control matrix

| Control ID | Objective | Mechanism | Owner | Evidence source | Frequency |
|---|---|---|---|---|---|
| CTRL-001 | Least privilege | Unity Catalog role-based entitlements | Security Lead | Access recertification export | Monthly |
| CTRL-002 | Change accountability | CI/CD promotions with approval gates | Platform Engineering Lead | Pipeline change logs | Per release |
| CTRL-003 | Traceability | Lineage and audit logs for Bronze/Silver/Gold | Governance Lead | Lineage reports and audit logs | Weekly |
| CTRL-004 | Sensitive data protection | Masking policies and controlled access views | Data Governance Lead | Policy definitions and query audit | Weekly |

### 6. Threat scenarios and mitigations

| Threat scenario | Likelihood | Impact | Mitigation | Residual risk |
|---|---:|---:|---|---|
| Privilege misuse | M | H | SoD, approval workflow, periodic recertification | M |
| Data exfiltration | M | H | Private networking, restricted egress, monitored access | M |
| Unauthorized schema change | M | M | Contract controls and CI/CD policy checks | L |
| Silent quality degradation | M | H | Quality gates, alerts, and owner escalation | M |

### 7. Exceptions and compensating controls

- Exception: none currently approved.
- Business justification: not applicable.
- Compensating control: not applicable.
- Expiry date: not applicable.
- Approver: not applicable.

### 8. Review checklist

- Security controls are implementable through code and policy artifacts.
- Privileged actions are attributable to approved identities.
- SoD conflicts are prevented and reviewed.
