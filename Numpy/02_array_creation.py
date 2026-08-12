# 02_array_creation.py

import numpy as np


# 1. Create an array from a Python list
arr1 = np.array([1, 2, 3, 4, 5])

print("From list:", arr1)
# Output: From list: [1 2 3 4 5]


# 2. Create a 2D array
arr2 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("2D array:\n", arr2)
# Output:
# 2D array:
# [[1 2 3]
#  [4 5 6]]


# 3. Create an array of zeros
zeros = np.zeros(5)

print("Zeros:", zeros)
# Output: Zeros: [0. 0. 0. 0. 0.]


# 4. Create a 2D array of zeros
zeros_2d = np.zeros((2, 3))

print("2D zeros:\n", zeros_2d)
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]]


# 5. Create an array of ones
ones = np.ones(5)

print("Ones:", ones)
# Output: Ones: [1. 1. 1. 1. 1.]


# 6. Create an array with a specific value
full = np.full((2, 3), 7)

print("Full array:\n", full)
# Output:
# [[7 7 7]
#  [7 7 7]]


# 7. Create an array using arange()
arr3 = np.arange(1, 10)

print("Arange:", arr3)
# Output: Arange: [1 2 3 4 5 6 7 8 9]


# 8. arange() with a step
arr4 = np.arange(0, 11, 2)

print("Arange with step:", arr4)
# Output: Arange with step: [ 0  2  4  6  8 10]


# 9. Create evenly spaced values using linspace()
arr5 = np.linspace(0, 10, 5)

print("Linspace:", arr5)
# Output: Linspace: [ 0.   2.5  5.   7.5 10. ]


# 10. Create an identity matrix
identity = np.eye(3)

print("Identity matrix:\n", identity)
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]