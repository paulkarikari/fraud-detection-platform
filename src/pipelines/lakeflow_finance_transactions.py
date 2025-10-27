"""Lakeflow Declarative Pipelines definitions for finance transaction processing."""

from __future__ import annotations

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

try:
    from pyspark import pipelines as dp
except ImportError:  # pragma: no cover - enables local linting and static checks
    dp = None

spark = SparkSession.builder.getOrCreate()


def cfg(name: str, default: str) -> str:
    return spark.conf.get(name, default)


if dp is not None:
    CATALOG = cfg("pipeline.catalog_name", "finance_dev")
    BRONZE_SCHEMA = cfg("pipeline.bronze_schema", "bronze")

    @dp.table(
        name="finance_transactions_silver_stream",
        comment="Lakeflow streaming Silver table with standardized transaction records.",
    )
    @dp.expect_or_drop("has_transaction_id", "transaction_id IS NOT NULL")
    @dp.expect_or_drop("has_account_id", "account_id IS NOT NULL")
    @dp.expect_or_drop("amount_non_negative", "amount >= 0")
    @dp.expect_or_drop("has_valid_currency", "LENGTH(currency) = 3")
    @dp.expect_or_drop("has_event_ts", "event_timestamp IS NOT NULL")
    def finance_transactions_silver_stream():
        return (
            spark.readStream.table(f"{CATALOG}.{BRONZE_SCHEMA}.finance_transactions")
            .withWatermark("event_timestamp", "7 days")
            .dropDuplicates(["transaction_id", "event_type", "event_timestamp"])
            .withColumn("currency", F.upper(F.trim(F.col("currency"))))
            .withColumn("event_type", F.upper(F.trim(F.col("event_type"))))
            .withColumn("event_ts", F.col("event_timestamp").cast("timestamp"))
        )

    @dp.table(
        name="finance_quality_metrics",
        comment="Operational quality and volume metrics for finance transactions.",
    )
    def finance_quality_metrics():
        source_df = (
            spark.readStream.table(f"{CATALOG}.{BRONZE_SCHEMA}.finance_transactions")
            .withColumn("event_ts", F.col("event_timestamp").cast("timestamp"))
            .withColumn("currency", F.upper(F.trim(F.col("currency"))))
        )
        valid_df = source_df.filter(
            F.col("transaction_id").isNotNull()
            & F.col("account_id").isNotNull()
            & (F.col("amount") >= F.lit(0))
            & (F.length(F.col("currency")) == F.lit(3))
            & F.col("event_ts").isNotNull()
        )
        return valid_df.withWatermark("event_ts", "7 days").groupBy(
            F.to_date(F.col("event_ts")).alias("metric_date")
        ).agg(
            F.count("*").alias("record_count"),
            F.approx_count_distinct("transaction_id").alias("distinct_transactions"),
            F.sum("amount").alias("gross_amount"),
        )
