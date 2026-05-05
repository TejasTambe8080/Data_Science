import pandas as pd

data = {
    "dept": ["IT", "HR", "IT", "HR"],
    "salary": [50000, 40000, 60000, 45000]
}

df = pd.DataFrame(data)

# 1️⃣ Create salary category
df["salary_category"] = df["salary"].apply(lambda x: "High" if x > 50000 else "Low")

# 2️⃣ Encode department (One-Hot Encoding)
dept_encoded = pd.get_dummies(df["dept"], prefix="dept")
df = pd.concat([df, dept_encoded], axis=1)

# 3️⃣ Add new feature: high salary (1/0)
df["high_salary"] = df["salary"].apply(lambda x: 1 if x > 50000 else 0)

print(df)