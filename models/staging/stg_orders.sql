SELECT
    CAST(order_id AS INTEGER) AS order_id,
    CAST(order_date AS DATE) AS order_date,
    CAST(customer_id AS INTEGER) AS customer_id,
    CAST(product_id AS INTEGER) AS product_id,
    CAST(quantity AS INTEGER) AS quantity,
    sales_channel
FROM {{ ref('raw_orders') }}
