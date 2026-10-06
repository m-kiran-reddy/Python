import matplotlib.pyplot as plt

departments = ["IT", "HR", "Finance", "Sales"]
employees = [25, 15, 10, 20]

plt.barh(departments, employees)
plt.title("Employees by Department")
plt.xlabel("Number of Employees")
plt.ylabel("Department")

plt.show()