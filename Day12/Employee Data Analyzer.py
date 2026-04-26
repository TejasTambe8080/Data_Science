import pandas as pd 
data = {
    "name": ["A", "B", "C", "C"],
    "dept": ["IT", "HR", "IT", "IT"],
    "salary": [50000, None, 60000, 60000]
}

df = pd.DataFrame(data)

df["name"] = df["name"].str.strip()
df["dept"] = df["dept"].str.strip()
df["salary"] = df["salary"].fillna(df["salary"].mean())
df = df.drop_duplicates()
print(df)

avg_salry = df["salary"].mean()
print("Average Salary:", avg_salry)

highest_salary = df[df["salary"] == df["salary"].max()]
print("Employee with highest salary:", highest_salary["name"].values[0])

second_highest = df["salary"].sort_values(ascending=False).iloc[1]
print(second_highest)
