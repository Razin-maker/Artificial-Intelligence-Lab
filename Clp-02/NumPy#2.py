import numpy as np

arr = np.random.rand(100)

arr = (arr - arr.min()) / (arr.max() - arr.min())

print(arr)