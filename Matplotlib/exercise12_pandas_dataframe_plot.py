import matplotlib.pyplot as plt
import pandas as pd

data = {
    "month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "sales": [120, 150, 130, 180, 200]
}

df = pd.DataFrame(data)

plt.plot(df["month"], df["sales"])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()