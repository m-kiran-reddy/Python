import streamlit as st

st.title("Employee Registration")

name = st.text_input("Enter Employee Name")
experience = st.number_input("Enter Experience", min_value=0, max_value=30)

if st.button("Submit"):
    st.text(f"Employee Name: {name}")
    st.text(f"Experience: {experience} years")