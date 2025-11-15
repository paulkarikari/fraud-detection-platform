# 09. Operating Model

### 1. Operating model purpose

Define how the fraud lakehouse is run, supported, and improved while maintaining control and reliability.

### 2. Service model

| Service | Description | SLA/SLO | Owner | Support hours |
|---|---|---|---|---|
| Domain onboarding | Onboard new fraud datasets and contracts | New domain ready in <= 4 weeks once prerequisites are met | Platform + Data Product Leads | Business hours + planned releases |
| Data access workflows | Controlled request and approval for governed data access | 95% requests resolved within 2 business days | Governance Lead | Business hours |
| Incident response | Detect, triage, recover, and evidence incidents | P1 acknowledge <= 15 min, restore <= 60 min | Operations Lead | 24x7 for P1/P2 |

### 3. Team boundaries and RACI

| Capability | Platform team | Data product team | Security/Risk | Operations |
|---|---|---|---|---|
| Identity and access | R | C | A | C |
| Pipeline deployment | C | A/R | C | C |
| Incident management | C | R | C | A/R |
| Quality policy enforcement | C | A/R | C | R |
| Control evidence operations | C | R | A | R |

### 4. Change and release process

- Standard change flow: develop -> automated tests -> non-prod deploy -> control checks -> approval -> production deploy.
- Emergency change flow: incident-based expedited path with mandatory post-change review.
- Approval points: architecture and security checkpoints before production.
- Rollback criteria: failed NFR/control gates or adverse production impact.

### 5. Incident management model

- Severity definitions: P1 critical service/business impact, P2 degraded critical path, P3 non-critical issue.
- Escalation matrix: on-call operations -> platform/data owners -> governance/security as required.
- Communication protocol: incident bridge for P1/P2, status updates at defined intervals.
- Post-incident review requirement: root cause and corrective action completed within 5 business days.

### 6. Runbook standards

- Minimum runbook sections: detection, triage, containment, recovery, evidence capture, escalation.
- Ownership and review cadence: owner assigned per runbook, reviewed monthly.
- Testing and drill frequency: quarterly recovery drills and scenario exercises.

### 7. Operating KPIs

| KPI | Definition | Target | Source | Review cadence |
|---|---|---|---|---|
| On-time critical jobs | Percent of critical jobs meeting schedule | >= 99.5% | Job telemetry | Weekly |
| Mean time to recover | Average incident recovery duration for P1/P2 | <= 60 min for P1 | Incident management records | Weekly |
| Change failure rate | Percent of production changes requiring rollback or hotfix | <= 5% | CI/CD and change records | Monthly |

### 8. Improvement backlog

- Automate monthly recertification evidence publication.
- Expand synthetic data quality probes for early detection.
- Standardize rollback playbooks across all critical pipelines.
