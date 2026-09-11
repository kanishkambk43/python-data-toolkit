# 12_sorting.py

import numpy as np


# 1. Sort a 1D array

arr = np.array([50, 20, 40, 10, 30])

print("Original array:", arr)
# Output: Original array: [50 20 40 10 30]

sorted_arr = np.sort(arr)

print("Sorted array:", sorted_arr)
# Output: Sorted array: [10 20 30 40 50]


# 2. Sort in descending order

descending = np.sort(arr)[::-1]

print("Descending:", descending)
# Output: Descending: [50 40 30 20 10]


# 3. Sort a 2D array

arr2 = np.array([
    [30, 10, 20],
    [60, 40, 50]
])

sorted_2d = np.sort(arr2)

print("Sorted 2D array:\n", sorted_2d)

# Output:
# [[10 20 30]
#  [40 50 60]]


# 4. Sort each row

arr3 = np.array([
    [30, 10, 20],
    [90, 50, 70]
])

print("Sorted rows:\n", np.sort(arr3, axis=1))

# Output:
# [[10 20 30]
#  [50 70 90]]


# 5. Sort each column

print("Sorted columns:\n", np.sort(arr3, axis=0))

# Output:
# [[30 10 20]
#  [90 50 70]]


# 6. Find the indexes that would sort the array

arr4 = np.array([50, 20, 40, 10, 30])

indexes = np.argsort(arr4)

print("Sorting indexes:", indexes)
# Output: Sorting indexes: [3 1 4 2 0]


# 7. Use the indexes to get the sorted values

print("Sorted using indexes:", arr4[indexes])
# Output: Sorted using indexes: [10 20 30 40 50]


# 8. Sort strings

names = np.array(["Charlie", "Alice", "Bob"])

print("Sorted names:", np.sort(names))
# Output: Sorted names: ['Alice' 'Bob' 'Charlie']