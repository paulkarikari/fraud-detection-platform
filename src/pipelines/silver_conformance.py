"""Silver conformance job with deterministic quality checks and de-duplication."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Ensure shared pipeline helpers are importable when executed as a standalone script.
sys.path.append(str(Path(__file__).resolve().parent))

from quality_rules import standardize_transactions, with_quality_flags


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Conform Bronze transactions into Silver.")
    parser.add_argument("--source-table", required=True, help="Bronze source table.")
    parser.add_argument("--target-table", required=True, help="Silver target table.")
    parser.add_argument(
        "--quarantine-table",
        default="",
        help="Optional quarantine table for records failing quality checks.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    spark = SparkSession.builder.getOrCreate()

    source_df = spark.table(args.source_table)
    standardized_df = standardize_transactions(source_df)
    quality_df = with_quality_flags(standardized_df)

    valid_df = quality_df.filter(F.col("dq_passed") == F.lit(True))
    invalid_df = quality_df.filter(F.col("dq_passed") == F.lit(False))

    if args.quarantine_table:
        (
            invalid_df.write.format("delta")
            .mode("append")
            .option("mergeSchema", "true")
            .saveAsTable(args.quarantine_table)
        )

    dedupe_window = Window.partitionBy("transaction_id", "event_type").orderBy(
        F.col("event_ts").desc(),
        F.col("_ingest_ts").desc(),
        F.col("_source_file").desc(),
    )

    silver_df = (
        valid_df.withColumn("_record_rank", F.row_number().over(dedupe_window))
        .filter(F.col("_record_rank") == F.lit(1))
        .drop("_record_rank")
    )

    # Deterministic full replacement keeps reruns reproducible across environments.
    (
        silver_df.write.format("delta")
        .mode("overwrite")
        .option("overwriteSchema", "true")
        .saveAsTable(args.target_table)
    )


if __name__ == "__main__":
    main()
