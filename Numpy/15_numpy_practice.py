import numpy as np  # Import NumPy and give it the short name np


# ============================================================
# 1. CREATE AN ARRAY
# ============================================================

# Create a 2D array containing marks of 5 students
# Each row represents one student
# Each column represents one subject
marks = np.array([
    [78, 85, 92, 67],  # Student 1
    [88, 76, 95, 82],  # Student 2
    [65, 72, 80, 70],  # Student 3
    [90, 91, 89, 94],  # Student 4
    [55, 68, 74, 60]   # Student 5
])

print("Marks:")  # Print a heading
print(marks)     # Display the complete array


# ============================================================
# 2. ARRAY ATTRIBUTES
# ============================================================

print("\nShape:", marks.shape)  # Gives rows and columns
print("Dimensions:", marks.ndim)  # Gives number of dimensions
print("Number of elements:", marks.size)  # Gives total elements
print("Data type:", marks.dtype)  # Gives the data type of elements


# ============================================================
# 3. INDEXING
# ============================================================

print("\nFirst student's marks:", marks[0])
# marks[0] → gets the first row

print("First student's first subject:", marks[0, 0])
# marks[0, 0] → row 0, column 0

print("Third student's second subject:", marks[2, 1])
# marks[2, 1] → row 2, column 1


# ============================================================
# 4. SLICING
# ============================================================

print("\nFirst 3 students:")
print(marks[:3])
# :3 → selects rows 0, 1 and 2

print("\nFirst 2 subjects:")
print(marks[:, :2])
# : → all rows
# :2 → first two columns

print("\nLast 2 students:")
print(marks[-2:])
# -2: → starts from the second-last row


# ============================================================
# 5. RESHAPING
# ============================================================

numbers = np.arange(1, 13)
# Create numbers from 1 to 12

matrix = numbers.reshape(3, 4)
# Convert 12 elements into 3 rows and 4 columns

print("\nReshaped matrix:")
print(matrix)  # Display the reshaped array


# ============================================================
# 6. ITERATION
# ============================================================

print("\nAll marks:")

for row in marks:
    # Get one row at a time

    for mark in row:
        # Get one mark from the current row

        print(mark, end=" ")
        # Print each mark on the same line

    print()
    # Move to the next line after each student


# ============================================================
# 7. ARRAY OPERATIONS
# ============================================================

bonus_marks = marks + 5
# Add 5 to every element in the array

print("\nMarks after adding 5:")
print(bonus_marks)


# ============================================================
# 8. BROADCASTING
# ============================================================

subject_bonus = np.array([2, 3, 4, 5])
# Create different bonus marks for each subject

new_marks = marks + subject_bonus
# NumPy automatically applies the 4 bonuses to every row

print("\nMarks after subject-wise bonus:")
print(new_marks)


# ============================================================
# 9. FILTERING
# ============================================================

high_marks = marks[marks >= 90]
# Select only values that are greater than or equal to 90

print("\nMarks >= 90:")
print(high_marks)


# ============================================================
# 10. np.where()
# ============================================================

result = np.where(marks >= 40, "Pass", "Fail")
# If mark >= 40 → Pass
# Otherwise → Fail

print("\nPass/Fail:")
print(result)


# ============================================================
# 11. SORTING
# ============================================================

sorted_marks = np.sort(marks, axis=1)
# Sort each student's marks from smallest to largest
# axis=1 → work across each row

print("\nMarks sorted for each student:")
print(sorted_marks)


# ============================================================
# 12. AGGREGATION
# ============================================================

print("\nTotal marks:", np.sum(marks))
# Add every element in the array

print("Average marks:", np.mean(marks))
# Calculate the average of all marks

print("Highest mark:", np.max(marks))
# Find the largest mark

print("Lowest mark:", np.min(marks))
# Find the smallest mark


# ============================================================
# 13. STUDENT-WISE AGGREGATION
# ============================================================

student_totals = np.sum(marks, axis=1)
# axis=1 → calculate total across each student's row

student_averages = np.mean(marks, axis=1)
# axis=1 → calculate average for each student

print("\nStudent totals:")
print(student_totals)

print("\nStudent averages:")
print(student_averages)


# ============================================================
# 14. SUBJECT-WISE AGGREGATION
# ============================================================

subject_totals = np.sum(marks, axis=0)
# axis=0 → calculate total down each column

subject_averages = np.mean(marks, axis=0)
# axis=0 → calculate average for each subject

print("\nSubject totals:")
print(subject_totals)

print("\nSubject averages:")
print(subject_averages)


# ============================================================
# 15. RANDOM NUMBERS
# ============================================================

np.random.seed(42)
# Fix the random starting point so results are reproducible

random_marks = np.random.randint(40, 101, size=5)
# Generate 5 random integers from 40 to 100
# 101 is excluded

print("\nRandom marks:")
print(random_marks)


# ============================================================
# 16. PRACTICAL ANALYSIS
# ============================================================

print("\n===== STUDENT ANALYSIS =====")


best_student_index = np.argmax(student_totals)
# np.argmax() returns the index of the largest value

print("Best student index:", best_student_index)
# Display the index of the student with the highest total

print("Best student's marks:", marks[best_student_index])
# Use that index to get the student's marks

print("Best student's total:", student_totals[best_student_index])
# Get that student's total marks


# ============================================================
# 17. OVERALL CLASS ANALYSIS
# ============================================================

class_average = np.mean(marks)
# Calculate the average of all marks

highest_mark = np.max(marks)
# Find the highest mark in the entire array

lowest_mark = np.min(marks)
# Find the lowest mark in the entire array

print("\nClass average:", class_average)
# Display the class average

print("Highest mark in class:", highest_mark)
# Display the highest mark

print("Lowest mark in class:", lowest_mark)
# Display the lowest mark