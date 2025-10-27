"""Gold publication job for finance data products."""

from __future__ import annotations

import argparse

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publish Gold finance data products.")
    parser.add_argument("--source-table", required=True, help="Silver source table.")
    parser.add_argument(
        "--gold-schema",
        required=True,
        help="Target catalog.schema for Gold outputs.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    spark = SparkSession.builder.getOrCreate()
    silver_df = spark.table(args.source_table)

    daily_summary_df = (
        silver_df.withColumn("transaction_date", F.to_date(F.col("event_ts")))
        .groupBy("transaction_date", "currency")
        .agg(
            F.countDistinct("transaction_id").alias("transaction_count"),
            F.sum("amount").alias("total_amount"),
            F.avg("amount").alias("avg_amount"),
        )
    )

    account_history_df = (
        silver_df.select(
            "transaction_id",
            "account_id",
            "counterparty_account_id",
            "event_type",
            "event_ts",
            "amount",
            "currency",
            "payment_channel",
            "source_system",
        )
        .orderBy(F.col("event_ts").desc())
    )

    (
        daily_summary_df.write.format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .saveAsTable(f"{args.gold_schema}.finance_daily_summary")
    )

    (
        account_history_df.write.format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .saveAsTable(f"{args.gold_schema}.account_transaction_history")
    )


if __name__ == "__main__":
    main()
