import pandas as pd
employees = {
    "emp_id" : [101,102,103,104,105],
    "emp_name" : ["Kiran","Ravi","Sita","Anil","Raj"],
    "department" : ["IT","HR","IT","Finance","IT"],
    "salary": [75000,65000,85000,55000,95000]
}

df = pd.DataFrame(employees)

print(f"employees by salary in ascending order: {df.sort_values(by='salary', ascending=True)}")
print(f"employees by salary in descending order: {df.sort_values(by='salary', ascending=False)}")
print(f"employees by emp_name in alphabetically: {df.sort_values(by='emp_name')}")
print(f"employees by department in alphabetically: {df.sort_values(by='department')}")
print(f"employees by department in ascending order and within each department, sort salary descending: {df.sort_values( by=['department','salary'], ascending=[True,False]) }")
df1 = df.sort_values(by='salary', ascending=False)
print(f"employees by salary in descending order: {df1}")
print(f"original df after the sorting operations: {df}")