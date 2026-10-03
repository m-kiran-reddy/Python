import numpy as np

num_arr = np.array([45, 12, 78, 34, 90, 23, 67, 10, 56, 89])

print(f"Original array: {num_arr}")

num_sort_arr = np.sort(num_arr)

print(f"Ascending: {num_sort_arr}")

print(f"Descending: {num_sort_arr[::-1]}")

num_arg_sort = np.argsort(num_arr)
print(f"Argsort: {num_arg_sort}")

index_filter_num_arr1 = np.where(num_arr > 50)
print(f"Indexes greater than 50: {index_filter_num_arr1}")

index_filter_num_arr2 = np.where(num_arr < 30)
print(f"Indexes less than 30: {index_filter_num_arr2}")

elements_ftr_num_arr1 = num_arr[np.where(num_arr > 50)]
print(f"Elements greater than 50: {elements_ftr_num_arr1}")


print(f"Count greater than 50: {elements_ftr_num_arr1.size}")

print(f"Sorted array: {num_sort_arr}")

search_sort_arr_55 = np.searchsorted(num_sort_arr, 55)
print(f"Insertion position for 55: {search_sort_arr_55}")

search_sort_arr_100 = np.searchsorted(num_sort_arr, 100)
print(f"Insertion position for 100: {search_sort_arr_100}")