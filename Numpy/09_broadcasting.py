# 09_broadcasting.py

import numpy as np


# 1. Scalar with an array

arr = np.array([10, 20, 30, 40])

result = arr + 5

print("Array:", arr)
# Output: Array: [10 20 30 40]

print("Result:", result)
# Output: Result: [15 25 35 45]