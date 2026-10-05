import pandas as pd

employees = {
    "emp_id": [101, 102, 103, 104, 105],
    "emp_name": ["Kiran", "Ravi", "Sita", "Anil", "Raj"],
    "department": ["IT", "HR", "IT", "Finance", "IT"],
    "salary": [75000, 65000, 85000, 55000, 95000]
}

emp_df = pd.DataFrame(employees)
emp_df.to_csv("employees.csv",index=False)

df_from_csv = pd.read_csv("employees.csv")
print(f"data from csv: {df_from_csv}")

print(f"shape of the csv: {df_from_csv.shape}")