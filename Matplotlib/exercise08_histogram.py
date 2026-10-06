import matplotlib.pyplot as plt

salaries = [40000, 45000, 50000, 52000, 55000, 58000, 60000, 62000,
            65000, 68000, 70000, 72000, 75000, 80000, 85000, 90000]

plt.hist(salaries, bins=5)
plt.title("Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Number of Employees")
plt.show()