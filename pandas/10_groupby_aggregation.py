# 1. Import Pandas
import pandas as pd

# 2. Create a DataFrame
# We will analyze students belonging to different departments.

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank"],
    "Department": ["CSE", "ISE", "CSE", "ISE", "CSE", "ISE"],
    "Marks": [85, 90, 78, 95, 88, 80],
    "Age": [20, 21, 22, 20, 21, 22]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# 3. Group data using groupby()
# groupby() groups rows that share the same value.
# Here, students are grouped by their department.

print("\nStudents grouped by Department:")
print(df.groupby("Department")["Marks"].mean())


# 4. Calculate the sum
# sum() adds the marks of all students in each department.

print("\nTotal Marks by Department:")
print(df.groupby("Department")["Marks"].sum())


# 5. Calculate the average
# mean() calculates the average marks for each department.

print("\nAverage Marks by Department:")
print(df.groupby("Department")["Marks"].mean())


# 6. Find the maximum and minimum
# max() finds the highest marks in each department.
# min() finds the lowest marks in each department.

print("\nMaximum Marks:")
print(df.groupby("Department")["Marks"].max())

print("\nMinimum Marks:")
print(df.groupby("Department")["Marks"].min())


# 7. Count records in each group
# count() counts non-missing values in the selected column.

print("\nNumber of Students by Department:")
print(df.groupby("Department")["Name"].count())


# 8. Use multiple aggregation functions
# agg() applies multiple calculations to a column.
# We calculate count, mean, maximum, and minimum together.

print("\nMarks Statistics by Department:")
print(
    df.groupby("Department")["Marks"].agg(
        ["count", "mean", "max", "min"]
    )
)


# 9. Group by multiple columns
# We can group data using more than one column.
# Here, students are grouped by Department and Age.

print("\nAverage Marks by Department and Age:")
print(df.groupby(["Department", "Age"])["Marks"].mean())


# 10. Aggregate multiple columns
# We can calculate different statistics for different columns.

print("\nDepartment-wise Statistics:")
print(
    df.groupby("Department").agg(
        Average_Marks=("Marks", "mean"),
        Maximum_Marks=("Marks", "max"),
        Average_Age=("Age", "mean")
    )
)


# 11. Reset the index
# By default, groupby() uses the grouping column as the index.
# reset_index() converts it back into a regular column.

result = df.groupby("Department")["Marks"].mean().reset_index()

print("\nResult after resetting index:")
print(result)