import seaborn as sns
import matplotlib.pyplot as plt

data = [10,20,20,30,30,30]

sns.histplot(data, kde=True)
plt.show()


## BOX plot 
sns.boxplot(x=data)
plt.show()

## count Plot 
dept = ["IT", "HR", "IT", "HR", "IT"]

sns.countplot(x=dept)
plt.show()

# 4. Heatmap
import pandas as pd

df = pd.DataFrame({
    "a": [1,2,3],
    "b": [4,5,6]
})

sns.heatmap(df.corr(), annot=True)
plt.show()

x = [1,2,3]
y = [10,20,30]

sns.scatterplot(x=x, y=y)
plt.show()