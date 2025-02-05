import numpy as np

matrix = np.random.randint(0, 101, (5, 5))

r_sums = matrix.sum(axis = 1)

print("The Matrix:")
print(matrix)
print("\n Row-wise sum",r_sums)