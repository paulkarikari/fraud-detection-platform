-- Gold data product contract: daily finance KPI summary.
CREATE OR REPLACE TABLE finance.gold.finance_daily_summary AS
SELECT
  TO_DATE(event_ts) AS transaction_date,
  currency,
  COUNT(DISTINCT transaction_id) AS transaction_count,
  SUM(amount) AS total_amount,
  AVG(amount) AS avg_amount
FROM finance.silver.finance_transactions_silver_stream
GROUP BY TO_DATE(event_ts), currency;
