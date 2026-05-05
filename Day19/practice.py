import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "experience": [1,2,3,4,5],
    "salary": [20000,30000,40000,50000,60000],
    "age": [22,25,28,30,35]
}
# ✅ Tasks:

# ✔ Calculate correlation matrix
# ✔ Find strongest relationship
# ✔ Plot heatmap
df = pd.DataFrame(data)

# Calculate correlation matrix
correlation_matrix = df.corr()
print("Correlation Matrix:")
print(correlation_matrix)
# Find strongest relationship
strongest_relationship = correlation_matrix.unstack().sort_values(ascending=False)
# plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlation Heatmap")    
print(strongest_relationship)
plt.show()