from typing import Optional
from fastapi import FastAPI, Query, HTTPException

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


@app.get("/employees/sort")
def sort_employees(sort_by: Optional[str] = Query( "salary"),
                   order:  Optional[str] = Query( "asc")):
    allowed_sort_by_list = ["salary", "emp_name"]
    allowed_order_list = ["asc", "desc"]

    if sort_by not in allowed_sort_by_list:
        raise HTTPException(status_code=400, detail="unsupported sort_by")

    if order not in allowed_order_list:
        raise HTTPException(status_code=400, detail="unsupported order")

    if not sort_by:
        return emp_list
    reverse_order = True if order == "desc" else False

    sorted_employees = sorted(
        emp_list, key=lambda x: x[sort_by], reverse=reverse_order
    )
    return sorted_employees
