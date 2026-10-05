import pandas as pd
employees = {
    "emp_id" : [101,102,103,104,105],
    "emp_name" : ["Kiran","Ravi","Sita","Anil","Raj"],
    "department" : ["IT","HR","IT","Finance","IT"],
    "salary": [75000,65000,85000,55000,95000]
}

df = pd.DataFrame(employees)
#loc
print(f"first employee: {df.loc[0]}")
print(f"third employee: {df.loc[2]}")
print(f"employees from index 1 through 3: {df.loc[1:3]}")
print(f"Employee Names And Salary for the first three employees: {df.loc[1:3, ['emp_name', 'salary']]}")
#iloc
print(f"first employee: {df.iloc[0]}")
print(f"third employee: {df.iloc[2]}")
print(f"first three employees: {df.iloc[0:3]}")
print(f"Employee Names And Salary for the first three employees: {df.iloc[0:3][['emp_name', 'salary']]}")
