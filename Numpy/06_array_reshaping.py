# 06_array_reshaping.py

import numpy as np


# 1. Create a 1D array
arr = np.array([1, 2, 3, 4, 5, 6])

print("Original array:", arr)
# Output: Original array: [1 2 3 4 5 6]


# 2. Check the original shape
print("Original shape:", arr.shape)
# Output: Original shape: (6,)


# 3. Reshape into 2 rows and 3 columns
reshaped = arr.reshape(2, 3)

print("Reshaped array:\n", reshaped)
# Output:
# [[1 2 3]
#  [4 5 6]]


# 4. Check the new shape
print("New shape:", reshaped.shape)
# Output: New shape: (2, 3)


# 5. Reshape into 3 rows and 2 columns
reshaped2 = arr.reshape(3, 2)

print("3 x 2 array:\n", reshaped2)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]]


# 6. Reshape into a single row
row = arr.reshape(1, 6)

print("Single row:\n", row)
# Output:
# [[1 2 3 4 5 6]]


# 7. Reshape into a single column
column = arr.reshape(6, 1)

print("Single column:\n", column)
# Output:
# [[1]
#  [2]
#  [3]
#  [4]
#  [5]
#  [6]]


# 8. Using -1
auto = arr.reshape(2, -1)

print("Using -1:\n", auto)
# Output:
# [[1 2 3]
#  [4 5 6]]


# 9. Flatten the array
flat = reshaped.flatten()

print("Flattened array:", flat)
# Output: Flattened array: [1 2 3 4 5 6]


# 10. Reshape using ravel()
raveled = reshaped.ravel()

print("Raveled array:", raveled)
# Output: Raveled array: [1 2 3 4 5 6]