import pandas as pd

employees = {
    "emp_id": [101, 102, 103, 104, 105, 106, 107, 108],
    "emp_name": ["Kiran", "Ravi", "Sita", "Anil", "Raj", "John", "Priya", "Arun"],
    "department": ["IT", "HR", "IT", "Finance", "IT", "HR", "Finance", "IT"],
    "salary": [75000, 65000, 85000, 55000, 95000, 70000, 60000, 80000],
    "joining_date": [
        "2021-03-10", "2022-06-15", "2020-01-20", "2023-08-05",
        "2021-11-25", "2022-02-10", "2023-01-15", "2020-07-20"
    ]
}

emp_df = pd.DataFrame(employees)
emp_df['joining_date'] = pd.to_datetime(emp_df['joining_date'])
emp_df['joining_year'] = emp_df['joining_date'].dt.year

print(f"employees with salary greater than 70,000: {emp_df[emp_df['salary']>70000]}")

df1 = emp_df.groupby('department')
print(df1.agg(average_salary  =("salary", "mean"),highest_salary = ("salary", "max")))

print(f"employee with the highest salary overall.: {emp_df.loc[emp_df['salary'].idxmax()]}")

print(f"employees after sorting by salary in descending order: {emp_df.sort_values(by='salary', ascending=False)}")

print(f"employees joined after 2021-01-01: {emp_df[ emp_df['joining_date'] > '2021-01-01']}")

def salary_grade(salary):
    if salary >= 80000:
        return "A"
    elif salary >= 70000:
        return "B"
    elif salary < 70000:
        return "C"
    return None

emp_df['salary_grade'] = emp_df['salary'].apply(salary_grade)

print(f"Final DataFrame: {emp_df}")
