# 1. Import Pandas
import pandas as pd

# 2. Create the first DataFrame
# This DataFrame contains student names and IDs.

students = pd.DataFrame({
    "Student_ID": [101, 102, 103, 104],
    "Name": ["Alice", "Bob", "Charlie", "David"]
})

# 3. Create the second DataFrame
# This DataFrame contains student IDs and their marks.

marks = pd.DataFrame({
    "Student_ID": [101, 102, 103, 105],
    "Marks": [85, 90, 78, 88]
})

print("Students DataFrame:")
print(students)

print("\nMarks DataFrame:")
print(marks)


# 4. Inner merge
# Keeps only rows with matching Student_ID values
# in both DataFrames.

print("\nInner Merge:")
print(pd.merge(students, marks, on="Student_ID", how="inner"))


# 5. Left merge
# Keeps every row from the left DataFrame (students).
# Unmatched rows receive NaN for missing marks.

print("\nLeft Merge:")
print(pd.merge(students, marks, on="Student_ID", how="left"))


# 6. Right merge
# Keeps every row from the right DataFrame (marks).
# Unmatched rows receive NaN for missing student details.

print("\nRight Merge:")
print(pd.merge(students, marks, on="Student_ID", how="right"))


# 7. Outer merge
# Keeps all rows from both DataFrames.
# Unmatched values are filled with NaN.

print("\nOuter Merge:")
print(pd.merge(students, marks, on="Student_ID", how="outer"))


# 8. Merge using different column names
# left_on specifies the key in the left DataFrame.
# right_on specifies the key in the right DataFrame.

student_info = pd.DataFrame({
    "ID": [101, 102, 103],
    "Name": ["Alice", "Bob", "Charlie"]
})

student_scores = pd.DataFrame({
    "Student_ID": [101, 102, 103],
    "Marks": [85, 90, 78]
})

print("\nMerge Using Different Column Names:")
print(pd.merge(
    student_info,
    student_scores,
    left_on="ID",
    right_on="Student_ID",
    how="inner"
))


# 9. Concatenate DataFrames vertically
# concat() combines DataFrames along an axis.
# axis=0 stacks rows; columns are aligned by column name.

class_a = pd.DataFrame({
    "Name": ["Alice", "Bob"],
    "Marks": [85, 90]
})

class_b = pd.DataFrame({
    "Name": ["Charlie", "David"],
    "Marks": [78, 95]
})

print("\nConcatenated DataFrames:")
print(pd.concat([class_a, class_b], ignore_index=True))


# 10. Concatenate DataFrames horizontally
# axis=1 places columns side by side.
# Rows are aligned by their index labels.

print("\nHorizontal Concatenation:")
print(pd.concat([class_a, class_b], axis=1))