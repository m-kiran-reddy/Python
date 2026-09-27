import numpy as np

num_arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(f" First element: {num_arr[0]}")
print(f" Last element: {num_arr[-1]}")
print(f" Third element: {num_arr[2]}")
print(f" Elements from index 1 to index 4: {num_arr[1:5]}")
print(f" First 4 elements: {num_arr[:4]}")
print(f" Last 3 elements: {num_arr[-3:]}")
print(f" Every Second element: {num_arr[0::2]}")
print(f" Array in Reverse Order: {num_arr[::-1]}")
num_arr[3] = 400
print(f" Final Array: {num_arr}")