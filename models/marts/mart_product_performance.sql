SELECT
    product_id,
    product_name,
    category,
    SUM(quantity) AS total_items_sold,
    ROUND(SUM(line_revenue), 2) AS total_revenue,
    COUNT(DISTINCT order_id) AS total_orders
FROM {{ ref('int_order_items') }}
GROUP BY product_id, product_name, category
