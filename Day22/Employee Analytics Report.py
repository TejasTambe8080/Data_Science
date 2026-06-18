import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "department":["IT","HR","Sales","IT","HR","Sales","IT","HR","Sales","IT"],
    "experience":[1,2,3,4,5,6,7,8,9,10],
    "salary":[30000,35000,40000,50000,60000,65000,80000,85000,90000,110000],
    "performance":[60,65,70,75,80,82,88,90,93,98]
}

df = pd.DataFrame(data)

print("Missing Values:")
print(df.isnull().sum())

print("Duplicate Rows:")
print(df.duplicated().sum())
dept_salary = df.groupby("department")["salary"].mean()

print("Average Salary By Department")
print(dept_salary)
dept_perf = df.groupby("department")["performance"].mean()

print("Average Performance By Department")
print(dept_perf)

print("Maximum Salary:", df["salary"].max())

print("Minimum Salary:", df["salary"].min())

print("Average Salary:", df["salary"].mean())

print("Maximum Performance:", df["performance"].max())

print("Average Performance:", df["performance"].mean())

print(df.loc[df["performance"].idxmax()])

corr = df.corr(numeric_only=True)

print(corr)
print(corr["salary"])
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
plt.scatter(df["performance"], df["salary"])

plt.title("Performance vs Salary")
plt.xlabel("Performance")
plt.ylabel("Salary")

plt.show()

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()