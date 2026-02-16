# Fraud Detection Lakehouse on Azure Databricks

A solution architecture case study for a Tier-1 bank fraud domain.
This project shows how to move from fragmented fraud data pipelines to a governed, production-ready lakehouse with explicit control boundaries, repeatable deployment, and audit-ready evidence.

## Why This Project Exists

Fraud teams often struggle with siloed extracts, slow investigations, and weak audit traceability.
This project demonstrates a pragmatic architecture that addresses those gaps end-to-end:

- Business value: faster fraud-to-action and more trusted risk outputs.
- Architecture value: clear boundary design, ADR-backed decisions, and scalable patterns.
- Delivery value: Terraform + Databricks Asset Bundles with dev/test/prod discipline.
- Control value: governance, lineage, security, and operational evidence by design.

## Architecture Pack

The complete solution architecture document is organized in `solution_architecture/`.

| Section | Title | Link |
|---|---|---|
| 00 | Document Control | [Open](solution_architecture/00-document-control.md) |
| 01 | Executive Decision Brief | [Open](solution_architecture/01-executive-decision-brief.md) |
| 02 | Business Case | [Open](solution_architecture/02-business-case.md) |
| 03 | Architecture Vision | [Open](solution_architecture/03-architecture-vision.md) |
| 04 | Reference Architecture | [Open](solution_architecture/04-reference-architecture.md) |
| 05 | Architecture Decision Records | [Open](solution_architecture/05-architecture-decision-records.md) |
| 06 | Non-Functional Requirements | [Open](solution_architecture/06-non-functional-requirements.md) |
| 07 | Security and Control Architecture | [Open](solution_architecture/07-security-and-control-architecture.md) |
| 08 | Data Governance Model | [Open](solution_architecture/08-data-governance-model.md) |
| 09 | Operating Model | [Open](solution_architecture/09-operating-model.md) |
| 10 | Implementation Roadmap | [Open](solution_architecture/10-implementation-roadmap.md) |
| 11 | Risk and Control Register | [Open](solution_architecture/11-risk-and-control-register.md) |
| 12 | Assurance and Evidence Plan | [Open](solution_architecture/12-assurance-and-evidence-plan.md) |
| 13 | Cost and Capacity Model | [Open](solution_architecture/13-cost-and-capacity-model.md) |
| 14 | Production Readiness Checklist | [Open](solution_architecture/14-production-readiness-checklist.md) |

Detailed technical architecture views are maintained in:
- `solution_architecture/04-reference-architecture.md`
- `solution_architecture/images/`
  - `01-system-context.png`
  - `02-logical-architecture.png`
  - `deployment_view.png`
  - `03-data-architecture.png`

## How To Run

### 1. Prerequisites

- Python 3.9+ with `ruff`
- Terraform CLI
- Databricks CLI (authenticated profile)
- Bash



### 4. Validate and deploy Databricks bundle (example: dev)

```bash
cd fraud-detection-platform/databricks
databricks bundle validate --var env=dev
databricks bundle deploy --var env=dev
databricks bundle run finance_batch_eod --var env=dev
```

### 5. Validate Terraform (infra foundation)

```bash
cd fraud-detection-platform/infra/terraform
terraform fmt
terraform init -backend=false
terraform validate
```

## File Structure and Purpose

| Path | Purpose |
|---|---|
| `solution_architecture/` | Canonical template-based solution architecture pack (`00` to `14`). |
| `solution_architecture/images/` | Embedded architecture visuals used by section 04 (system context, logical, deployment, data flow). |
| `databricks/` | Databricks Asset Bundle config for pipelines/jobs and environment overlays. |
| `infra/terraform/` | Azure infrastructure as code for resource group, storage, and workspace baseline. |
| `src/` | Pipeline and SQL implementation for Bronze/Silver/Gold flow and governance logic. |

## Reader Journey (Business -> Architecture -> Production)

If you are reviewing this as a hiring manager or architecture panel:

1. Start with strategy and outcomes:
   - `solution_architecture/01-executive-decision-brief.md`
   - `solution_architecture/02-business-case.md`
   - `solution_architecture/03-architecture-vision.md`
2. Validate technical depth and design rationale:
   - `solution_architecture/04-reference-architecture.md`
   - `solution_architecture/05-architecture-decision-records.md`
   - `solution_architecture/06-non-functional-requirements.md`
3. Validate control and operating maturity:
   - `solution_architecture/07-security-and-control-architecture.md`
   - `solution_architecture/08-data-governance-model.md`
   - `solution_architecture/09-operating-model.md`
4. Validate production readiness:
   - `solution_architecture/10-implementation-roadmap.md`
   - `solution_architecture/11-risk-and-control-register.md`
   - `solution_architecture/14-production-readiness-checklist.md`


## Disclaimer

- This case study is a portfolio reconstruction based on real delivery experience in regulated financial services.
- All scenario details, architecture context, and sample data are anonymized and representative.
- Any references to clients are for industry context only and do not disclose confidential information.
- No proprietary client code, production data, credentials, secrets, tenant IDs, or workspace URLs are included.
- Artifacts are provided for demonstration of approach, decision-making, and delivery capability.

