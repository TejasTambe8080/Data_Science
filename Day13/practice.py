import pandas as pd 

data = {
    "name": ["A", "B", "C", "D"],
    "dept": ["IT", "HR", "IT", "HR"],
    "salary": [50000, 40000, 60000, 45000]
}

df = pd.DataFrame(data)

shape = df.shape
print("Shape of the Dataframe ",shape)

## Datatypes 
datatypes = df.dtypes ## df.info() also gives datatypes but it also gives some other information like memory usage and number of non-null values in each column
print("Datatypes of the columns ", datatypes)

avg_salary = df["salary"].mean()
print("Average Salary:", avg_salary)
## Department wise salary analysis
dept_salary = df.groupby("dept")["salary"].mean()
print("Average Salary by Department:")
print(dept_salary)
## Count of employees in each department
dept_count = df["dept"].value_counts()
print("Number of employees in each department:")    
print(dept_count)