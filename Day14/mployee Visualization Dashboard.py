import pandas as pd
import matplotlib.pyplot as plt

data = {
    "dept": ["IT", "HR", "IT", "HR", "IT"],
    "salary": [50000, 40000, 60000, 45000, 70000]
}

df = pd.DataFrame(data)

# ✔ Bar chart → avg salary per dept
avg_salary = df.groupby("dept")["salary"].mean()

plt.figure()
plt.bar(avg_salary.index, avg_salary.values)
plt.title("Average Salary per Department")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

# ✔ Histogram → salary distribution
plt.figure()
plt.hist(df["salary"])
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# ✔ Scatter → index vs salary
plt.figure()
plt.scatter(df.index, df["salary"])
plt.title("Index vs Salary")
plt.xlabel("Index")
plt.ylabel("Salary")
plt.show()