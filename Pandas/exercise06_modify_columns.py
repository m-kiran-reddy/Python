import pandas as pd
employees = {
    "emp_id" : [101,102,103,104,105],
    "emp_name" : ["Kiran","Ravi","Sita","Anil","Raj"],
    "department" : ["IT","HR","IT","Finance","IT"],
    "salary": [75000,65000,85000,55000,95000]
}

df = pd.DataFrame(employees)
df["bonus"] = [7500, 6500, 8500, 5500, 9500]
print(f"After Adding Bonus Column: {df}")

df["annual_salary"] = df["salary"] * 12
print(f"After Adding Annual Salary Column: {df}")

df["bonus"] = df["bonus"] + df["bonus"] * 0.10
print(f"After increasing every bonus by 10%: {df}")

df["total_compensation"] = df["annual_salary"] + df["bonus"]
print(f"After adding Total Compensation Column: {df}")

df.drop(["bonus"],inplace=True)

print(f"Final DataFrame: {df}")