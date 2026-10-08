import streamlit as st
import pandas as pd
from matplotlib.pyplot import xlabel

emp_data = {
    "emp_name" : ["Kiran","Ravi","Sita","Anil","Raj"],
    "department" : ["IT","HR","IT","Finance","IT"],
    "salary" : [75000,65000,85000,55000,95000]
}
emp_df = pd.DataFrame(emp_data)
st.title("Employee Dashboard")

total_employees_count = len(emp_df)
avg_salary = emp_df["salary"].mean()
highest_salary = emp_df["salary"].max()

columns = st.columns(3)
columns[0].metric("Total Employees", total_employees_count)
columns[1].metric("Average salary", avg_salary)
columns[2].metric("Highest salary", highest_salary)

department = st.selectbox("Select Department", ["All","IT","HR","Finance"])
filter_df = emp_df[emp_df["department"] == department]

if department == "All":
    filter_df = emp_df
st.dataframe(filter_df)

st.bar_chart(data=filter_df, x="emp_name", y="salary", x_label="Employee Name", y_label="Salary")
