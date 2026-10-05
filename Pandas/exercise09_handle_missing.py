import pandas as pd
employees = {
    "emp_id": [101, 102, 103, 104, 105],
    "emp_name": ["Kiran", "Ravi", None, "Anil", "Raj"],
    "department": ["IT", "HR", "IT", None, "IT"],
    "salary": [75000, None, 85000, 55000, None]
}

df = pd.DataFrame(employees)
avg_sal = df['salary'].mean()
df['salary'] = df['salary'].fillna(avg_sal)
print(f"After filling missing salary values with the average salary: {df}")
df['department'] = df['department'].fillna('Unknown')
print(f"After filling missing department values with the \"Unknown\": {df}")
df['emp_name'] = df['emp_name'].fillna('Unknown')
print(f"After filling missing emp_name values with the \"Unknown\": {df}")
print(f"Verify zero missing values: {df.isna().sum()}")


df['emp_name'] = df['emp_name'].str.upper()
print(f"After converting all emp_names to uppercase: {df}")

df['department'] = df['department'].str.lower()
print(f"After converting all department to lowercase: {df}")

df['name_length'] = df['emp_name'].str.len()
print(f"After Adding name length column: {df}")

df['name_with_dept'] = df['emp_name']+"-"+df['department']
print(f"After Adding name_with_dept column: {df}")

print(f"employee whose name contain \"A\": {df[df['emp_name'].str.contains('A')][['emp_id','emp_name']]}")

print(df)


def salary_grade(salary):
    if salary >= 80000:
        return "A"
    elif salary >= 70000:
        return "B"
    elif salary < 70000:
        return "C"
    return None
df['salary_grade'] = df['salary'].apply(salary_grade)
print(f"After adding salary_grade column: {df}")

def salary_after_hike(grade,salary):
    if grade == "A":
      return salary + salary * 0.05
    elif grade == "B":
      return salary + salary * 0.10
    elif grade == "C":
      return salary + salary * 0.15
    return None
df['salary_after_hike'] = df[['salary_grade', 'salary']].apply(
    lambda row: salary_after_hike(row["salary_grade"], row["salary"]),
    axis=1
)
print(f"After adding salary_after_hike column: {df}")

employees = {
    "emp_id" : [101,102,103,104,105],
    "emp_name" : ["Kiran","Ravi","Sita","Anil","Raj"],
    "department" : ["IT","HR","IT","Finance","IT"],
    "salary": [75000,65000,85000,55000,95000]
}
df = pd.DataFrame(employees)
df1 = df.groupby('department')

print(f"Total Salary by each department: {df1['salary'].sum()}")
print(f"Average Salary by each department: {df1['salary'].mean()}")
print(f"Highest Salary by each department: {df1['salary'].max()}")
print(f"Employee count by each department: {df1['emp_id'].count()}")

print(df1.agg(total_salary=("salary", "sum"),average_salary  =("salary", "mean"),min_salary  =("salary", "min"),max_salary =("salary", "max")))


employees = {
    "emp_id" : [101,102,103,104,105],
    "emp_name" : ["Kiran","Ravi","Sita","Anil","Raj"],
    "department" : ["IT","HR","IT","Finance","IT"],
    "salary": [75000,65000,85000,55000,95000]
}
df = pd.DataFrame(employees)
df1 = df.groupby(['department','emp_name'])
print(df1.agg(total_salary=("salary", "sum"),average_salary  =("salary", "mean")))
