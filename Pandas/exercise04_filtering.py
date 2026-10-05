import pandas as pd
employees = {
    "emp_id" : [101,102,103,104,105],
    "emp_name" : ["Kiran","Ravi","Sita","Anil","Raj"],
    "department" : ["IT","HR","IT","Finance","IT"],
    "salary": [75000,65000,85000,55000,95000]
}

df = pd.DataFrame(employees)
print(f"Salary > 70,000: {df[df.salary > 70000]} ")
print(f"Salary < 70,000: {df[df.salary < 70000]} ")
print(f"Greater than or equal to 75,000: {df[df.salary >= 75000]} ")
print(f"IT department: {df[df.department == 'IT']} ")
print(f"HR department: {df[df.department == 'HR']} ")
print(f"emp_name and salary of employees whose salary is greater than 70,000: {df[df.salary > 70000][['emp_name', 'salary']]} ")