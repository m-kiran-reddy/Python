from fastapi import FastAPI, Query

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
    skip: int = Query(0, ge=0, description="Number of employees to skip"),
    limit: int = Query(2, ge=1, description="Max number of employees to return")
):
    return emp_list[skip: skip + limit]


