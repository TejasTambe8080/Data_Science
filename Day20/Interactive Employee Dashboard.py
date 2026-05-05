import pandas as pd
import matplotlib.pyplot as plt

data = {
    "dept": ["IT", "HR", "IT", "HR", "IT"],
    "salary": [50000, 40000, 60000, 45000, 70000]
}

df = pd.DataFrame(data)

# 🔹 1. Bar Chart → Dept vs Avg Salary
dept_salary = df.groupby("dept")["salary"].mean()

plt.figure()
dept_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

# 🔹 2. Scatter Plot → Index vs Salary
plt.figure()
plt.scatter(df.index, df["salary"])
plt.title("Salary Distribution (Index vs Salary)")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.show()

# 🔹 3. Line Chart → Salary Trend
plt.figure()
plt.plot(df["salary"])
plt.title("Salary Trend Over Employees")
plt.xlabel("Employee Index")
plt.ylabel("Salary")
plt.show()