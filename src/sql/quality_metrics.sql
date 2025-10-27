-- Data quality and volume scorecard from Lakeflow metrics table.
SELECT
  metric_date,
  record_count,
  distinct_transactions,
  gross_amount
FROM finance.silver.finance_quality_metrics
ORDER BY metric_date DESC;
