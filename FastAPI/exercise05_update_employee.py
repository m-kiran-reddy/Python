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
    emp_name: str
    department: str
    salary: int

@app.put("/employees/{emp_id}")
def update_employee_details(emp_id: int, employee: Employee):
    filter_emp = next((emp for emp in emp_list if emp["emp_id"] == emp_id), None)
    if filter_emp is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    else:
        emp = employee.model_dump()
        filter_emp["emp_name"] = emp["emp_name"]
        filter_emp["department"] = emp["department"]
        filter_emp["salary"] = emp["salary"]
        return filter_emp