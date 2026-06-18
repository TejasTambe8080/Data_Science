import pandas as pd
import matplotlib.pyplot as plt

data = {
    "dept": ["IT", "HR", "IT", "HR", "IT", "Sales", "Sales"],
    "salary": [50000, 40000, 60000, 45000, 70000, 30000, 35000],
    "experience": [2, 1, 3, 2, 5, 1, 2]
}
df = pd.DataFrame(data)
print(df)
df.info()
df.describe()
df.isnull().sum()
df.duplicated().sum()
df["salary"].mean()
df.groupby("dept")["salary"].mean()
df[["experience","salary"]]
## GRAPH BAR CHART and SCATTER PLOT
dept_salary = df.groupby("dept")["salary"].mean()

dept_salary.plot(kind="bar")

plt.title("Department vs Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

plt.scatter(df["experience"], df["salary"])

plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")

plt.show()