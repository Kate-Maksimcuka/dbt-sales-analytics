SELECT
    orders.order_id,
    orders.order_date,
    DATE_TRUNC('month', orders.order_date) AS order_month,
    orders.customer_id,
    customers.customer_name,
    customers.region,
    customers.city,
    orders.product_id,
    products.product_name,
    products.category,
    orders.quantity,
    products.unit_price,
    orders.quantity * products.unit_price AS line_revenue,
    orders.sales_channel
FROM {{ ref('stg_orders') }} AS orders
LEFT JOIN {{ ref('stg_customers') }} AS customers
    ON orders.customer_id = customers.customer_id
LEFT JOIN {{ ref('stg_products') }} AS products
    ON orders.product_id = products.product_id
