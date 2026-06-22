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

# ----------------------------
# Mean
# ----------------------------
mean_salary = df["Salary"].mean()

# ----------------------------
# Standard Deviation
# ----------------------------
std_salary = df["Salary"].std()

# ----------------------------
# Z-Score Calculation
# ----------------------------
df["Z-Score"] = zscore(df["Salary"])

# ----------------------------
# Outlier Detection
# ----------------------------
outliers = df[abs(df["Z-Score"]) > 3]

# ----------------------------
# Results
# ----------------------------
print("=" * 50)
print("EMPLOYEE SALARY DISTRIBUTION ANALYZER")
print("=" * 50)

print(f"\nMean Salary: ₹{mean_salary:.2f}")
print(f"Standard Deviation: ₹{std_salary:.2f}")

print("\nSalary and Z-Scores")
print(df)

print("\nOutliers (|Z| > 3)")
if len(outliers) == 0:
    print("No Outliers Found")
else:
    print(outliers)

# ----------------------------
# Histogram
# ----------------------------
plt.figure(figsize=(8,5))
plt.hist(df["Salary"], bins=5)

plt.axvline(
    mean_salary,
    linestyle="--",
    label=f"Mean = {mean_salary:.0f}"
)

plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.title("Employee Salary Distribution")
plt.legend()

plt.show()

# ----------------------------
# Business Interpretation
# ----------------------------
print("\n" + "=" * 50)
print("BUSINESS INTERPRETATION")
print("=" * 50)

print(f"Average employee salary is ₹{mean_salary:.0f}.")
print(f"Salary variation (SD) is ₹{std_salary:.0f}.")

if len(outliers) == 0:
    print("No employee salary is considered an outlier.")
else:
    print("Some employees have unusually high/low salaries.")

print(
    "Most employees fall within the normal salary range, "
    "while higher salaries may indicate senior-level positions."
)