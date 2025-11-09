# 00. Document Control (Master)

## Document Control

- Document ID: `FDP-SAD-001`
- Version: `v1.0.0`
- Status: `Draft`
- Owner: `Lead Solution Architect`
- Reviewers: `Architecture, Security, Governance, Operations`
- Classification: `Internal`
- Last Updated: `2026-02-12`
- Next Review: `2026-03-15`

### 1. Document identity

- Program / initiative: `Fraud Detection Lakehouse Modernization`
- Master document ID: `FDP-SAD-001`
- Repository path: `fraud-detection-platform/solution_architecture/README.md`
- Master status: `Draft`
- Effective date: `2026-02-12`
- Next review date: `2026-03-15`

### 2. Ownership and approvals

| Role | Name | Responsibility | Approval required (Y/N) |
|---|---|---|---|
| Document owner | Lead Solution Architect | Overall integrity and lifecycle | Y |
| Lead architect | Enterprise Data Architect | Technical correctness | Y |
| Security reviewer | Platform Security Lead | Control and risk alignment | Y |
| Governance reviewer | Data Governance Lead | Policy and stewardship alignment | Y |
| Operations reviewer | Platform Operations Lead | Operability and support readiness | N |

### 3. Section register (whole pack tracking)

| Section No. | Section Title | Project artifact path | Section Owner | Section Version | Last Updated | Status |
|---|---|---|---|---|---|---|
| 01 | Executive Decision Brief | `fraud-detection-platform/solution_architecture/01-executive-decision-brief.md` | Lead Solution Architect | v1.0 | 2026-02-12 | Draft |
| 02 | Business Case | `fraud-detection-platform/solution_architecture/02-business-case.md` | Program Sponsor + Architecture | v1.0 | 2026-02-12 | Draft |
| 03 | Architecture Vision | `fraud-detection-platform/solution_architecture/03-architecture-vision.md` | Lead Solution Architect | v1.0 | 2026-02-12 | Draft |
| 04 | Reference Architecture | `fraud-detection-platform/solution_architecture/04-reference-architecture.md` | Solution Architecture Team | v1.0 | 2026-02-12 | Draft |
| 05 | ADR(s) | `fraud-detection-platform/solution_architecture/05-architecture-decision-records.md` | Architecture Board | v1.0 | 2026-02-12 | Approved |
| 06 | NFR | `fraud-detection-platform/solution_architecture/06-non-functional-requirements.md` | Architecture + Operations | v1.0 | 2026-02-12 | Draft |
| 07 | Security and Control Architecture | `fraud-detection-platform/solution_architecture/07-security-and-control-architecture.md` | Security Architecture | v1.0 | 2026-02-12 | Draft |
| 08 | Data Governance Model | `fraud-detection-platform/solution_architecture/08-data-governance-model.md` | Data Governance | v1.0 | 2026-02-12 | Draft |
| 09 | Operating Model | `fraud-detection-platform/solution_architecture/09-operating-model.md` | Platform Operations | v1.0 | 2026-02-12 | Draft |
| 10 | Implementation Roadmap | `fraud-detection-platform/solution_architecture/10-implementation-roadmap.md` | Program Delivery | v1.0 | 2026-02-12 | Draft |
| 11 | Risk and Control Register | `fraud-detection-platform/solution_architecture/11-risk-and-control-register.md` | Risk and Control Office | v1.0 | 2026-02-12 | Draft |
| 12 | Assurance and Evidence Plan | `fraud-detection-platform/solution_architecture/12-assurance-and-evidence-plan.md` | Assurance Lead | v1.0 | 2026-02-12 | Draft |
| 13 | Cost and Capacity Model | `fraud-detection-platform/solution_architecture/13-cost-and-capacity-model.md` | FinOps + Platform | v1.0 | 2026-02-12 | Draft |
| 14 | Production Readiness Checklist | `fraud-detection-platform/solution_architecture/14-production-readiness-checklist.md` | Program Governance | v1.0 | 2026-02-12 | Draft |

### 4. Version history (master)

| Version | Date | Change summary | Files/sections affected | Author | Approved by |
|---|---|---|---|---|---|
| v1.0.0 | 2026-02-12 | Full template alignment across sections 00-14 and consolidation into canonical SAD | `fraud-detection-platform/README.md`, `fraud-detection-platform/solution_architecture/04-reference-architecture.md` | Codex | Pending governance review |
| v1.1.0 | 2026-02-12 | Moved complete template pack into `solution_architecture/` as the single documentation location | `fraud-detection-platform/solution_architecture/`, `fraud-detection-platform/README.md` | Codex | Pending governance review |

### 5. Change control rules

- Major (`X`): structural or governance-significant changes.
- Minor (`Y`): section content changes with no structural impact.
- Patch (`Z`): editorial corrections only.
- Any Approved document change requires:
  1. Updated section version in the section register.
  2. New row in the version history.
  3. Reviewer re-signoff where control impact exists.

### 6. Review checklist (per update)

- Scope and impacted sections identified.
- Traceability to ADR, requirement, or risk item recorded.
- Security and governance impact assessed.
- Evidence links updated.
- Approval records captured.
