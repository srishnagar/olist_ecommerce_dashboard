# Olist E-Commerce Business Intelligence Dashboard

A end-to-end business intelligence project analyzing 100,000+ real orders 
from Olist, Brazil's largest e-commerce platform. Built using Python, SQL, 
and Power BI.

---

## Tools Used
- **Python (Pandas)** — data cleaning and preparation
- **SQL (pandasql)** — business question analysis
- **Power BI** — interactive dashboard (4 pages)

---

## Dataset
- Source: [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)
- 100,000+ orders across 9 related tables (2016–2018)

---

## Dashboard Pages

| Page | Business Question |
|------|-------------------|
| Sales Overview | How is revenue trending over time? |
| Customer Analysis | Who are our customers and where are they? |
| Order Health | Where are deliveries failing? |
| Seller Performance | Who are the top performing sellers? |

---

## Key Business Insights

1. **Revenue grew 25x from Oct 2016 to Nov 2017** — driven by platform 
   expansion. November 2017 was the peak month (likely Black Friday effect).

2. **Bed, Bath & Table is the top revenue category** at R$1.69M, followed 
   by Health & Beauty (R$1.62M) — suggesting strong home goods demand.

3. **São Paulo dominates** with 42% of all orders and 70% of seller activity 
   — indicating high geographic concentration risk for the business.

4. **92% on-time delivery rate overall**, but northern states like RR and AP 
   average 27+ days vs SP's much lower average — a clear logistics gap.

5. **Top seller generates R$505K revenue** but has only a 3.35 avg review 
   score — high volume does not guarantee customer satisfaction.

---

## Business Recommendations

- **Invest in logistics infrastructure** in northern states (RR, AP, AM) 
  where delivery times exceed 25 days — this directly impacts review scores.

- **Introduce a seller quality program** — the top revenue sellers have below 
  average review scores, creating long-term retention risk.

- **Diversify geographic marketing** beyond São Paulo — RJ and MG show 
  growth potential but remain underpenetrated relative to SP.

---

## Project Structure
```
olist-ecommerce-dashboard/
├── data/                          
│   └── olist_cleaned.csv          
├── notebooks/
│   └── data_cleaning.py           
├── sql/
│   └── business_queries.py        
├── dashboard/
│   └── olist_dashboard.pbix       
└── screenshots/
    ├── sales_overview.png
    ├── customer_analysis.png
    ├── order_health.png
    └── seller_performance.png
```

---

## How to Run

1. Download dataset from Kaggle link above
2. Place CSVs in `/data` folder
3. Run `notebooks/data_cleaning.py` to generate `olist_cleaned.csv`
4. Run `sql/business_queries.py` to see analysis output
5. Open `dashboard/olist_dashboard.pbix` in Power BI Desktop