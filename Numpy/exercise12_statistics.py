import numpy as np

num_arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print(f"Array: {num_arr}")

sum_nums = np.sum(num_arr)
print(f"Sum: {sum_nums}")

mean_nums = np.mean(num_arr)
print(f"Mean: {mean_nums}")

median_nums = np.median(num_arr)
print(f"Median: {median_nums}")

min_num = np.min(num_arr)
print(f"Minimum: {min_num}")

max_num = np.max(num_arr)
print(f"Maximum: {max_num}")

std_dev  = np.std(num_arr)
print(f"Standard Deviation: {std_dev}")

std_var  = np.var(num_arr)
print(f"Variance: {std_var}")

perc_25 = np.percentile(num_arr, 25)
perc_50 = np.percentile(num_arr, 50)
perc_75 = np.percentile(num_arr, 75)

print(f"25th Percentile: {perc_25}")
print(f"50th Percentile: {perc_50}")
print(f"75th Percentile: {perc_75}")

print(f"Range: {np.max(num_arr)-np.min(num_arr)}")