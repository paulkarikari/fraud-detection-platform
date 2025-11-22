# 14. Production Readiness Checklist

### 1. Architecture readiness

| Check | Evidence | Owner | Status |
|---|---|---|---|
| Reference architecture approved | `fraud-detection-platform/solution_architecture/04-reference-architecture.md` | Lead Architect | Pass |
| ADRs for major decisions finalized | `fraud-detection-platform/solution_architecture/05-architecture-decision-records.md` | Architecture Board | Pass |
| NFR targets validated | Section 06 + test evidence package | Architecture + Operations | Conditional |

### 2. Security and control readiness

| Check | Evidence | Owner | Status |
|---|---|---|---|
| Least privilege model implemented | `fraud-detection-platform/solution_architecture/07-security-and-control-architecture.md` | Security Lead | Pass |
| SoD conflicts reviewed | Monthly access review records | Security + Governance | Conditional |
| Control evidence pipeline active | Section 12 evidence catalog process | Assurance Lead | Conditional |

### 3. Data governance readiness

| Check | Evidence | Owner | Status |
|---|---|---|---|
| Domain ownership assigned | Section 08 domain ownership table | Governance Lead | Pass |
| Classification and retention policies applied | Section 08 policy mapping | Governance Lead | Conditional |
| Lineage and quality checks active | Quality and lineage run evidence | Data Product Owner | Pass |

### 4. Operations readiness

| Check | Evidence | Owner | Status |
|---|---|---|---|
| Monitoring and alerting validated | `fraud-detection-platform/solution_architecture/09-operating-model.md` | Operations Lead | Pass |
| Incident runbooks tested | `fraud-detection-platform/solution_architecture/09-operating-model.md` + drill logs | Operations Lead | Conditional |
| Rollback and recovery drill completed | `fraud-detection-platform/solution_architecture/09-operating-model.md` + drill evidence | Platform Operations Lead | Conditional |

### 5. Assurance readiness

| Check | Evidence | Owner | Status |
|---|---|---|---|
| Risk and control register updated | Section 11 register | Risk and Control Office | Pass |
| Assurance evidence package complete | Section 12 package checklist | Assurance Lead | Conditional |
| Open critical risks accepted or mitigated | Risk review minutes and approvals | Governance Forum | Conditional |

### 6. Go-live conditions and actions

#### Open issues

- Complete full production-scale DR drill and capture evidence (`Owner: Operations Lead, Due: 2026-09-15`).
- Close remaining conditional SoD evidence automation action (`Owner: Security Lead, Due: 2026-08-31`).
- Finalize retention policy legal hold test evidence (`Owner: Governance Lead, Due: 2026-09-30`).

#### Go/no-go recommendation

- Recommendation: Conditional go, subject to closure of open issues above.
- Conditions (if any): all conditional checks must be moved to pass before cutover approval.
- Approval authority: Program steering group with architecture and security sign-off.

### 7. Sign-offs

- Architecture: Pending final checkpoint.
- Security: Pending final checkpoint.
- Operations: Pending final checkpoint.
- Governance: Pending final checkpoint.
- Business owner: Pending final checkpoint.
