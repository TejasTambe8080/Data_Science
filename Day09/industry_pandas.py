import pandas as pd 
data = {
    "date": ["2024-01-01", "2024-02-15"]
}

df = pd.DataFrame(data)
print(df)

df["date"] = pd.to_datetime(df["date"])

print(df["date"].dt.year)
print(df["date"].dt.month)