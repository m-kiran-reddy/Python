import streamlit as st
import pandas as pd

st.title("Employee CSV Viewer")
uploaded_file  = st.file_uploader("Upload Employee CSV", type=["csv"])

if uploaded_file  is None:
    st.text("Please upload a CSV file.")
else:
    st.dataframe(pd.read_csv(uploaded_file))
