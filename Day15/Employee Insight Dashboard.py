import seaborn as sns 
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "dept": ["IT", "HR", "IT", "HR", "IT"],
    "salary": [50000, 40000, 60000, 45000, 70000]
}

df = pd.DataFrame(data)

sns.histplot(df["salary"], kde=True)
plt.show()

sns.boxplot(x=df["salary"])
plt.show()

## count plot 
sns.countplot(x=df["dept"])
plt.show()
##Heatmap
sns.heatmap(df.select_dtypes(include='number').corr(), annot=True)
plt.show()