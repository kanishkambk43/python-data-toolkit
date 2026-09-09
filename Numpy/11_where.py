# 10_filtering.py

import numpy as np


# 1. Create an array
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
# Output: Array: [10 20 30 40 50]


# 2. Create a condition
condition = arr > 30

print("Condition:", condition)
# Output: Condition: [False False False  True  True]


# 3. Use the condition to filter the array
result = arr[condition]

print("Filtered values:", result)
# Output: Filtered values: [40 50]


# 4. Filtering directly
print("Values greater than 25:", arr[arr > 25])
# Output: Values greater than 25: [30 40 50]


# 5. Values less than 40
print("Values less than 40:", arr[arr < 40])
# Output: Values less than 40: [10 20 30]


# 6. Values greater than or equal to 30
print("Values >= 30:", arr[arr >= 30])
# Output: Values >= 30: [30 40 50]


# 7. Values equal to 30
print("Values equal to 30:", arr[arr == 30])
# Output: Values equal to 30: [30]


# 8. Values not equal to 30
print("Values not equal to 30:", arr[arr != 30])
# Output: Values not equal to 30: [10 20 40 50]


# 9. Multiple conditions using &
result = arr[(arr > 20) & (arr < 50)]

print("Between 20 and 50:", result)
# Output: Between 20 and 50: [30 40]


# 10. Multiple conditions using |
result = arr[(arr < 20) | (arr > 40)]

print("Less than 20 OR greater than 40:", result)
# Output: Less than 20 OR greater than 40: [10 50]