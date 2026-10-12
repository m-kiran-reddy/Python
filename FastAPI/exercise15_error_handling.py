from fastapi import FastAPI, HTTPException

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


@app.get("/employees/{emp_id}")
def get_employee(emp_id: int):
    for emp in emp_list:
        if emp["emp_id"] == emp_id:
            return emp

    raise HTTPException(status_code=404, detail="Employee not found")


@app.get("/error-demo")
def error_demo():
    raise HTTPException(status_code=400, detail="Invalid request")