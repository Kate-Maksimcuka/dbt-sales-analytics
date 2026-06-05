-- Example analysis query using the final sales mart

SELECT
    order_month,
    total_revenue,
    total_orders,
    average_order_value
FROM {{ ref('mart_monthly_sales') }}
ORDER BY order_month;
