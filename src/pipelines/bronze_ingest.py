"""Bronze ingestion job for append-only transaction capture."""

from __future__ import annotations

import argparse

from pyspark.sql import DataFrame, SparkSession
from pyspark.sql import functions as F


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ingest finance transactions into Bronze.")
    parser.add_argument("--source-table", required=True, help="Input landing table name.")
    parser.add_argument("--target-table", required=True, help="Bronze target table name.")
    parser.add_argument(
        "--load-mode",
        choices=("batch", "stream"),
        default="batch",
        help="Execution mode: batch or stream.",
    )
    parser.add_argument(
        "--checkpoint-path",
        default="",
        help="Checkpoint path for streaming mode. Optional in batch mode.",
    )
    return parser.parse_args()


def with_ingestion_metadata(df: DataFrame) -> DataFrame:
    return (
        df.withColumn("_ingest_ts", F.current_timestamp())
        .withColumn("_ingest_date", F.to_date(F.col("_ingest_ts")))
        .withColumn("_source_file", F.coalesce(F.input_file_name(), F.lit("managed_table")))
    )


def run_batch(spark: SparkSession, source_table: str, target_table: str) -> None:
    source_df = spark.table(source_table)
    bronze_df = with_ingestion_metadata(source_df)

    (
        bronze_df.write.format("delta")
        .mode("append")
        .option("mergeSchema", "true")
        .saveAsTable(target_table)
    )


def run_stream(
    spark: SparkSession,
    source_table: str,
    target_table: str,
    checkpoint_path: str,
) -> None:
    if not checkpoint_path:
        raise ValueError("--checkpoint-path is required when --load-mode=stream")

    source_df = spark.readStream.table(source_table)
    bronze_df = with_ingestion_metadata(source_df)

    query = (
        bronze_df.writeStream.format("delta")
        .outputMode("append")
        .option("checkpointLocation", checkpoint_path)
        .toTable(target_table)
    )
    query.awaitTermination()


def main() -> None:
    args = parse_args()
    spark = SparkSession.builder.getOrCreate()

    if args.load_mode == "stream":
        run_stream(spark, args.source_table, args.target_table, args.checkpoint_path)
        return

    run_batch(spark, args.source_table, args.target_table)


if __name__ == "__main__":
    main()
