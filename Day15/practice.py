import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "dept": ["IT", "HR", "IT", "HR", "IT"],
    "salary": [50000, 40000, 60000, 45000, 70000]
}

df = pd.DataFrame(data)

# Histogram
sns.histplot(df["salary"], kde=True)
plt.show()

# Box plot (outliers)
sns.boxplot(x=df["salary"])
plt.show()

# Count plot
sns.countplot(x=df["dept"])
plt.show()

# Heatmap (fixed)
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True)
plt.show()