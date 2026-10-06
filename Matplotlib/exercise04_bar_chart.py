import matplotlib.pyplot as plt

departments = ["IT", "HR", "Finance", "Sales"]
employees = [25, 15, 10, 20]

plt.bar(departments, employees)

plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.show()