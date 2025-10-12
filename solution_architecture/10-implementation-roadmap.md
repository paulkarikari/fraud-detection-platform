# 10. Implementation Roadmap

### 1. Roadmap approach

- Delivery strategy: hybrid (capability-first foundation, then domain onboarding).
- Release cadence: two-week sprints and monthly governed release windows.

### 2. Phase plan

| Phase | Objectives | Key deliverables | Exit criteria | Target window |
|---|---|---|---|---|
| Phase 1 | Foundation | IaC baseline, environment model, identity boundary, Bronze ingestion baseline, observability baseline | Non-prod controls active, initial evidence pipeline running | 2025-10-01 to 2025-10-31 |
| Phase 2 | Governed onboarding | Silver conformance, Gold fraud products, quality policy enforcement, access workflows | Business validation complete, quality gates operational | 2025-10-16 to 2025-11-20 |
| Phase 3 | Scale and harden | Resilience drills, cost controls, security hardening, production readiness | Section 14 checks pass and open critical risks resolved | 2025-11-01 to 2025-11-28 |

### 3. Dependency map

| Dependency | Type | Owner | Needed by | Risk if late |
|---|---|---|---|---|
| Source data contract alignment | External | Source system owners | Phase 2 | Delays onboarding and quality stabilization |
| Identity group and approval model | Internal | Security Lead | Phase 1 | Blocks least privilege implementation |
| Test/prod environment parity | Internal | Platform Engineering Lead | Phase 2/3 | Higher release and rollback risk |
| Operations staffing for 24x7 critical response | Internal | Operations Lead | Phase 3 | Go-live support risk |

### 4. Risk-informed sequencing

- Derisk first: identity boundaries, governance controls, and release evidence pathways.
- Intentionally deferred: non-critical domain expansion until fraud-domain controls and reliability are stable.

### 5. Resource and capability plan

| Capability | Required role(s) | Availability assumption | Gap action |
|---|---|---|---|
| Platform foundation and IaC | Platform engineers, cloud architect | 2 platform engineers available full-time | Backfill with contract support if delayed |
| Data product delivery | Data engineers, analytics engineer | 3 engineers across phases 1-2 | Stage scope by product priority |
| Governance and assurance | Governance lead, security analyst | Shared governance capacity | Reserve dedicated governance sprint capacity |
| Operations readiness | SRE/operations engineers | On-call coverage by phase 3 | Train and certify additional on-call staff |

### 6. Governance checkpoints

- Architecture checkpoint: end of phase 1 and phase 2.
- Security and control checkpoint: pre-production hardening and before go/no-go.
- Production readiness checkpoint: final gate before production decision.

### 7. Example milestone narrative

Phase 1 establishes control boundaries, baseline identity and network model, and CI/CD control evidence flow. Business-critical Gold outputs are not promoted until phase 2 quality and governance controls are proven.
