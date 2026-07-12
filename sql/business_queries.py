import pandas as pd
from pandasql import sqldf

df = pd.read_csv('D:/olist_ecommerce_dashboard/data/olist_cleaned.csv')

# Helper to run SQL queries directly on the dataframe
pysql = lambda q: sqldf(q, {'df': df})

# Q1: High-level business metrics
q1 = pysql("""
    SELECT 
        COUNT(DISTINCT order_id)        AS total_orders,
        ROUND(SUM(payment_value), 2)    AS total_revenue,
        ROUND(AVG(payment_value), 2)    AS avg_order_value
    FROM df
""")
print("=== Q1: Overall Business Metrics ===")
print(q1)

# Q2: How has revenue trended month over month?
q2 = pysql("""
    SELECT 
        order_year,
        order_month,
        order_month_name,
        ROUND(SUM(payment_value), 2) AS monthly_revenue,
        COUNT(DISTINCT order_id)     AS monthly_orders
    FROM df
    GROUP BY order_year, order_month, order_month_name
    ORDER BY order_year, order_month
""")
print("\n=== Q2: Monthly Revenue Trend ===")
print(q2)

# Q3: Which product categories are driving the most revenue?
q3 = pysql("""
    SELECT 
        category,
        ROUND(SUM(payment_value), 2) AS category_revenue,
        COUNT(DISTINCT order_id)     AS category_orders
    FROM df
    GROUP BY category
    ORDER BY category_revenue DESC
    LIMIT 10
""")
print("\n=== Q3: Top 10 Categories by Revenue ===")
print(q3)

# Q4: What percentage of orders are delivered on time?
q4 = pysql("""
    SELECT
        on_time,
        COUNT(DISTINCT order_id) AS total_orders
    FROM df
    GROUP BY on_time
""")
print("\n=== Q4: On-Time vs Late Deliveries ===")
print(q4)

# Q5: Which states have the slowest delivery times? (logistics gap analysis)
q5 = pysql("""
    SELECT 
        customer_state,
        ROUND(AVG(delivery_days), 1) AS avg_delivery_days,
        COUNT(DISTINCT order_id)     AS total_orders
    FROM df
    GROUP BY customer_state
    ORDER BY avg_delivery_days DESC
    LIMIT 10
""")
print("\n=== Q5: Top 10 Slowest States (Avg Delivery Days) ===")
print(q5)

# Q6: Do higher-rated categories correlate with specific product types?
q6 = pysql("""
    SELECT 
        category,
        ROUND(AVG(review_score), 2)  AS avg_review_score,
        COUNT(DISTINCT order_id)     AS total_orders
    FROM df
    GROUP BY category
    ORDER BY avg_review_score DESC
    LIMIT 10
""")
print("\n=== Q6: Top 10 Categories by Review Score ===")
print(q6)

# Q7: Top sellers by revenue — do high revenue sellers also have high ratings?
q7 = pysql("""
    SELECT 
        seller_id,
        seller_state,
        ROUND(SUM(payment_value), 2) AS seller_revenue,
        COUNT(DISTINCT order_id)     AS seller_orders,
        ROUND(AVG(review_score), 2)  AS avg_review
    FROM df
    GROUP BY seller_id, seller_state
    ORDER BY seller_revenue DESC
    LIMIT 10
""")
print("\n=== Q7: Top 10 Sellers by Revenue ===")
print(q7)

print("\nAll queries done!")
