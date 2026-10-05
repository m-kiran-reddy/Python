import pandas as pd

employees = {
    "emp_id": [101, 102, 103, 104, 105],
    "emp_name": ["Kiran", "Ravi", "Sita", "Anil", "Raj"],
    "department": ["IT", "HR", "IT", "Finance", "IT"]
}

salaries = {
    "emp_id": [101, 102, 103, 104, 105],
    "salary": [75000, 65000, 85000, 55000, 95000]
}

emp_df = pd.DataFrame(employees)
salary_df = pd.DataFrame(salaries)

merged_df = pd.merge(emp_df, salary_df, on="emp_id")
print(merged_df)
