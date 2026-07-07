# Databricks notebook source
from pyspark.sql.functions import current_timestamp

df_raw= spark.read.format("csv")\
.option("header","true")\
.option("inferSchema","true")\
.load("/Volumes/text/text_schema/my_volume/raw_sales_transactions.csv")

# Add ingestion timestamp for bronze 
df_bronze = df_raw.withColumn("ingestion_timestamp", current_timestamp())

# Previous data
display(df_bronze)

# COMMAND ----------

from pyspark.sql.functions import col

# clean column names
df_bronze = df_bronze.select(
    [col(c).alias(c.strip().replace(" ", "_")) for c in df_bronze.columns]
)

# write bronze table
df_bronze.write.mode("overwrite").format("delta").saveAsTable("bronze_sales")



# COMMAND ----------

display(spark.table("bronze_sales"))