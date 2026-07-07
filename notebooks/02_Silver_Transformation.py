# Databricks notebook source
df_bronze = spark.table("bronze_sales")
display(df_bronze)

# COMMAND ----------

from pyspark.sql.functions import col,regexp_replace, to_date

df_silver = (
    df_bronze
    .withColumnRenamed("Transaction_ID","transaction_id")
    .withColumnRenamed("Product_ID","product_id")
    .withColumnRenamed("Product_Name","product_name")
    .withColumnRenamed("Product_Category","product_category")
    .withColumnRenamed("Date","order_date")
    .withColumnRenamed("PPU","ppu")
    .withColumnRenamed("Amount","amount")
    .withColumnRenamed("Customer_ID","customer_id")
    .withColumnRenamed("Region","region")
)


# Convert date
df_silver = df_silver.withColumn("order_date", to_date(col("order_date"),"yyyy-MM-dd"))

#Remove commas and convert ppu, amount to numeric
df_silver = df_silver.withColumn("ppu",regexp_replace(col("ppu"),",","").cast("double"))
df_silver = df_silver.withColumn("amount",regexp_replace(col("amount"),",","").cast("double"))

# Quantity to integer
df_silver = df_silver.withColumn("quantity",col("quantity").cast("int"))

#Remove duplicate rows
df_silver = df_silver.dropDuplicates()

display(df_silver)

# COMMAND ----------

df_silver.write.mode("overwrite").format("delta").saveAsTable("silver_sales")

# COMMAND ----------

display(spark.table("silver_sales"))