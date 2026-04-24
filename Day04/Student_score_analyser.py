## this is related to the csv files 

import pandas as pd 
df = pd.read_csv("student.csv")
print(df)

avg_marks = df["marks"].mean()

print("Average Marks:", avg_marks)

topper = df.loc[df["marks"].idxmax()]

print("Topper:\n", topper)

pass_count = (df["marks"] >= 50).sum()
fail_count = (df["marks"] < 50).sum()

print("Pass Students:", pass_count)
print("Fail Students:", fail_count)


