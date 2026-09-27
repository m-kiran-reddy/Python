import numpy as np

num_arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

print(f"Original array: {num_arr}")
print(f"Original shape: {num_arr.shape}")
print(f"Original dimensions: {num_arr.ndim}")

reshape_arr = num_arr.reshape(3, 4)
print(f"3 x 4 array: {reshape_arr}")

print(f"3 x 4 shape: {reshape_arr.shape}")
print(f"3 x 4 dimensions: {reshape_arr.ndim}")

reshape_arr1 = num_arr.reshape(4, 3)
print(f"4 x 3 array: {reshape_arr1}")

org_array = reshape_arr.reshape(reshape_arr.size,)
print(f"Flattened array: {org_array}")
print(f"Flattened elements: {org_array.size}")