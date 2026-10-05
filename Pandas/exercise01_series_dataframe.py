import pandas as pd

series_df = pd.Series([10, 20, 30, 40, 50])
print(series_df)
print(f"Type: {type(series_df)}")
print(f"Values: {series_df.values}")
print(f"Index: {series_df.index}")
print(f"Size: {series_df.size}")

employees = {
    "emp_id" : [101,102,103,104,105],
    "emp_name" : ["Kiran","Ravi","Sita","Anil","Raj"],
    "department" : ["IT","HR","IT","Finance","IT"],
    "salary": [75000,65000,85000,55000,95000]
}

df = pd.DataFrame(employees)
print(df)
print(f"Type: {type(df)}")
print(f"Column names: {df.columns}")
print(f"Index: {df.index}")
print(f"Values: {df.values}")
print(f"Shape: {df.shape}")
print(f"Data types: {df.dtypes}")
