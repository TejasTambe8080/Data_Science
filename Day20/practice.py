import pandas as pd
import matplotlib.pyplot as plt

data = {
    "dept": ["IT", "HR", "IT", "HR", "IT"],
    "salary": [50000, 40000, 60000, 45000, 70000]
}

df = pd.DataFrame(data)

# 1️⃣ Bar Chart → dept vs avg salary
dept_salary = df.groupby("dept")["salary"].mean()
plt.figure()
dept_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()

# 2️⃣ Scatter Plot → index vs salary
plt.figure()
plt.scatter(df.index, df["salary"])
plt.title("Index vs Salary")
plt.xlabel("Index")
plt.ylabel("Salary")
plt.show()

# 3️⃣ Line Plot → salary trend
plt.figure()
plt.plot(df["salary"])
plt.title("Salary Trend")
plt.xlabel("Index")
plt.ylabel("Salary")
plt.show()