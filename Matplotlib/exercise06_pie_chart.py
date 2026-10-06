import matplotlib.pyplot as plt

departments = ["IT", "HR", "Finance", "Sales"]
employees = [25, 15, 10, 20]

plt.pie(employees, labels=departments, autopct="%1.1f%%")
plt.title("Employee Distribution")
plt.show()