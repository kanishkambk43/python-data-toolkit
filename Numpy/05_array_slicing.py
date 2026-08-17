# 05_array_slicing.py

import numpy as np


# 1. One-dimensional array
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
# Output: Array: [10 20 30 40 50]


# 2. Get elements from index 1 to 3
print("Slice:", arr[1:4])
# Output: Slice: [20 30 40]


# 3. Get first three elements
print("First three:", arr[:3])
# Output: First three: [10 20 30]


# 4. Get elements from index 2 to the end
print("From index 2:", arr[2:])
# Output: From index 2: [30 40 50]


# 5. Get the last three elements
print("Last three:", arr[-3:])
# Output: Last three: [30 40 50]


# 6. Get every second element
print("Every second element:", arr[::2])
# Output: Every second element: [10 30 50]


# 7. Reverse the array
print("Reversed:", arr[::-1])
# Output: Reversed: [50 40 30 20 10]


# 8. Two-dimensional array
arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("2D Array:\n", arr2)

# Output:
# [[10 20 30]
#  [40 50 60]
#  [70 80 90]]


# 9. Get first two rows
print("First two rows:\n", arr2[:2])
# Output:
# [[10 20 30]
#  [40 50 60]]


# 10. Get first two columns
print("First two columns:\n", arr2[:, :2])
# Output:
# [[10 20]
#  [40 50]
#  [70 80]]


# 11. Get rows 1 and 2, columns 1 and 2
print("Selected elements:\n", arr2[1:3, 1:3])
# Output:
# [[50 60]
#  [80 90]]