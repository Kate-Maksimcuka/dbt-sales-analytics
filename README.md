# dbt Sales Analytics

## Project Overview

This project uses dbt to transform raw sales data into clean analytics tables for reporting.

It is designed as a beginner analytics engineering project focused on SQL, data modelling, testing and documentation.

## Project Goals

- Practise dbt project structure
- Build staging, intermediate and mart models
- Apply basic data quality tests
- Create clean reporting tables
- Use final tables for simple sales analysis and charts

## Tools

- dbt
- SQL
- DuckDB, Postgres or BigQuery
- Python or BI tool for charts
- GitHub

## Planned dbt Structure

- `stg_customers`
- `stg_orders`
- `stg_products`
- `int_order_items`
- `mart_sales_summary`
- `mart_customer_metrics`

## Planned Tests

- Unique customer IDs
- Non-null order IDs
- Accepted values for order status
- Relationship checks between customers and orders

## Planned Charts

- Monthly revenue trend
- Top product categories
- Sales by customer segment
- Average order value over time
- Repeat vs one-time customers

## What This Project Demonstrates

- SQL transformations
- dbt modelling conventions
- Data quality checks
- Analytics engineering basics
- Business-focused reporting tables
