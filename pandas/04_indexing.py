import pandas as pd  # Import Pandas


# ============================================================
# 1. CREATE A DATAFRAME
# ============================================================

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],  # Student names
    "Age": [20, 21, 19, 22],                       # Student ages
    "Marks": [85, 78, 92, 67]                      # Student marks
}

df = pd.DataFrame(data)  # Create a DataFrame from the dictionary

print("Original DataFrame:")
print(df)  # Display the complete DataFrame


# ============================================================
# 2. ACCESS A COLUMN
# ============================================================

print("\nMarks column:")
print(df["Marks"])  # Select the Marks column


# ============================================================
# 3. ACCESS A SINGLE VALUE
# ============================================================

print("\nFirst student's name:")
print(df.loc[0, "Name"])
# loc[row, column] → access a value using labels


print("\nSecond student's marks:")
print(df.loc[1, "Marks"])
# Row 1 and Marks column


# ============================================================
# 4. loc[] — ACCESS USING LABELS
# ============================================================

print("\nFirst row using loc:")
print(df.loc[0])
# Get row with index label 0


print("\nFirst two rows using loc:")
print(df.loc[0:1])
# loc includes both 0 and 1


print("\nNames and marks:")
print(df.loc[:, ["Name", "Marks"]])
# : means all rows
# Select only Name and Marks columns


# ============================================================
# 5. iloc[] — ACCESS USING POSITION
# ============================================================

print("\nFirst row using iloc:")
print(df.iloc[0])
# iloc[0] → first row based on position


print("\nSecond row using iloc:")
print(df.iloc[1])
# iloc[1] → second row


print("\nFirst two rows:")
print(df.iloc[0:2])
# Get rows at positions 0 and 1
# iloc slicing excludes the ending position


# ============================================================
# 6. ACCESS A SPECIFIC VALUE USING iloc
# ============================================================

print("\nFirst student's name:")
print(df.iloc[0, 0])
# Row position 0, column position 0


print("\nSecond student's marks:")
print(df.iloc[1, 2])
# Row position 1, column position 2


# ============================================================
# 7. SELECT MULTIPLE ROWS AND COLUMNS
# ============================================================

print("\nSelected data:")
print(df.iloc[0:3, 0:2])
# Rows 0 to 2
# Columns 0 to 1


# ============================================================
# 8. BOOLEAN INDEXING
# ============================================================

print("\nStudents with marks >= 80:")
print(df[df["Marks"] >= 80])
# Keep only rows where Marks is greater than or equal to 80


# ============================================================
# 9. BOOLEAN INDEXING WITH MULTIPLE CONDITIONS
# ============================================================

print("\nStudents with marks >= 80 and age < 21:")

result = df[(df["Marks"] >= 80) & (df["Age"] < 21)]
# & means AND
# Both conditions must be true

print(result)


# ============================================================
# 10. USING OR CONDITION
# ============================================================

print("\nStudents with marks >= 90 OR age >= 22:")

result = df[(df["Marks"] >= 90) | (df["Age"] >= 22)]
# | means OR
# At least one condition must be true

print(result)


# ============================================================
# 11. SET A COLUMN AS INDEX
# ============================================================

df_indexed = df.set_index("Name")
# Make the Name column the DataFrame index

print("\nDataFrame with Name as index:")
print(df_indexed)


# ============================================================
# 12. ACCESS DATA AFTER CHANGING INDEX
# ============================================================

print("\nAlice's data:")
print(df_indexed.loc["Alice"])
# loc can now use the student name as the label


print("\nAlice's marks:")
print(df_indexed.loc["Alice", "Marks"])
# Access Alice's Marks using labels


# ============================================================
# 13. RESET INDEX
# ============================================================

df_reset = df_indexed.reset_index()
# Convert the index back into a normal column.

print("\nAfter resetting index:")
print(df_reset)