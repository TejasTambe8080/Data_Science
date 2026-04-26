import pandas as pd 
data = {
    "name": [" A ", "B", "C", "C"],
    "marks": [80, None, 70, 70]
}
df = pd.DataFrame(data)


df["name"] = df["name"].str.strip()

df["marks"] = df["marks"].fillna(df["marks"].mean())


df = df.drop_duplicates()
df["marks"] = df["marks"].astype(int)

print(df)