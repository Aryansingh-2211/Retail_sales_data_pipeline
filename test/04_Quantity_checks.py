# Databricks notebook source
from pyspark.sql.functions import col, sum, when

df = spark.table("silver_sales")

df.select(
    sum(when(col("transaction_id").isNull(), 1).otherwise(0)).alias("null_transaction_id"),
    sum(when(col("order_date").isNull(), 1).otherwise(0)).alias("null_order_date"),
    sum(when(col("product_id").isNull(), 1).otherwise(0)).alias("null_product_id"),
    sum(when(col("customer_id").isNull(), 1).otherwise(0)).alias("null_customer_id"),
    sum(when(col("amount").isNull(), 1).otherwise(0)).alias("null_amount")
).show()

# COMMAND ----------

spark.sql("""
SELECT transaction_id, COUNT(*) as cnt
FROM silver_sales
GROUP BY transaction_id
HAVING COUNT(*) > 1
""").display()

# COMMAND ----------

spark.sql("""
SELECT *
FROM silver_sales
WHERE quantity <= 0 OR ppu <= 0 OR amount <= 0
""").show()

# COMMAND ----------

spark.sql("""
SELECT *
FROM silver_sales
WHERE amount != quantity * ppu
""").show()

# COMMAND ----------

spark.sql("""
SELECT *
FROM fact_sales
WHERE transaction_id IS NULL
   OR product_id IS NULL
   OR customer_id IS NULL
   OR amount IS NULL
""").show()