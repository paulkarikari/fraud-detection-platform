# 11. Risk and Control Register

### 1. Scoring model

- Likelihood: `1-5`
- Impact: `1-5`
- Inherent risk score: `Likelihood x Impact`
- Residual risk score: post-control score

### 2. Register

| Risk ID | Risk statement | Inherent score | Existing controls | Control owner | Residual score | Action plan | Due date | Status |
|---|---|---:|---|---|---:|---|---|---|
| R-001 | Pipeline failures delay fraud alert availability | 16 | Checkpointing, retries, dashboard alerting | Operations Lead | 8 | Run quarterly resilience drills and tune retry policies | 2025-11-07 | Open |
| R-002 | Data quality drift leads to incorrect fraud outputs | 15 | Silver quality gates and contract checks | Data Product Owner | 7 | Expand schema drift tests and block-on-fail policy | 2025-10-31 | Open |
| R-003 | Unauthorized access to confidential data | 12 | Unity Catalog RBAC, monthly recertification | Security Lead | 6 | Automate entitlement evidence and stale-access revocation | 2025-11-10 | Open |
| R-004 | Cost overrun in high-volume periods | 12 | Auto-scaling, auto-termination, spend monitoring | FinOps Lead | 7 | Introduce workload-level budget guardrails | 2025-11-14 | Open |
| R-005 | Incomplete lineage for regulated reports | 16 | Lineage enabled on curated layers | Governance Lead | 8 | Extend lineage checks to all critical report paths | 2025-11-18 | Open |

### 3. Governance and escalation

- Review cadence: weekly operational risk review and monthly governance review.
- Escalation threshold: residual score >= 12.
- Escalation forum: security and risk forum plus architecture board.

### 4. Closure criteria

A risk can be closed only when:

- Action plan is completed.
- Evidence is attached.
- Residual risk acceptance is approved by accountable owner.
