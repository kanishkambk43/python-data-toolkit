# 03_array_attributes.py

import numpy as np


# Create a 2D NumPy array
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])


# 1. ndim
print("Dimensions:", arr.ndim)
# Output: Dimensions: 2


# 2. shape
print("Shape:", arr.shape)
# Output: Shape: (2, 3)


# 3. size
print("Size:", arr.size)
# Output: Size: 6


# 4. dtype
print("Data type:", arr.dtype)
# Output: Data type: int64
# Note: It can be int32 on some systems.


# 5. itemsize
print("Item size:", arr.itemsize)
# Output: Item size: 8
# int64 uses 8 bytes per element.


# 6. nbytes
print("Total bytes:", arr.nbytes)
# Output: Total bytes: 48
# 6 elements × 8 bytes = 48 bytes