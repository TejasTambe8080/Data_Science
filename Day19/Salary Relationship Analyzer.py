import pandas as pd
import matplotlib.pyplot as plt

data = {
    "experience": [1,2,3,4,5],
    "salary": [20000,30000,40000,50000,60000],
    "age": [22,25,28,30,35]
}

df = pd.DataFrame(data)

# 1️⃣ Compute correlation
corr = df.corr()
print("Correlation Matrix:\n", corr)

# 2️⃣ Plot heatmap
plt.imshow(corr)
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns)
plt.yticks(range(len(corr.columns)), corr.columns)

# Add values on heatmap
for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        plt.text(j, i, round(corr.iloc[i, j], 2),
                 ha='center', va='center')

plt.title("Correlation Heatmap")
plt.show()