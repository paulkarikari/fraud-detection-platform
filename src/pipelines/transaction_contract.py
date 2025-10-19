"""Shared transaction contract definitions for finance pipelines."""

from __future__ import annotations

from pyspark.sql.types import DecimalType, StringType, StructField, StructType, TimestampType

TRANSACTION_SCHEMA = StructType(
    [
        StructField("transaction_id", StringType(), False),
        StructField("account_id", StringType(), False),
        StructField("counterparty_account_id", StringType(), True),
        StructField("event_type", StringType(), False),
        StructField("event_timestamp", TimestampType(), False),
        StructField("amount", DecimalType(18, 2), False),
        StructField("currency", StringType(), False),
        StructField("payment_channel", StringType(), True),
        StructField("source_system", StringType(), False),
        StructField("ingestion_batch_id", StringType(), True),
    ]
)

VALID_EVENT_TYPES = (
    "AUTHORIZED",
    "SETTLED",
    "REVERSED",
)
