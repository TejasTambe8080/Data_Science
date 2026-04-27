import matplotlib.pyplot as plt 
import pandas as pd
data = {
    "dept": ["IT", "HR", "IT", "HR"],
    "salary": [50000, 40000, 60000, 45000]
}
df = pd.DataFrame(data)

# ✅ Tasks:

# ✔ Bar chart → avg salary per dept
# ✔ Histogram → salary distribution
# ✔ Line chart → index vs salary

## Bar chart for avg salary per dept
dept_salary = df.groupby("dept")["salary"].mean()
plt.figure()
dept_salary.plot(kind="bar")
plt.title("Average Salary by Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

# Histogram for salary distribution
plt.figure()
plt.hist(df["salary"])
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()
#Line chart for index vs salary
plt.figure()
plt.plot(df.index, df["salary"])
plt.title("Index vs Salary")
plt.xlabel("Index")
plt.ylabel("Salary")
plt.show()
