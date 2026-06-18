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

# Convert to Pandas Series
s = pd.Series(salary)

# Task 1: Mean
print("Mean:", s.mean())

# Task 2: Median
print("Median:", s.median())

# Task 3: Mode
print("Mode:")
print(s.mode())

# Task 4: Q1 (25th Percentile)
print("Q1:", s.quantile(0.25))

# Task 5: Q3 (75th Percentile)
print("Q3:", s.quantile(0.75))

# Task 6: 90th Percentile
print("90th Percentile:", s.quantile(0.90))

# Additional Statistics
print("\nSummary Statistics:")
print(s.describe())

# Task 7: Histogram
plt.figure(figsize=(8, 5))
plt.hist(s, bins=5)

plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")

plt.show()