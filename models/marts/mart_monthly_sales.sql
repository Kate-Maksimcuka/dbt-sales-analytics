SELECT
    order_month,
    COUNT(DISTINCT order_id) AS total_orders,
    SUM(quantity) AS total_items_sold,
    ROUND(SUM(line_revenue), 2) AS total_revenue,
    ROUND(SUM(line_revenue) / COUNT(DISTINCT order_id), 2) AS average_order_value
FROM {{ ref('int_order_items') }}
GROUP BY order_month
