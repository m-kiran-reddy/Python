import pandas as pd

employees1 = {
    "emp_id": [101, 102, 103],
    "emp_name": ["Kiran", "Ravi", "Sita"],
    "department": ["IT", "HR", "IT"]
}

employees2 = {
    "emp_id": [104, 105, 106],
    "emp_name": ["Anil", "Raj", "John"],
    "department": ["Finance", "IT", "HR"]
}

emp1_df = pd.DataFrame(employees1)
emp2_df = pd.DataFrame(employees2)

combined_df = pd.concat([emp1_df, emp2_df],ignore_index=True)
print(combined_df)