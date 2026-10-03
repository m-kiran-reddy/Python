import numpy as np

rdm_int = np.random.randint(1, 101, 5)
print(f"Random integers: {rdm_int}")

num_arry = np.random.randint(1,51, size = (3,3))
print(f"3 x 3 random array:: {num_arry}")

rdm_floats = np.random.random(5)
print(f"Random floats: {rdm_floats}")

np.random.seed(42)
rdm_int1 = np.random.randint(1, 101, 5)

np.random.seed(42)
rdm_int2 = np.random.randint(1, 101, 5)

print(f"Seeded random integers: {rdm_int1}")
print(f"Seeded random integers again: {rdm_int2}")

print(f"Arrays equals: {np.array_equal(rdm_int1, rdm_int2)}")

print(f"Minimum: {np.min(num_arry)}")
print(f"Maximum: {np.max(num_arry)}")
print(f"Mean: {np.mean(num_arry)}")