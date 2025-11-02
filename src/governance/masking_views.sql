-- Dynamic masking view for sensitive account identifiers.
CREATE OR REPLACE VIEW finance.gold.vw_account_transaction_history_secure AS
SELECT
  transaction_id,
  CASE
    WHEN is_account_group_member('pii_access') THEN account_id
    ELSE CONCAT('MASKED-', RIGHT(account_id, 4))
  END AS account_id,
  event_type,
  event_ts,
  amount,
  currency,
  payment_channel,
  source_system
FROM finance.gold.account_transaction_history;
