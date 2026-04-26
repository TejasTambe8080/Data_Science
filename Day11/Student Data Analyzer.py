import pandas as pd 

data = {
    "name": ["Tejas", "Rahul", "Anita"],
    "marks": [80, 40, 90]
}
df = pd.DataFrame(data)
print(df)

rows = df.head(2)
print(rows)

avg = df["marks"].mean()
print("Average marks:", avg)
topper = df[df["marks"] == df["marks"].max()]
print("Topper:", topper["name"].values[0])

passed_students = df[df["marks"] >= 50] 
print("Passed students:")
print(passed_students["name"].values)