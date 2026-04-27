import pandas as pd

data = {
    "dept": ["IT", "IT", "HR", "HR", "IT"],
    "role": ["Dev", "Manager", "Dev", "Manager", "Dev"],
    "salary": [50000, 80000, 40000, 70000, 60000]
}
df = pd.DataFrame(data)

pivot = pd.pivot_table(df, values="salary", index="dept", aggfunc="mean")

print(pivot)

max = pd.pivot_table(df, values="salary", index="dept", aggfunc="max")
##Group By the role 
pivot_role = pd.pivot_table(df, values="salary", index="role", aggfunc="mean")

## find Highest paid role 
pivot_role_max = pd.pivot_table(df, values="salary", index="role", aggfunc="max")
