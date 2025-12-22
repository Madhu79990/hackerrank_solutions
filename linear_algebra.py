import numpy as np
n = int(input())
matrix = [list(map(float, input().split())) for _ in range(n)]
determinant = np.linalg.det(matrix)
print(round(determinant, 2))
