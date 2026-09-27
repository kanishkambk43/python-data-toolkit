import numpy as np


# ============================================================
# 1. CREATE AN ARRAY
# ============================================================

marks = np.array([
    [78, 85, 92, 67],
    [88, 76, 95, 82],
    [65, 72, 80, 70],
    [90, 91, 89, 94],
    [55, 68, 74, 60]
])

print("Marks:")
print(marks)


# ============================================================
# 2. ARRAY ATTRIBUTES
# ============================================================

print("\nShape:", marks.shape)
print("Number of dimensions:", marks.ndim)
print("Number of elements:", marks.size)
print("Data type:", marks.dtype)


# ============================================================
# 3. INDEXING
# ============================================================

print("\nFirst student's marks:", marks[0])
print("First student's first subject:", marks[0, 0])
print("Third student's second subject:", marks[2, 1])


# ============================================================
# 4. SLICING
# ============================================================

print("\nFirst 3 students:")
print(marks[:3])

print("\nFirst 2 subjects:")
print(marks[:, :2])

print("\nLast 2 students:")
print(marks[-2:])


# ============================================================
# 5. RESHAPING
# ============================================================

numbers = np.arange(1, 13)

matrix = numbers.reshape(3, 4)

print("\nReshaped matrix:")
print(matrix)


# ============================================================
# 6. ITERATION
# ============================================================

print("\nAll marks:")

for row in marks:
    for mark in row:
        print(mark, end=" ")

print()


# ============================================================
# 7. ARRAY OPERATIONS
# ============================================================

bonus_marks = marks + 5

print("\nMarks after adding 5 bonus marks:")
print(bonus_marks)


# ============================================================
# 8. BROADCASTING
# ============================================================

subject_bonus = np.array([2, 3, 4, 5])

new_marks = marks + subject_bonus

print("\nMarks after subject-wise bonus:")
print(new_marks)


# ============================================================
# 9. FILTERING
# ============================================================

high_marks = marks[marks >= 90]

print("\nMarks >= 90:")
print(high_marks)


# ============================================================
# 10. np.where()
# ============================================================

result = np.where(marks >= 40, "Pass", "Fail")

print("\nPass/Fail:")
print(result)


# ============================================================
# 11. SORTING
# ============================================================

sorted_marks = np.sort(marks, axis=1)

print("\nMarks sorted for each student:")
print(sorted_marks)


# ============================================================
# 12. AGGREGATION
# ============================================================

print("\nTotal marks:", np.sum(marks))
print("Average marks:", np.mean(marks))
print("Highest mark:", np.max(marks))
print("Lowest mark:", np.min(marks))


# ============================================================
# 13. STUDENT-WISE AGGREGATION
# ============================================================

student_totals = np.sum(marks, axis=1)
student_averages = np.mean(marks, axis=1)

print("\nStudent totals:")
print(student_totals)

print("\nStudent averages:")
print(student_averages)


# ============================================================
# 14. SUBJECT-WISE AGGREGATION
# ============================================================

subject_totals = np.sum(marks, axis=0)
subject_averages = np.mean(marks, axis=0)

print("\nSubject totals:")
print(subject_totals)

print("\nSubject averages:")
print(subject_averages)


# ============================================================
# 15. RANDOM NUMBERS
# ============================================================

np.random.seed(42)

random_marks = np.random.randint(40, 101, size=5)

print("\nRandom marks:")
print(random_marks)


# ============================================================
# 16. PRACTICAL ANALYSIS
# ============================================================

print("\n===== STUDENT ANALYSIS =====")

best_student_index = np.argmax(student_totals)

print("Best student index:", best_student_index)
print("Best student's marks:", marks[best_student_index])
print("Best student's total:", student_totals[best_student_index])

print("\nClass average:", np.mean(marks))
print("Highest mark in class:", np.max(marks))
print("Lowest mark in class:", np.min(marks))