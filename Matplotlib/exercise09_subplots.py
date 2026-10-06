import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [120, 150, 130, 180, 200]

expenses = [80, 90, 100, 110, 120]

fig, ax = plt.subplots(1, 2)
ax[0].plot(months, sales)
ax[0].set_title("Monthly Sales")
ax[0].set_xlabel("Month")
ax[0].set_ylabel("Sales")


ax[1].plot(months, expenses)
ax[1].set_title("Monthly Expenses")
ax[1].set_xlabel("Month")
ax[1].set_ylabel("Expenses")

plt.show()