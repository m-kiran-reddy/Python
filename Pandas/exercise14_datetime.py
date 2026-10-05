import pandas as pd

employees = {
    "emp_id": [101, 102, 103, 104, 105],
    "emp_name": ["Kiran", "Ravi", "Sita", "Anil", "Raj"],
    "joining_date": [
        "2021-03-10",
        "2022-06-15",
        "2020-01-20",
        "2023-08-05",
        "2021-11-25"
    ]
}

employees_df = pd.DataFrame(employees)
employees_df['joining_date'] = pd.to_datetime(employees_df['joining_date'])
employees_df['joining_year'] = employees_df['joining_date'].dt.year
employees_df['joining_month'] = employees_df['joining_date'].dt.month
employees_df['joining_day'] = employees_df['joining_date'].dt.day
print(employees_df)
employees_df = employees_df[employees_df['joining_date'] > '2021-01-01']
print(employees_df)