from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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
    emp_id: int
    emp_name: str
    department: str
    salary: int

@app.get("/employees/{emp_id}", response_model=Employee)
def get_employees(emp_id: int):
    filter_emp = next((emp for emp in emp_list if emp["emp_id"] == emp_id),None)
    if filter_emp is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return filter_emp