import numpy as np

num_arr1 = np.array([10, 20, 30])
num_arr2 = np.array([40, 50, 60])

print(f"Array 1: {num_arr1}")
print(f"Array 2: {num_arr2}")

num_vstack = np.vstack((num_arr1, num_arr2))
print(f"Vertical stack: {num_vstack}")


num_hstack = np.hstack((num_arr1, num_arr2))
print(f"Horizontal  stack: {num_hstack}")

num_2Darray = np.array([[10, 20, 30],
 [40, 50, 60],
 [70, 80, 90],
 [100, 110, 120]])
print(f"Original 4 x 3 array: {num_2Darray}")

num_2Darray_vsplit = np.vsplit(num_2Darray,2)
print(f"Vertical split: {num_2Darray_vsplit}")

col0, col1, col2 = np.hsplit(num_2Darray,[1,2])
print(f"Column split 1: {col0}")

print(f"Column split 2: {col1}")

print(f"Column split 3: {col2}")