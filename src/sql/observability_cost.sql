-- Cost and observability baseline using Databricks system tables.
SELECT
  u.usage_metadata.workspace_id,
  u.usage_metadata.job_id,
  u.sku_name,
  u.usage_date,
  SUM(u.usage_quantity) AS dbus,
  SUM(u.usage_quantity * pricing.default) AS estimated_cost
FROM system.billing.usage AS u
LEFT JOIN system.billing.list_prices AS pricing
  ON u.sku_name = pricing.sku_name
 AND u.usage_start_time >= pricing.price_start_time
 AND (u.usage_end_time <= pricing.price_end_time OR pricing.price_end_time IS NULL)
GROUP BY u.usage_metadata.workspace_id, u.usage_metadata.job_id, u.sku_name, u.usage_date;
