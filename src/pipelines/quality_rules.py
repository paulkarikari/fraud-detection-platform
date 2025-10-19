"""Reusable quality and conformance rules for finance transaction pipelines."""

from __future__ import annotations

from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def standardize_transactions(df: DataFrame) -> DataFrame:
    """Apply canonical casing and type normalization for conformed Silver records."""
    return (
        df.withColumn("transaction_id", F.trim(F.col("transaction_id")))
        .withColumn("account_id", F.trim(F.col("account_id")))
        .withColumn("currency", F.upper(F.trim(F.col("currency"))))
        .withColumn("event_type", F.upper(F.trim(F.col("event_type"))))
        .withColumn("source_system", F.lower(F.trim(F.col("source_system"))))
        .withColumn("event_ts", F.col("event_timestamp").cast("timestamp"))
        .withColumn("amount", F.col("amount").cast("decimal(18,2)"))
    )


def with_quality_flags(df: DataFrame) -> DataFrame:
    """Add deterministic quality flags used by DLT and non-DLT processing paths."""
    return (
        df.withColumn("dq_has_transaction_id", F.col("transaction_id").isNotNull())
        .withColumn("dq_has_account_id", F.col("account_id").isNotNull())
        .withColumn("dq_amount_non_negative", F.col("amount") >= F.lit(0))
        .withColumn("dq_valid_currency", F.length(F.col("currency")) == F.lit(3))
        .withColumn("dq_has_event_ts", F.col("event_ts").isNotNull())
        .withColumn(
            "dq_passed",
            F.col("dq_has_transaction_id")
            & F.col("dq_has_account_id")
            & F.col("dq_amount_non_negative")
            & F.col("dq_valid_currency")
            & F.col("dq_has_event_ts"),
        )
    )
