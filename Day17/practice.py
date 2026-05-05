import pandas as pd 
data = {
    "dept": ["IT", "HR", "IT"],
    "salary": [50000, 40000, 60000]
}
# ✅ Tasks:

# ✔ Create salary category (>50k)
# ✔ Apply label encoding
# ✔ Apply one-hot encoding
df = pd.DataFrame(data)
# create salary category
df["salary_category"] = df["salary"].apply(lambda x: "High" if x > 50000 else "Low")
print(df)
# label encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["salary_category_encoded"] = le.fit_transform(df["salary_category"]) 
print(df)
# one-hot encoding
df_one_hot = pd.get_dummies(df["salary_category"], prefix="salary_cat")
df = pd.concat([df, df_one_hot], axis=1)
print(df)