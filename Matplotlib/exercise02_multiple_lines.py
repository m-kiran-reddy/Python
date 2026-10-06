import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]

sales_2025 = [100, 120, 90, 140, 160]
sales_2026 = [110, 130, 100, 150, 180]

plt.plot(days, sales_2025)
plt.plot(days, sales_2026)

plt.title("Sales Comparison")
plt.xlabel("Day")
plt.ylabel("Sales")

plt.legend(["2025", "2026"])

plt.show()