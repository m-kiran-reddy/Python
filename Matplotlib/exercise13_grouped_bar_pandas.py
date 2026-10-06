import matplotlib.pyplot as plt
import pandas as pd

data = {
    "department": ["IT", "HR", "Finance", "Sales"],
    "male": [15, 8, 6, 12],
    "female": [10, 7, 4, 8]
}

df = pd.DataFrame(data)
positions = range(len(df))
bar_width = 0.4
plt.bar([p - bar_width / 2 for p in positions], df["male"], width=bar_width)
plt.bar([p + bar_width / 2 for p in positions], df["female"], width=bar_width)
plt.title("Employee Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.xticks(positions, df["department"], rotation=0)
plt.legend(["Male", "Female"])
plt.show()
