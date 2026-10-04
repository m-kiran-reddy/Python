import numpy as np

num_arr = np.array([[10, 20, 30],
 [40, 50, 60],
 [70, 80, 90]])

print(f"Array: {num_arr}")
print(f"Total sum: {np.sum(num_arr)}")
print(f"Row sums: {np.sum(num_arr, axis=1)}")
print(f"Column  sums: {np.sum(num_arr, axis=0)}")

print(f"Row means: {np.mean(num_arr, axis=1)}")
print(f"Column means: {np.mean(num_arr, axis=0)}")


print(f"Row minimums: {np.min(num_arr, axis=1)}")
print(f"Column maximums: {np.max(num_arr, axis=0)}")