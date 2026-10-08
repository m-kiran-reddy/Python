import streamlit as st

st.title("Employee Preferences")
department = st.selectbox("Department", ["IT","HR","Finance","Sales"])
work_mode = st.radio("Work Mode", ["office","Hybrid","Remote"])
skills = st.multiselect("Skills", ["Java","Python","SQL","AWS","Docker"])

if st.button("Submit"):
    st.text(f"Department: {department}")
    st.text(f"Work Mode: {work_mode}")
    st.text(f"Skills: {', '.join([str(val) for val in skills])}")