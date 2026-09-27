import numpy as np

num_arr1 = [10, 20, 30, 40, 50]
num_arr2 = [1,  2,  3,  4,  5]

print(f"Addition: {np.add(num_arr1, num_arr2)}")
print(f"Subtraction: {np.subtract(num_arr1, num_arr2)}")
print(f"Multiplication: {np.multiply(num_arr1, num_arr2)}")
print(f"Division: {np.divide(num_arr1, num_arr2)}")
print(f"First array + 10: {np.add(num_arr1, 10)}")
print(f"Second  array * 5: {np.multiply(num_arr2, 5)}")
print(f"Square of first array: {np.multiply(num_arr1 , num_arr1)}")
print(f"Sum of first array: {np.sum(num_arr1)}")
print(f"Mean of first array: {np.mean(num_arr1)}")
print(f"Minimum of first array: {np.min(num_arr1)}")
print(f"Maximum of first array: {np.max(num_arr1)}")


