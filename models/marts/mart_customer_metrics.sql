SELECT
    customer_id,
    customer_name,
    region,
    city,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(quantity) AS total_items_bought,
    ROUND(SUM(line_revenue), 2) AS total_spend,
    ROUND(SUM(line_revenue) / COUNT(DISTINCT order_id), 2) AS average_order_value,
    MIN(order_date) AS first_order_date,
    MAX(order_date) AS latest_order_date
FROM {{ ref('int_order_items') }}
GROUP BY customer_id, customer_name, region, city
