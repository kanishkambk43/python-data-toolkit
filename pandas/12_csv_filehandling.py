# 1. Import Pandas
import pandas as pd

# 2. Create a DataFrame
# We will use this data to practice reading and writing CSV files.

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [20, 21, 22, 23],
    "Marks": [85, 90, 78, 95]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# 3. Write data to a CSV file
# to_csv() saves the DataFrame as a CSV file.
# index=False prevents Pandas from saving row indexes as a column.

df.to_csv("students.csv", index=False)

print("\nData saved to students.csv")


# 4. Read data from a CSV file
# read_csv() loads CSV data into a DataFrame.
# The CSV file must exist at the specified path.

df_read = pd.read_csv("students.csv")

print("\nData read from CSV:")
print(df_read)


# 5. Read only specific columns
# usecols selects only the columns we need.
# This is useful when a dataset contains many columns.

df_selected = pd.read_csv("students.csv", usecols=["Name", "Marks"])

print("\nSelected columns:")
print(df_selected)


# 6. Read a limited number of rows
# nrows specifies how many rows to load from the file.

df_limited = pd.read_csv("students.csv", nrows=2)

print("\nFirst two rows:")
print(df_limited)


# 7. Display basic information about the CSV data
# head() displays the first five rows by default.
# shape returns the number of rows and columns.
# info() displays column names, data types, and non-null counts.

print("\nFirst rows:")
print(df_read.head())

print("\nShape:", df_read.shape)

print("\nDataFrame information:")
df_read.info()


# 8. Handle missing values while reading
# na_values tells Pandas to treat specified values as missing.
# Here, "NA" in the CSV will be interpreted as a missing value.

df_missing = pd.read_csv(
    "students.csv",
    na_values=["NA"]
)

print("\nCSV with missing-value handling:")
print(df_missing)


# 9. Append data to an existing CSV file
# mode="a" appends new rows to the file.
# header=False prevents column names from being written again.

new_student = pd.DataFrame({
    "Name": ["Eva"],
    "Age": [24],
    "Marks": [88]
})

new_student.to_csv(
    "students.csv",
    mode="a",
    header=False,
    index=False
)

print("\nNew student added to CSV")


# 10. Read the updated CSV file
# Read the file again to verify that the new row was added.

df_updated = pd.read_csv("students.csv")

print("\nUpdated CSV data:")
print(df_updated)
