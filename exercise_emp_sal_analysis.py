import numpy as np

num_emp_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108])
num_emp_sal = np.array([45000, 65000, 55000, 85000, 75000, 95000, 50000, 120000])

print(f"Employee IDs: {num_emp_ids}")
print(f"Salaries: {num_emp_sal}")

sum_sal = np.sum(num_emp_sal)
print(f"Total salary: {sum_sal}")

avg_emp_sal = np.mean(num_emp_sal)
print(f"Average salary: {avg_emp_sal}")

min_emp_sal = np.min(num_emp_sal)
print(f"Minimum salary: {min_emp_sal}")

max_emp_sal = np.max(num_emp_sal)
print(f"Maximum salary: {max_emp_sal}")

med_emp_sal = np.median(num_emp_sal)
print(f"Median salary: {med_emp_sal}")

std_emp_sal = np.std(num_emp_sal)
print(f"Standard deviation: {std_emp_sal}")

emp_sal_filter = num_emp_sal[np.where(num_emp_sal > 70000)]
print(f"Salaries greater than 70,000: {emp_sal_filter}")

emp_sal_filter1 = num_emp_sal[np.where((num_emp_sal >= 50000) & (num_emp_sal<=90000))]
print(f"Salaries between 50,000 and 90,000 inclusive: {emp_sal_filter1}")

print(f"Count employees earning > 70000: {emp_sal_filter.size}")

sorted_sal = np.sort(num_emp_sal)
print(f"Sorted salaries in ascending: {sorted_sal}")

print(f"Sorted salaries in descending: {sorted_sal[::-1]}")

emp_sal__index_filter = np.where(num_emp_sal > 70000)
print(f"empids who's salaries greater than 70,000: {num_emp_ids[emp_sal__index_filter]}")


print(f"Highest paid employee id: {num_emp_ids[np.argmax(num_emp_sal)]}")


print(f"Highest paid employee salary: {num_emp_sal[np.argmax(num_emp_sal)]}")