# 09_broadcasting.py
#Broadcasting in NumPy basically means:

#NumPy automatically treats a smaller array/value as if it were repeated to match a bigger array, so the operation can happen element-by-element.
import numpy as np


# 1. Scalar with an array

arr = np.array([10, 20, 30, 40])

result = arr + 5

print("Array:", arr)
# Output: Array: [10 20 30 40]

print("Result:", result)
# Output: Result: [15 25 35 45]

#Brodcasting a column
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

values = np.array([
    [1],
    [2]
])

result = arr + values

print(result)