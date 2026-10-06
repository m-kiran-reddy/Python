import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

product_a = [120, 150, 140, 180, 200, 220]
product_b = [100, 130, 160, 150, 190, 210]
product_c = [80, 110, 120, 140, 170, 180]

plt.plot(months, product_a, marker="o", label="Product A")
plt.plot(months, product_b, marker="s", label="Product B")
plt.plot(months, product_c, marker="^", label="Product C")

plt.title("Product Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend(["Product A", "Product B", "Product C"])
plt.show()