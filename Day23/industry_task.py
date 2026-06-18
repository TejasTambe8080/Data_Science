import pandas as pd
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

# Create Series
s = pd.Series(salary)

# ==========================
# DESCRIPTIVE STATISTICS
# ==========================

print("----- Salary Statistics Report -----\n")

# Mean
mean_salary = s.mean()
print("Average Salary:", mean_salary)

# Median
median_salary = s.median()
print("Median Salary:", median_salary)

# Mode
mode_salary = s.mode()
print("\nMode:")
print(mode_salary)

# Quartiles
q1 = s.quantile(0.25)
q2 = s.quantile(0.50)
q3 = s.quantile(0.75)

print("\nQ1 (25th Percentile):", q1)
print("Q2 (Median):", q2)
print("Q3 (75th Percentile):", q3)

# Percentiles
p90 = s.quantile(0.90)

print("\n90th Percentile:", p90)

# ==========================
# OUTLIER DETECTION (IQR)
# ==========================

iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print("\nLower Bound:", lower_bound)
print("Upper Bound:", upper_bound)

outliers = s[(s < lower_bound) | (s > upper_bound)]

print("\nOutliers:")
print(outliers)

# ==========================
# SUMMARY
# ==========================

print("\nSummary Statistics")
print(s.describe())

# ==========================
# HISTOGRAM
# ==========================

plt.figure(figsize=(8,5))

plt.hist(s, bins=5)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()