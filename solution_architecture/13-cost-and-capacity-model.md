# 13. Cost and Capacity Model

### 1. Modeling assumptions

- Workload growth assumptions: 25% year-over-year data volume growth and 15% growth in fraud detection workloads.
- Data growth assumptions: retained governed data grows from 80 TB to 125 TB over two years.
- Utilization assumptions: production compute utilization target of 65-75% under autoscale policies.
- Pricing assumptions and date: indicative Azure and Databricks pricing baseline dated 2026-02-12.

### 2. Workload profile

| Workload | Pattern | Baseline usage | Peak usage | Growth rate |
|---|---|---:|---:|---:|
| Bronze ingestion pipelines | Batch + streaming | 9,000 DBU/month | 14,000 DBU/month | 20% |
| Silver conformance and quality jobs | Batch | 6,000 DBU/month | 9,000 DBU/month | 18% |
| Gold serving and reporting refresh | Batch + interactive | 4,000 DBU/month | 6,500 DBU/month | 15% |

### 3. Cost model by environment

| Environment | Compute | Storage | Network | Other | Monthly total |
|---|---:|---:|---:|---:|---:|
| Dev | USD 18,000 | USD 4,500 | USD 1,200 | USD 2,300 | USD 26,000 |
| Test | USD 24,000 | USD 6,500 | USD 1,500 | USD 3,000 | USD 35,000 |
| Prod | USD 55,000 | USD 13,000 | USD 3,500 | USD 6,500 | USD 78,000 |

### 4. Unit economics

| Unit metric | Formula | Baseline | Target |
|---|---|---:|---:|
| Cost per pipeline run | Monthly environment cost / number of production-equivalent runs | USD 95 | <= USD 80 |
| Cost per TB processed | Monthly compute + storage / TB processed | USD 1,050 | <= USD 900 |

### 5. Capacity thresholds

| Resource area | Threshold | Trigger action | Owner |
|---|---|---|---|
| Streaming compute pool | Sustained > 80% utilization for 3 days | Scale policy tuning and workload rebalance | Platform Engineering Lead |
| Storage growth | > 10% monthly growth for 2 consecutive months | Retention and archival policy review | Governance + FinOps |
| Job queue time | Critical jobs waiting > 10 minutes | Priority policy update and capacity adjustment | Operations Lead |

### 6. Optimization levers

- Workload scheduling and autoscale tuning.
- Storage lifecycle tiering and retention enforcement.
- Query and pipeline performance optimization with Delta best practices.

### 7. Governance cadence

- Weekly: spend anomaly review.
- Monthly: unit economics and optimization review.
- Quarterly: reforecast and capacity planning update.
