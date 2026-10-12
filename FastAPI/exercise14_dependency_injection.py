from fastapi import FastAPI, Depends

from exercise02_path_parameters import emp_list

app = FastAPI()

def get_employee_list():
    return emp_list

@app.get("/employees")
def get_employees(employees = Depends(get_employee_list)):
     return employees

@app.get("/employees/count")
def get_employees(employees = Depends(get_employee_list)):
     return {
         "total_employees":len(employees)
     }