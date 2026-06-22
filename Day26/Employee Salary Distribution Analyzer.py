import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

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

# Create DataFrame
df = pd.DataFrame({"Salary": salary})

# Mean
mean_salary = df["Salary"].mean()

# Standard Deviation
std_salary = df["Salary"].std()

# Z-Score
df["Z-Score"] = zscore(df["Salary"])

# Outlier Detection
outliers = df[abs(df["Z-Score"]) > 3]

# Results
print("========== Salary Analysis ==========")
print(f"Mean Salary: ₹{mean_salary:.2f}")
print(f"Standard Deviation: ₹{std_salary:.2f}")

print("\nSalary with Z-Scores:")
print(df)

print("\nOutliers:")
print(outliers)

# Histogram
plt.figure(figsize=(8,5))
plt.hist(df["Salary"], bins=6)
plt.axvline(mean_salary, linestyle="--", label=f"Mean = {mean_salary:.0f}")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.title("Employee Salary Distribution")
plt.legend()
plt.show()