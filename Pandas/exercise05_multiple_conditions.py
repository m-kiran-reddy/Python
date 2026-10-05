import pandas as pd
employees = {
    "emp_id" : [101,102,103,104,105],
    "emp_name" : ["Kiran","Ravi","Sita","Anil","Raj"],
    "department" : ["IT","HR","IT","Finance","IT"],
    "salary": [75000,65000,85000,55000,95000]
}

df = pd.DataFrame(employees)
print(f"Salary > 70,000 AND department is IT: {df[(df.salary > 70000) & (df.department == 'IT')]} ")
print(f"Salary > 70,000 OR department is HR: {df[(df.salary > 70000) | (df.department == 'HR')]} ")
print(f"between 60,000 and 90,000, inclusive: {df[(df.salary >= 60000) & (df.salary <= 90000)]}")
print(f"employees who are not in the IT department: {df[df.department!='IT']} ")
print(f"emp_name and salary for employees who: Salary > 70,000 AND department is IT: {df[(df.salary > 70000) & (df.department == 'IT')][['emp_name','salary']]}")
