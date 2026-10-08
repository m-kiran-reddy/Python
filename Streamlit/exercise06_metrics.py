import streamlit as st
import pandas as pd

emp_data = {
    "emp_name" : ["Kiran","Ravi","Sita","Anil","Raj"],
    "department" : ["IT","HR","IT","Finance","IT"],
    "salary" : [75000,65000,85000,55000,95000]
}
emp_df = pd.DataFrame(emp_data)
st.title("Employee Metrics")

total_employees = len(emp_df)
average_salary = emp_df["salary"].mean()
highest_salary = emp_df["salary"].max()

columns = st.columns(3)
columns[0].metric("Total Employees", total_employees)
columns[1].metric("Average Salary", average_salary)
columns[2].metric("Highest Salary", highest_salary)