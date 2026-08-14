# 04_array_indexing.py

import numpy as np


# 1. One-dimensional array
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
# Output: Array: [10 20 30 40 50]


# 2. Access the first element
print("First element:", arr[0])
# Output: First element: 10


# 3. Access the third element
print("Third element:", arr[2])
# Output: Third element: 30


# 4. Access the last element
print("Last element:", arr[-1])
# Output: Last element: 50


# 5. Access the second-last element
print("Second-last element:", arr[-2])
# Output: Second-last element: 40


# 6. Two-dimensional array
arr2 = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("2D Array:\n", arr2)

# Output:
# [[10 20 30]
#  [40 50 60]]


# 7. Access an element from a 2D array
print("Element:", arr2[0, 1])
# Output: Element: 20


# 8. Access another element
print("Element:", arr2[1, 2])
# Output: Element: 60


# 9. Access the first row
print("First row:", arr2[0])
# Output: First row: [10 20 30]


# 10. Access the second row
print("Second row:", arr2[1])
# Output: Second row: [40 50 60]