import streamlit as st
import pandas as pd

emp_data = {
    "emp_name" : ["Kiran","Ravi","Sita","Anil","Raj"],
    "department" : ["IT","HR","IT","Finance","IT"],
    "salary" : [75000,65000,85000,55000,95000]
}
emp_df = pd.DataFrame(emp_data)
st.title("Employee Data")
st.dataframe(emp_df)