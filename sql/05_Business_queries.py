# Databricks notebook source
# DBTITLE 1,Top 5 months by revenue
# MAGIC %sql
# MAGIC Select 
# MAGIC     year(order_date) as year,
# MAGIC     month(order_date) as month,
# MAGIC     Sum(amount) as revenue
# MAGIC     From fact_sales
# MAGIC     Group by year(order_date),Month(order_date)
# MAGIC     Order by revenue desc
# MAGIC     limit 5;

# COMMAND ----------

# DBTITLE 1,Average order values
# MAGIC %sql
# MAGIC Select 
# MAGIC Round(sum(amount) / Count(distinct transaction_id),2) as avg_order_values
# MAGIC From fact_sales

# COMMAND ----------

# DBTITLE 1,Category contribution %
# MAGIC %sql
# MAGIC SELECT 
# MAGIC     p.product_category,
# MAGIC     ROUND(SUM(f.amount), 2) AS revenue,
# MAGIC     ROUND(100.0 * SUM(f.amount) / (SELECT SUM(amount) FROM fact_sales), 2) AS revenue_pct
# MAGIC FROM fact_sales f
# MAGIC JOIN dim_product p
# MAGIC     ON f.product_id = p.product_id
# MAGIC GROUP BY p.product_category
# MAGIC ORDER BY revenue DESC;

# COMMAND ----------

# DBTITLE 1,Top customer contributing highest revenue
# MAGIC %sql
# MAGIC SELECT 
# MAGIC     customer_id,
# MAGIC     SUM(amount) AS total_spent
# MAGIC FROM fact_sales
# MAGIC GROUP BY customer_id
# MAGIC ORDER BY total_spent DESC
# MAGIC LIMIT 20;

# COMMAND ----------

# DBTITLE 1,Best region by revenue
# MAGIC %sql
# MAGIC SELECT 
# MAGIC     region,
# MAGIC     SUM(amount) AS total_revenue
# MAGIC FROM fact_sales
# MAGIC GROUP BY region
# MAGIC ORDER BY total_revenue DESC
# MAGIC LIMIT 1;