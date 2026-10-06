import matplotlib.pyplot as plt

experience = [1, 2, 3, 4, 5, 6, 7, 8]
salary = [40000, 45000, 50000, 58000, 65000, 72000, 80000, 90000]

plt.scatter(experience, salary)

plt.title("Experience vs Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.show()