import pandas as pd 
import matplotlib.pyplot as plt 

data = {
    "department":["IT","HR","Sales","IT","HR","Sales","IT","HR","Sales","IT"],
    "experience":[1,2,3,4,5,6,7,8,9,10],
    "salary":[30000,35000,40000,50000,60000,65000,80000,85000,90000,110000],
    "performance":[60,65,70,75,80,82,88,90,93,98]
}

df = pd.DataFrame(data)
## ALL Structure Analysis 
df.shape
df.info()
df.describe()

## Missing Values 
df.isnull().sum()

## Duplicated values 
df.duplicated().sum()
## unique Values 
df.nunique()
## BUSINESS ANALYSIS 
#1 Average Salary by Department
avg_salary_dept = df.groupby("department")["salary"].mean()
print(avg_salary_dept)
#2 Average performance by department
avg_per_dept = df.groupby("department")["performance"].mean()
print(avg_per_dept)
#3 Highest paid department
max_salary_dept = df.groupby("department")["salary"].max()
print(max_salary_dept)
#4 Highest Performance 
max_perf_dept = df.groupby("department")["performance"].max()

#5Department contributing most value
dept_value = df.groupby("department")["salary"].sum()
print(dept_value)

df.corr(numeric_only=True)

## BAR CHART dept vs avg salary
avg_salary_dept.plot(kind="bar")
plt.title("Department vs Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.show()

## SCATTER PLOT experience vs salary
plt.scatter(df["experience"],df["salary"])
plt.title("Experience vs Salary")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()
## Scatter Plot experience vs performance
plt.scatter(df["experience"],df["performance"])
plt.title("experience vs performance")
plt.xlabel("Experience")
plt.ylabel("Performance")   
plt.show()
#Correlation Heatmap
import seaborn as sns
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")    
plt.show()
