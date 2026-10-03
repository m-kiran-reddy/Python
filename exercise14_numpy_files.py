import numpy as np

num_arr = np.array(
[[10 , 20,  30],
 [40, 50, 60],
 [70, 80, 90]]
)

print(f"Original array: {num_arr}")

np.save("num_arr.npy", num_arr)

loaded_num_array = np.load("num_arr.npy")

print(f"Loaded NPY array: {loaded_num_array}")

print(f"NPY arrays equal: {np.array_equal(num_arr, loaded_num_array)}")

np.savetxt("num_arr1.csv", num_arr, delimiter=",")

loaded_num_array_csv = np.loadtxt("num_arr1.csv",  delimiter=",")
print(f"Loaded CSV array: {loaded_num_array_csv}")


print(f"CSV arrays equal: {np.array_equal(loaded_num_array_csv, num_arr)}")