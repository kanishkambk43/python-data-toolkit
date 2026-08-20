# 07_array_iteration.py

import numpy as np


# 1. Iterating through a 1D array

arr = np.array([10, 20, 30, 40, 50])

for value in arr:
    print(value)

# Output:
# 10
# 20
# 30
# 40
# 50


# 2. Iterating through a 2D array

arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

for row in arr2:
    print(row)

# Output:
# [10 20 30]
# [40 50 60]


# 3. Accessing individual elements using nested loops

for row in arr2:
    for value in row:
        print(value)

# Output:
# 10
# 20
# 30
# 40
# 50
# 60


# 4. Using np.nditer()

for value in np.nditer(arr2):
    print(value)

# Output:
# 10
# 20
# 30
# 40
# 50
# 60


# 5. Iterating with index using enumerate()

for index, value in enumerate(arr):
    print("Index:", index, "Value:", value)

# Output:
# Index: 0 Value: 10
# Index: 1 Value: 20
# Index: 2 Value: 30
# Index: 3 Value: 40
# Index: 4 Value: 50