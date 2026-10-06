import matplotlib.pyplot as plt
import pandas as pd

data = {
    "emp_name": ["Kiran", "Ravi", "Sita", "Anil", "Raj"],
    "department": ["IT", "HR", "IT", "Finance", "IT"],
    "salary": [75000, 65000, 85000, 55000, 95000],
    "experience": [5, 4, 6, 3, 8]
}

df = pd.DataFrame(data)


fig, ax = plt.subplots(1, 3)

#Plot1 Salary By Employee
ax[0].bar(df["emp_name"], df["salary"])
ax[0].set_title("Employee Salary")
ax[0].set_xlabel("Employee Name")
ax[0].set_ylabel("Salary")


#Salary vs Experience
ax[1].scatter(df["experience"], df["salary"])
ax[1].set_title("Salary vs Experience")
ax[1].set_xlabel("Experience")
ax[1].set_ylabel("Salary")

#Employees by Department
department_counts = df.groupby("department").size()
ax[2].bar(department_counts.index,department_counts)
ax[2].set_title("Employees by Department")
ax[2].set_xlabel("Department")
ax[2].set_ylabel("Number of Employees")

plt.show()