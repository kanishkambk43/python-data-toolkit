import numpy as np


# ============================================================
# 1. RANDOM INTEGER
# ============================================================

np.random.seed(42)

numbers = np.random.randint(1, 10, size=5)

print("Random integers:", numbers)

# Output:
# Random integers: [7 4 8 5 7]



# ============================================================
# 2. RANDOM FLOATS - rand()
# ============================================================

np.random.seed(42)

numbers = np.random.rand(5)

print("Random floats:", numbers)

# Output:
# Random floats: [0.37454012 0.95071431 0.73199394 0.59865848 0.15601864]



# ============================================================
# 3. RANDOM FLOATS - random()
# ============================================================

np.random.seed(42)

numbers = np.random.random(5)

print("Random numbers:", numbers)

# Output:
# Random numbers: [0.37454012 0.95071431 0.73199394 0.59865848 0.15601864]



# ============================================================
# 4. RANDOM NUMBERS FROM NORMAL DISTRIBUTION
# ============================================================

np.random.seed(42)

numbers = np.random.randn(5)

print("Normal distribution:", numbers)

# Output:
# Normal distribution:
# [ 0.49671415 -0.1382643   0.64768854  1.52302986 -0.23415337]



# ============================================================
# 5. RANDOM CHOICE
# ============================================================

np.random.seed(42)

fruits = ["Apple", "Banana", "Mango", "Orange"]

selected = np.random.choice(fruits, size=3)

print("Selected fruits:", selected)



# ============================================================
# 6. RANDOM 2D ARRAY
# ============================================================

np.random.seed(42)

matrix = np.random.randint(1, 100, size=(3, 4))

print("Random matrix:")
print(matrix)



# ============================================================
# 7. SHUFFLE
# ============================================================

np.random.seed(42)

numbers = np.array([1, 2, 3, 4, 5])

np.random.shuffle(numbers)

print("Shuffled array:", numbers)



# ============================================================
# 8. PRACTICAL EXAMPLE - STUDENT MARKS
# ============================================================

np.random.seed(42)

marks = np.random.randint(40, 101, size=10)

print("Student marks:", marks)

print("Average marks:", np.mean(marks))
print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))