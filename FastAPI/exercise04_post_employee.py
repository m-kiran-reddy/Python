from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

emp_list = []

class Employee(BaseModel):
    emp_id: int = Field(...)
    emp_name: str = Field(...)
    department: str = Field(...)
    salary: float= Field(..., gt = 0)

@app.post("/employees")
def save_employee_details(employee: Employee):
    emp = employee.model_dump()
    emp_list.append(emp)
    return emp

