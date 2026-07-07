# Databricks notebook source
df_silver = spark.table("silver_sales")
display(df_silver)

# COMMAND ----------

dim_product = (
    df_silver.select("product_id","product_name","product_category","ppu")
    .dropDuplicates(["product_id"])
)
dim_product.write.mode("overwrite").format("delta").saveAsTable("dim_product")

# COMMAND ----------

dim_customer = (
    df_silver.select("customer_id").dropDuplicates()
)
dim_customer.write.mode("overwrite").format("delta").saveAsTable("dim_customer")


# COMMAND ----------

dim_region = (
    df_silver.select("region").dropDuplicates()
)
dim_region.write.mode("overwrite").format("delta").saveAsTable("dim_region")


# COMMAND ----------

from pyspark.sql.functions import year,month,dayofmonth,quarter

dim_date = (
    df_silver.select("order_date").dropDuplicates().\
    withColumn("year",year("order_date")).\
    withColumn("month",month("order_date")).\
    withColumn("day",dayofmonth("order_date")).\
    withColumn("quarter",quarter("order_date"))
)

dim_date.write.mode("overwrite").format("delta").saveAsTable("dim_date")

# COMMAND ----------

fact_sales = (
    df_silver.select("transaction_id","order_date","product_id","quantity","amount","customer_id","ppu","region")
)
fact_sales.write.mode("overwrite").format("delta").saveAsTable("fact_sales")


# COMMAND ----------

display(spark.table("dim_product"))
display(spark.table("dim_customer"))
display(spark.table("dim_region"))
display(spark.table("dim_date"))
display(spark.table("fact_sales"))

# COMMAND ----------

