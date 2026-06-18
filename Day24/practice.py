import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

salary = [
    30000,
    35000,
    40000,
    45000,
    50000,
    55000,
    60000,
    65000,
    70000,
    100000
]

s = pd.Series(salary)

# Task 1: Range
salary_range = s.max() - s.min()

# Task 2: Variance
variance = s.var()

# Task 3: Standard Deviation
std_dev = s.std()

# Task 4: Q1
q1 = s.quantile(0.25)

# Task 5: Q3
q3 = s.quantile(0.75)

# Task 6: IQR
iqr = q3 - q1

# Task 7: Coefficient of Variation
cv = (std_dev / s.mean()) * 100

print("Range:", salary_range)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Coefficient of Variation (%):", cv)
sns.histplot(salary, kde=True)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()