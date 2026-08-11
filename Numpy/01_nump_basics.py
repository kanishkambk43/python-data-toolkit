# NumPy Basics
# ----------------------------
# NumPy = Numerical Python
# Used for numerical and mathematical operations
# on arrays and matrices.

import numpy as np


# 1. Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5])

print("Array:", arr)


# 2. Checking the type
print("Type:", type(arr))


# 3. Checking the data type of elements
print("Data type:", arr.dtype)


# 4. Number of dimensions
print("Dimensions:", arr.ndim)


# 5. Shape of the array
print("Shape:", arr.shape)


# 6. Total number of elements
print("Size:", arr.size)


# 7. Basic mathematical operations
print("Addition:", arr + 10)
print("Multiplication:", arr * 2)


# 8. Sum of all elements
print("Sum:", np.sum(arr))


# 9. Minimum and maximum
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))


# 10. Mean (average)
print("Mean:", np.mean(arr))