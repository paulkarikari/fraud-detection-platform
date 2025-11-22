# 12. Assurance and Evidence Plan

### 1. Assurance scope

- Regulatory controls in scope: lineage, least privilege, retention, and change accountability controls.
- Internal policy controls in scope: SoD, release approvals, quality gates, and incident management evidence.
- Critical data products in scope: Gold fraud transaction history, fraud alert feed, and regulatory fraud extracts.

### 2. Evidence catalog

| Control ID | Evidence artifact | Source system | Collection method | Frequency | Owner | Retention | Storage location |
|---|---|---|---|---|---|---|---|
| CTRL-001 | Access recertification report | Identity and Unity Catalog | Automated export | Monthly | Security Lead | 7 years | Controlled assurance repository |
| CTRL-002 | Change approval log | CI/CD platform | Automated export | Per release | Platform Engineering Lead | 7 years | Controlled assurance repository |
| CTRL-003 | Lineage coverage report | Unity Catalog lineage | Automated report | Weekly | Governance Lead | 7 years | Controlled assurance repository |
| CTRL-004 | Data quality gate results | Pipeline runtime | Automated export | Daily | Data Product Owner | 7 years | Controlled assurance repository |
| CTRL-005 | Incident and recovery evidence | Incident management + runbook records | Semi-automated capture | Per incident | Operations Lead | 7 years | Controlled assurance repository |

### 3. Evidence quality standards

- Completeness: all required fields and metadata present.
- Timeliness: evidence generated within defined cadence.
- Traceability: each artifact linked to control ID, owner, and time window.

### 4. Assurance calendar

| Cycle | Activity | Output | Owner |
|---|---|---|---|
| Weekly | Control operations and exception triage | Updated exception log | Governance Lead |
| Monthly | Control health review | Assurance scorecard and remediation tracker | Security and Governance Leads |
| Quarterly | Deep control testing | Assurance summary and risk posture update | Assurance Lead |

### 5. Sampling and testing strategy

- Sampling approach: risk-based sampling prioritizing Tier 1 data products and privileged changes.
- Sample size guidance: at least 10% of monthly production changes and 100% of P1 incidents.
- Failure handling and escalation: failed sample triggers corrective action and forum escalation.

### 6. Exceptions

No active exceptions at this stage. Any future exception requires documented compensating controls, expiry date, and approver.

### 7. Evidence package checklist

- Control matrix snapshot.
- Access and entitlement evidence.
- Change and deployment evidence.
- Lineage and data quality evidence.
- Incident and runbook evidence.
