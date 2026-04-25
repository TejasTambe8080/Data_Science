import pandas as pd
from datetime import datetime

data = {
    "date": ["2024-01-01", "2024-01-05", "2024-02-01"],
    "sales": [100, 200, 300]
}

df = pd.DataFrame(data)

# ✔ Convert to datetime
df['date'] = pd.to_datetime(df['date'])

# ✔ Extract month
df['month'] = df['date'].dt.month

# ✔ Calculate total sales per month
monthly_sales = df.groupby('month')['sales'].sum()

# ✔ Find highest sales day
max_sales_day = df.loc[df['sales'].idxmax()]

# Output
print("DataFrame:\n", df)
print("\nTotal Sales per Month:\n", monthly_sales)
print("\nHighest Sales Day:\n", max_sales_day)