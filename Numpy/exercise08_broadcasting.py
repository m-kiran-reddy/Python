import numpy as np

num_arr1 = np.array([10,20,30,40,50])

num_arr2 = np.array([1,2,3,4,5])

num_2D_arr = np.array([[10, 20, 30],
 [40, 50, 60],
 [70, 80, 90]])

print(f"Original 1-D array: {num_arr1}")
print(f"Add 10: {num_arr1+10}")
print(f"Multiply by 2: {num_arr1*2}")
print(f"Add second array: {num_arr1+num_arr2}")

print(f"Original 2-D array: {num_2D_arr}")

print(f"Add [100 200 300]: {num_2D_arr+ [100,200,300]}")

print(f"Multiply columns by [1 2 3]: {num_2D_arr* [1,2,3]}")

print(f"Subtract 10: {num_2D_arr - 10}")

print(f"Divide by 10: {num_2D_arr / 10}")