import pandas as pd 
 
data = {
    "name": ["A", "B", "C", "D", "E"],
    "dept": ["IT", "HR", "IT", "HR", "IT"],
    "salary": [50000, 40000, 60000, 45000, 70000]
}

df = pd.DataFrame(data)

info = df.info()
print("Information about the Dataframe:")
print(info)

avg_salary = df["salary"].mean()
print("Average Salary:", avg_salary)    

## Dept-wise salary
Dept_wise_salary  = df.groupby("dept" )["salary"].mean()
print("Department-wise Average Salary:")            
print(Dept_wise_salary)

# ✔ Highest paid employee
# ✔ Most common dept
highest_paid_employee = df[df["salary"] == df["salary"].max()]
print("Highest Paid Employee:") 
print(highest_paid_employee["name"].values[0])
most_common_dept = df["dept"].value_counts().idxmax()
print("Most Common Department:", most_common_dept)      
