SELECT
    CAST(product_id AS INTEGER) AS product_id,
    product_name,
    category,
    CAST(unit_price AS DECIMAL(10, 2)) AS unit_price
FROM {{ ref('raw_products') }}
