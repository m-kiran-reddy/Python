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

@app.get("/employees/search")
def get_employees(
    department: Optional[str] = Query(
        None, min_length=2, max_length=20
    ),
    min_salary: Optional[int] = Query(
        None ,ge=0
    )
):

    if department is not None and min_salary is not None:
        filtered_employees = [
            emp
            for emp in emp_list
            if emp["department"] == department and emp["salary"] >= min_salary
        ]
        return filtered_employees
    elif department is not None:
        filtered_employees = [
            emp
            for emp in emp_list
            if emp["department"] == department
        ]
        return filtered_employees
    elif min_salary is not None:
         filtered_employees = [
                emp
                for emp in emp_list
                if emp["salary"] >= min_salary
         ]
         return filtered_employees
    else:
        return emp_list