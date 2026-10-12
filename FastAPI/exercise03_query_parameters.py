from typing import Optional

from fastapi import FastAPI,  Query

app = FastAPI()

emp_list = [
        {
            "emp_id": 101,
            "emp_name": "Kiran",
            "department": "IT",
            "salary": 75000
        },
        {
            "emp_id": 102,
            "emp_name": "Ravi",
            "department": "HR",
            "salary": 65000
        },
        {
            "emp_id": 103,
            "emp_name": "Sita",
            "department": "Finance",
            "salary": 85000
        }
    ]

@app.get("/employees")
def get_employees(
    department: Optional[str] = Query(
        None, description="Filter employees by department name"
    )
):
    if department:
        filtered_employees = [
            emp
            for emp in emp_list
            if emp["department"].lower() == department.lower()
        ]
        return filtered_employees

    return emp_list