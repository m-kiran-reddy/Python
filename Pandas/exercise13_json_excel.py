import pandas as pd

employees = {
    "emp_id": [101, 102, 103, 104, 105],
    "emp_name": ["Kiran", "Ravi", "Sita", "Anil", "Raj"],
    "department": ["IT", "HR", "IT", "Finance", "IT"],
    "salary": [75000, 65000, 85000, 55000, 95000]
}

employees_df = pd.DataFrame(employees)
employees_df.to_json("employees.json")

df_from_json = pd.read_json("employees.json")
print(f"data from employees.json file: {df_from_json}")

employees_df.to_excel("employees.xlsx")
df_from_excel = pd.read_excel("employees.xlsx")
print(f"data from employees.xlsx file: {df_from_excel}")
