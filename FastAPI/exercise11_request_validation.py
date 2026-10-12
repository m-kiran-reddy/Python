from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

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

class Employee(BaseModel):
    emp_id: int = Field(..., gt = 0)
    emp_name: str = Field(..., min_length=3)
    department: str = Field(..., min_length=2)
    salary: float= Field(..., gt = 0)

@app.post("/employees")
def save_employee_details(employee: Employee):
    emp_dict = employee.model_dump()
    filter_emp = next((emp for emp in emp_list if emp["emp_id"] == emp_dict["emp_id"]), None)
    if filter_emp is not None:
        raise HTTPException(status_code=409, detail="emp_id already exists")
    emp_list.append(emp_dict)
    return emp_dict
