
# Retail Sales Data Pipeline using Databricks, PySpark, and SQL

## Project Overview
This project builds an end-to-end retail sales data pipeline using Databricks, PySpark, Spark SQL, and Delta Lake.  
The pipeline ingests raw retail sales transaction data from a CSV file into a Bronze layer, cleans and standardizes the data in a Silver layer, and transforms it into Gold fact and dimension tables for analytics and reporting.

The project follows a **Medallion Architecture (Bronze → Silver → Gold)** and uses a **fact + dimension model** in the Gold layer to support business analysis.

---

## Tech Stack
- **Databricks**
- **PySpark**
- **Spark SQL**
- **Delta Lake**
- **GitHub**

---

## Project Architecture

### Bronze Layer
- Load raw CSV file into Databricks
- Store raw data as a Delta table
- Add ingestion timestamp

### Silver Layer
- Rename columns into a standardized format
- Convert date and numeric columns to proper data types
- Remove duplicates
- Prepare cleaned data for downstream modeling

### Gold Layer
Build a simple star-schema style warehouse model:
- **Fact Table**
  - `fact_sales`
- **Dimension Tables**
  - `dim_product`
  - `dim_customer`
  - `dim_region`
  - `dim_date`

---

## Dataset
Source file used in this project:

-  raw_sales_transaction

Main columns:
- Transaction_ID
- Date
- Product_ID
- Product_Name
- Product_Category
- Quantity
- PPU
- Amount
- Customer_ID
- Region

---

## Data Model

### Bronze Table
- `bronze_sales`

### Silver Table
- `silver_sales`

### Gold Tables

#### Fact Table
- `fact_sales`

#### Dimension Tables
- `dim_product`
- `dim_customer`
- `dim_region`
- `dim_date`

---

## Project Workflow

### 1. Bronze Layer
- Upload raw CSV file to Databricks
- Read CSV using PySpark
- Add ingestion timestamp
- Save as `bronze_sales`

### 2. Silver Layer
- Read `bronze_sales`
- Rename columns to lowercase standardized names
- Convert:
  - `order_date` → date
  - `quantity` → integer
  - `ppu` → double
  - `amount` → double
- Remove duplicate rows
- Save as `silver_sales`

### 3. Gold Layer
Create:
- `dim_product`
- `dim_customer`
- `dim_region`
- `dim_date`
- `fact_sales`

### 4. Analytics Layer
Run SQL queries for:
- total revenue
- monthly revenue
- top products
- top categories
- region-wise sales
- top customers
- average order value

---

## Key Transformations

### Bronze
- Raw CSV ingestion
- Added ingestion timestamp

### Silver
- Standardized column names
- Converted date format
- Casted numeric columns
- Removed duplicates

### Gold
- Built fact and dimension tables
- Structured data for business reporting and analysis

---

## Data Quality Checks
The project includes quality validations such as:
- Null checks on critical fields
- Duplicate transaction checks
- Negative / zero sales validation
- Amount = Quantity × PPU validation

---

# Me : Aryan kumar (student) 
thanks.
