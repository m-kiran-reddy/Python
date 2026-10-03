import numpy as np

matrix_A = np.array([
    [1, 2],
    [3, 4]
])

matrix_B = np.array([
    [5, 6],
    [7, 8]
])

print(f"Matrix A: {matrix_A}")
print(f"Matrix B: {matrix_B}")

print(f"Transpose of A: {np.transpose(matrix_A)}")

print(f"Matrix multiplication: {np.matmul(matrix_A, matrix_B)}")

print(f"Determinant of A: {np.linalg.det(matrix_A)}")

inverse_matrix_A = np.linalg.inv(matrix_A)
print(f"Inverse of A: {inverse_matrix_A}")