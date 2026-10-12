import streamlit as st
import requests

# FastAPI backend URL
BASE_URL = "http://127.0.0.1:8000/api"

st.set_page_config(
    page_title="Student Management",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Student Management System")

menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Create Student",
        "View All Students",
        "Get Student By ID"
    ]
)

# -----------------------------------
# 1. Create Student - POST API
# -----------------------------------
if menu == "Create Student":

    st.subheader("Create Student")

    with st.form("student_form"):
        name = st.text_input("Student Name")
        course = st.text_input("Course")
        fee = st.number_input(
            "Fee",
            min_value=0.01,
            step=100.0
        )

        submit = st.form_submit_button("Create Student")

    if submit:
        student = {
            "name": name,
            "course": course,
            "fee": fee
        }

        try:
            response = requests.post(
                f"{BASE_URL}/student",
                json=student,
                timeout=10
            )

            if response.status_code == 201:
                st.success("Student created successfully!")
                st.json(response.json())
            else:
                st.error(
                    f"Error {response.status_code}"
                )
                st.json(response.json())

        except requests.exceptions.RequestException as e:
            st.error(f"Could not connect to FastAPI: {e}")


# -----------------------------------
# 2. Get All Students - GET API
# -----------------------------------
elif menu == "View All Students":

    st.subheader("All Students")

    if st.button("Load Students"):
        try:
            response = requests.get(
                f"{BASE_URL}/students",
                timeout=10
            )

            response.raise_for_status()
            students = response.json()

            if students:
                st.dataframe(
                    students,
                    use_container_width=True
                )
            else:
                st.info("No students found.")

        except requests.exceptions.RequestException as e:
            st.error(f"Failed to fetch students: {e}")


# -----------------------------------
# 3. Get Student By ID - GET API
# -----------------------------------
elif menu == "Get Student By ID":

    st.subheader("Search Student")

    student_id = st.number_input(
        "Enter Student ID",
        min_value=1,
        step=1
    )

    if st.button("Search Student"):
        try:
            response = requests.get(
                f"{BASE_URL}/students/{student_id}",
                timeout=10
            )

            if response.status_code == 200:
                st.success("Student found!")
                st.json(response.json())

            elif response.status_code == 404:
                st.warning("Student not found.")

            else:
                st.error(
                    f"Error {response.status_code}"
                )
                st.json(response.json())

        except requests.exceptions.RequestException as e:
            st.error(f"Could not connect to FastAPI: {e}")