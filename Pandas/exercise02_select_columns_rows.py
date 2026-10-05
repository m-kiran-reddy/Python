import pandas as pd
employees = {
    "emp_id" : [101,102,103,104,105],
    "emp_name" : ["Kiran","Ravi","Sita","Anil","Raj"],
    "department" : ["IT","HR","IT","Finance","IT"],
    "salary": [75000,65000,85000,55000,95000]
}

df = pd.DataFrame(employees)
print(f"Emp Names : {df['emp_name']}")
print(f"Salaries  : {df['salary']}")
print(f"Emp Names & Salaries: {df[['emp_name','salary']]}")
print(f"First Employee Row: {df.head(1)}")
print(f"Third Employee Row: {df[2::3]}")
print(f"First three employee rows: {df.head(3)}")
print(f"Last two employee rows: {df.tail(2)}")