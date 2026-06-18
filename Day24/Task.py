import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset
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

# ======================
# Spread Statistics
# ======================

salary_range = s.max() - s.min()

variance = s.var()

std_dev = s.std()

q1 = s.quantile(0.25)

q3 = s.quantile(0.75)

iqr = q3 - q1

cv = (std_dev / s.mean()) * 100

print("Range:", salary_range)
print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("Q1:", q1)
print("Q3:", q3)
print("IQR:", iqr)
print("Coefficient of Variation (%):", cv)

# ======================
# Outlier Detection
# ======================

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = s[(s < lower_bound) | (s > upper_bound)]

print("\nLower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

print("\nOutliers:")
print(outliers)

# ======================
# Histogram
# ======================

plt.figure(figsize=(8,5))

sns.histplot(salary, kde=True)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()

# ======================
# Boxplot
# ======================

plt.figure(figsize=(8,2))

sns.boxplot(x=salary)

plt.title("Salary Boxplot")

plt.show()