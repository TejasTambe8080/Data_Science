import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd 
data = {
    "dept": ["IT", "IT", "HR", "HR", "IT"],
    "role": ["Dev", "Manager", "Dev", "Manager", "Dev"],
    "salary": [50000, 80000, 40000, 70000, 60000]
}

df = pd.DataFrame(data)
## pivot avg salry per dept 
pivot = pd.pivot_table(df, values="salary", index="dept", aggfunc="mean")
print(pivot)
## pivot max salary per dept
max = pd.pivot_table(df, values="salary", index="dept", aggfunc="max")
print(max)
## group by the dept + role 
pivot_role = pd.pivot_table(df, values="salary", index="role", aggfunc="mean")
print(pivot_role)
## find Highest paid role 
pivot_role_max = pd.pivot_table(df, values="salary", index="role", aggfunc="max")
print(pivot_role_max)