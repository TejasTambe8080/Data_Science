import pandas as pd 
import numpy as np 

data = {
    "salary": [30000, 40000, 50000, 60000, 500000]
}

df = pd.DataFrame(data)
# Detect outliers using IQR
Q1 = df["salary"].quantile(0.25)    
Q3 = df["salary"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")
# Remove outliers   
df_no_outliers = df[(df["salary"] >= lower_bound) & (df["salary"] <= upper_bound)]
print(df_no_outliers)
# Apply log transform
df_no_outliers["salary_log"] = np.log(df_no_outliers["salary"])
print(df_no_outliers)
# Check skewness before & after
skew_before = df["salary"].skew()
skew_after = df_no_outliers["salary_log"].skew()
print(f"Skewness before log transform: {skew_before}")
print(f"Skewness after log transform: {skew_after}")