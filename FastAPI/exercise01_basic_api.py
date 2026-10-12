from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_msg():
    return  {
        "message": "Welcome to my first FastAPI application"
    }

@app.get("/employees")
def get_employee_details():
    emp_list = [
        {
            "emp_id": 101,
            "emp_name": "Kiran",
            "department": "IT"
        },
        {
            "emp_id": 102,
            "emp_name": "Ravi",
            "department": "HR"
        },
        {
            "emp_id": 103,
            "emp_name": "Sita",
            "department": "Finance"
        }
    ]
    return  emp_list