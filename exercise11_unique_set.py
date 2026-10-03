import numpy as np

num_arr1 = np.array([10, 20, 30, 20, 40, 10, 50, 30])
num_arr2 = np.array([30, 40, 50, 60, 70, 40, 30])

print(f"Array 1: {num_arr1}")
print(f"Array 2: {num_arr2}")

unique_arr1 = np.unique(num_arr1)
unique_arr2 = np.unique(num_arr2)

print(f"Unique array 1: {unique_arr1}")
print(f"Unique array 2: {unique_arr2}")

print(f"Intersection: {np.intersect1d(num_arr1, num_arr2)}")

print(f"Union: {np.union1d(num_arr1, num_arr2)}")

print(f"Array 1 but not array 2: {np.setdiff1d(num_arr1, num_arr2)}")

print(f"Array 2 but not array 1: {np.setdiff1d(num_arr2,num_arr1)}")

print(f"Symmetric difference: {np.setxor1d(num_arr2,num_arr1)}")

print(f"Unique count array 1: {unique_arr1.size}")

print(f"Unique count array 2: {unique_arr2.size}")

