-- Gold data product contract: account-level transaction history.
CREATE OR REPLACE TABLE finance.gold.account_transaction_history AS
SELECT
  transaction_id,
  account_id,
  counterparty_account_id,
  event_type,
  event_ts,
  amount,
  currency,
  payment_channel,
  source_system
FROM finance.silver.finance_transactions_silver_stream;
