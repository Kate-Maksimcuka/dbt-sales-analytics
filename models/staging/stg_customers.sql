SELECT
    CAST(customer_id AS INTEGER) AS customer_id,
    customer_name,
    region,
    city,
    CAST(signup_date AS DATE) AS signup_date
FROM {{ ref('raw_customers') }}
