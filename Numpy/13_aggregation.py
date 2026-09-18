
# 13_aggregation.py

import numpy as np


# 1. Create a 1D array

arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
# Output: Array: [10 20 30 40 50]


# 2. Sum of all elements

print("Sum:", np.sum(arr))
# Output: Sum: 150


# 3. Mean / Average

print("Mean:", np.mean(arr))
# Output: Mean: 30.0


# 4. Minimum value

print("Minimum:", np.min(arr))
# Output: Minimum: 10


# 5. Maximum value

print("Maximum:", np.max(arr))
# Output: Maximum: 50


# 6. Median

print("Median:", np.median(arr))
# Output: Median: 30.0


# 7. Standard deviation

print("Standard deviation:", np.std(arr))
# Output: Standard deviation: 14.142135623730951


# 8. Variance

print("Variance:", np.var(arr))
# Output: Variance: 200.0


# 9. Cumulative sum

print("Cumulative sum:", np.cumsum(arr))
# Output: Cumulative sum: [ 10  30  60 100 150]


# 10. Product of all elements

print("Product:", np.prod(arr))
# Output: Product: 12000000


# ------------------------------------
# 2D ARRAY AGGREGATION
# ------------------------------------

arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("\n2D Array:\n", arr2)

# Output:
# [[10 20 30]
#  [40 50 60]]


# 11. Total sum of 2D array

print("Total sum:", np.sum(arr2))
# Output: Total sum: 210


# 12. Sum along columns (axis=0)

print("Column sums:", np.sum(arr2, axis=0))
# Output: Column sums: [50 70 90]


# 13. Sum along rows (axis=1)

print("Row sums:", np.sum(arr2, axis=1))
# Output: Row sums: [ 60 150]


# 14. Mean along columns

print("Column means:", np.mean(arr2, axis=0))
# Output: Column means: [25. 35. 45.]


# 15. Mean along rows

print("Row means:", np.mean(arr2, axis=1))
# Output: Row means: [20. 50.]


# 16. Minimum along columns

print("Column minimum:", np.min(arr2, axis=0))
# Output: Column minimum: [10 20 30]


# 17. Maximum along rows

print("Row maximum:", np.max(arr2, axis=1))
# Output: Row maximum: [30 60]