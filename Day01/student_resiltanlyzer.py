import pandas as pd

data = {
    "name": ["Tejas", "Rahul", "Priya", "Anjali"],
    "marks": [90, 85, 95, 88]
}

df = pd.DataFrame(data)


print("Average MArks:", df["marks"].mean())
print("Maximum Marks:", df["marks"].max())
print("Minimum Marks:", df["marks"].min())