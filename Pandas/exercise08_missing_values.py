import pandas as pd
employees = {
    "emp_id": [101, 102, 103, 104, 105],
    "emp_name": ["Kiran", "Ravi", None, "Anil", "Raj"],
    "department": ["IT", "HR", "IT", None, "IT"],
    "salary": [75000, None, 85000, 55000, None]
}

df = pd.DataFrame(employees)
print(f"{df}")
print(f"Missing values per column: {df.isna().sum()}")
print(f"The total number of missing values in the entire DataFrame: {df.isna().sum().sum()}")
print(f"The rows where salary is missing: {df[df['salary'].isna()]}")
print(f"The rows where salary is NOT missing: {df[df['salary'].notna()]}")
print(f"The rows where department is missing: {df[df['department'].isna()]}")