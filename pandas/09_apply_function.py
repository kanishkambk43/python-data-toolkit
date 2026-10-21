# 1. Import Pandas
import pandas as pd

# 2. Create a DataFrame

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Marks": [85, 60, 45, 95],
    "Age": [20, 21, 22, 23]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# 3. Apply a function to a column
# apply() executes a function on each value in a Series.
# Here, we convert each name to uppercase.

df["Name"] = df["Name"].apply(lambda name: name.upper())

print("\nNames in Uppercase:")
print(df)


# 4. Apply a calculation to a column
# We add 5 marks to every student's marks.
# The lambda function receives each value and returns value + 5.

df["Marks"] = df["Marks"].apply(lambda marks: marks + 5)

print("\nMarks After Adding 5:")
print(df)


# 5. Create a function to classify marks
# A regular Python function can also be used with apply().
# Here, marks of 50 or more are classified as Pass.

def check_result(marks):
    if marks >= 50:
        return "Pass"
    else:
        return "Fail"

df["Result"] = df["Marks"].apply(check_result)

print("\nStudent Results:")
print(df)


# 6. Apply a function to an entire row
# axis=1 means the function receives one row at a time.
# We use it to create a summary using the Name and Marks columns.

df["Summary"] = df.apply(
    lambda row: f"{row['Name']} scored {row['Marks']}",
    axis=1
)

print("\nStudent Summaries:")
print(df)


# 7. Use map() on a Series
# map() replaces values according to a dictionary.
# Here, we convert result labels into descriptive text.

result_map = {
    "Pass": "Passed Exam",
    "Fail": "Failed Exam"
}

df["Result Description"] = df["Result"].map(result_map)

print("\nResult Descriptions:")
print(df)


# 8. Use apply() with a built-in function
# len() returns the number of characters in a string.

df["Name Length"] = df["Name"].apply(len)

print("\nName Lengths:")
print(df)


# 9. Calculate values using a condition
# apply() can use conditional logic to categorize values.

df["Performance"] = df["Marks"].apply(
    lambda marks: "Excellent" if marks >= 90
    else "Good" if marks >= 70
    else "Needs Improvement"
)

print("\nPerformance Categories:")
print(df)


# 10. Display the final DataFrame

print("\nFinal DataFrame:")
print(df)