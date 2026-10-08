import streamlit as st
import pandas as pd

emp_data = {
    "emp_name" : ["Kiran","Ravi","Sita","Anil","Raj"],
    "department" : ["IT","HR","IT","Finance","IT"],
    "salary" : [75000,65000,85000,55000,95000]
}
emp_df = pd.DataFrame(emp_data)
st.title("Employee Filter")
department = st.selectbox("Department",["All","IT","HR","Finance"])

filter_emp_df = emp_df[emp_df["department"] == department]

if department == "All":
    st.dataframe(emp_df)
else:
    st.dataframe(filter_emp_df)