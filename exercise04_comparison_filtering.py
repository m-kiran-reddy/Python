import numpy as np

num_arr = np.array([12, 45, 67, 23, 89, 34, 56, 90, 15, 72])

num_arr1 = num_arr [ num_arr > 50  ]
print(f"Greater than 50: {num_arr1}")

num_arr2 = num_arr [ num_arr < 50  ]
print(f"Less than 50: {num_arr2}")

num_arr3 = num_arr [ num_arr == 45  ]
print(f"Equal to 45: {num_arr3}")

num_arr4 = num_arr [ num_arr >= 60  ]
print(f"Greater than or equal to 60: {num_arr4}")

num_arr5 = num_arr [ (num_arr >= 30) & (num_arr < 70) ]
print(f"Between 30 and 70: {num_arr5}")

num_arr6 = num_arr%2 == 0
print(f"Even: {num_arr6}")

num_arr7 = num_arr%2 != 0
print(f"Odd: {num_arr7}")

num_arr8 = num_arr [ num_arr > 50  ]
print(f"Count greater than 50: {num_arr8.size}")

num_arr9 = num_arr [ num_arr%2 == 0 ]
print(f"Count even: {num_arr9.size}")

num_arr [ num_arr<30 ] = 0
print(f"Final array: {num_arr}")