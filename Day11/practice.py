import pandas as pd
data = {
    "name": ["A", "B", "C"],
    "marks": [80, 90, 70]
}

df = pd.DataFrame(data)
print(df)
rows = df.head()
print(rows)
marks = df[df["marks"] > 80]
print(marks)
avg = df["marks"].mean()
print(avg)