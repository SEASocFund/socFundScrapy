import polars as pl

# load data
raw = pl.read_csv("SEAASEAN_raw.csv")

# merge keywords and remove duplicates
clean = (
    raw
    .group_by("pronums")
    .agg(pl.col("keyword").unique().str.join("；").alias("keyword"))
    .join(raw.drop("keyword"), on="pronums", how="full")  # Use outer join to keep missing pronums
    .unique(subset="pronums")
    .drop("pronums_right")
)

# save clean data
clean.write_csv("SEAASEAN_clean.csv")
