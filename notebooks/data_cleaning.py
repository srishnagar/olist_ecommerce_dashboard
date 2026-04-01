import pandas as pd

# ── Load ──────────────────────────────────────────────────────────────
customers            = pd.read_csv('D:/olist_ecommerce_dashboard/data/olist_customers_dataset.csv')
orders               = pd.read_csv('D:/olist_ecommerce_dashboard/data/olist_orders_dataset.csv')
order_items          = pd.read_csv('D:/olist_ecommerce_dashboard/data/olist_order_items_dataset.csv')
payments             = pd.read_csv('D:/olist_ecommerce_dashboard/data/olist_order_payments_dataset.csv')
reviews              = pd.read_csv('D:/olist_ecommerce_dashboard/data/olist_order_reviews_dataset.csv')
products             = pd.read_csv('D:/olist_ecommerce_dashboard/data/olist_products_dataset.csv')
sellers              = pd.read_csv('D:/olist_ecommerce_dashboard/data/olist_sellers_dataset.csv')
category_translation = pd.read_csv('D:/olist_ecommerce_dashboard/data/product_category_name_translation.csv')

# ── Clean orders ──────────────────────────────────────────────────────
date_cols = ['order_purchase_timestamp', 'order_delivered_customer_date',
             'order_estimated_delivery_date']
for col in date_cols:
    orders[col] = pd.to_datetime(orders[col])

orders = orders[orders['order_status'] == 'delivered']

orders['order_year']       = orders['order_purchase_timestamp'].dt.year
orders['order_month']      = orders['order_purchase_timestamp'].dt.month
orders['order_month_name'] = orders['order_purchase_timestamp'].dt.strftime('%b %Y')
orders['delivery_days']    = (
    orders['order_delivered_customer_date'] - orders['order_purchase_timestamp']
).dt.days
orders['on_time'] = orders['order_delivered_customer_date'] <= orders['order_estimated_delivery_date']

# ── Clean products ────────────────────────────────────────────────────
products = products.merge(category_translation, on='product_category_name', how='left')
products['category'] = products['product_category_name_english'].fillna('unknown')

# ── Clean reviews ─────────────────────────────────────────────────────
reviews = reviews.drop_duplicates(subset='order_id', keep='first')[['order_id', 'review_score']]

# ── Clean payments ────────────────────────────────────────────────────
payments = payments.groupby('order_id', as_index=False)['payment_value'].sum()

# ── Merge everything ──────────────────────────────────────────────────
# orders → customers (via customer_id)
df = orders.merge(customers, on='customer_id', how='left')

# df → order_items (via order_id)
df = df.merge(order_items, on='order_id', how='left')

# df → payments (via order_id)
df = df.merge(payments, on='order_id', how='left')

# df → reviews (via order_id)
df = df.merge(reviews, on='order_id', how='left')

# df → products (via product_id) — only keep category
df = df.merge(products[['product_id', 'category']], on='product_id', how='left')

# df → sellers (via seller_id) — only keep seller_state
df = df.merge(sellers[['seller_id', 'seller_state']], on='seller_id', how='left')

# ── Drop nulls in critical columns ────────────────────────────────────
df = df.dropna(subset=['payment_value', 'delivery_days'])

# ── Save ──────────────────────────────────────────────────────────────
output_path = 'D:/olist_ecommerce_dashboard/data/olist_cleaned.csv'
df.to_csv(output_path, index=False)

print("Cleaning done!")
print(f"Final dataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print(f"Saved to: {output_path}")