# 08_array_operations.py

import numpy as np


# Create two arrays
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])


# 1. Addition
print("Addition:", arr1 + arr2)
# Output: Addition: [11 22 33 44 55]


# 2. Subtraction
print("Subtraction:", arr1 - arr2)
# Output: Subtraction: [ 9 18 27 36 45]


# 3. Multiplication
print("Multiplication:", arr1 * arr2)
# Output: Multiplication: [ 10  40  90 160 250]


# 4. Division
print("Division:", arr1 / arr2)
# Output: Division: [10. 10. 10. 10. 10.]


# 5. Power
print("Power:", arr2 ** 2)
# Output: Power: [ 1  4  9 16 25]


# 6. Modulus
print("Modulus:", arr1 % arr2)
# Output: Modulus: [0 0 0 0 0]


# 7. Addition with a single value
print("Add 10:", arr1 + 10)
# Output: Add 10: [20 30 40 50 60]


# 8. Multiplication with a single value
print("Multiply by 2:", arr1 * 2)
# Output: Multiply by 2: [ 20  40  60  80 100]


# 9. Sum
print("Sum:", np.sum(arr1))
# Output: Sum: 150


# 10. Mean
print("Mean:", np.mean(arr1))
# Output: Mean: 30.0


# 11. Minimum
print("Minimum:", np.min(arr1))
# Output: Minimum: 10


# 12. Maximum
print("Maximum:", np.max(arr1))
# Output: Maximum: 50


# 13. Standard deviation
print("Standard deviation:", np.std(arr1))
# Output: Standard deviation: 14.142135623730951