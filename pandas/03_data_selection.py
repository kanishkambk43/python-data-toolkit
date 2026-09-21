# 1. Import Pandas
import pandas as pd


# 2. Create a DataFrame
# A DataFrame contains rows and columns.
# We will use it to practice selecting data.

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [20, 21, 22, 23],
    "Marks": [85, 90, 78, 95],
    "City": ["Mysuru", "Bengaluru", "Mangaluru", "Mysuru"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# 3. Select a single column
# Using the column name selects one column.
# The result is a Pandas Series.

print("\nName column:")
print(df["Name"])


# 4. Select multiple columns
# Pass a list of column names to select multiple columns.
# The result is a DataFrame.

print("\nName and Marks columns:")
print(df[["Name", "Marks"]])


# 5. Select rows using iloc[]
# iloc[] selects data using integer positions.
# The first row has position 0.

print("\nFirst row:")
print(df.iloc[0])

print("\nFirst two rows:")
print(df.iloc[0:2])


# 6. Select rows and columns using iloc[]
# The format is df.iloc[row_position, column_position].
# : means select all values in that direction.

print("\nFirst two rows and first two columns:")
print(df.iloc[0:2, 0:2])


# 7. Select rows using loc[]
# loc[] selects data using index labels.
# The default index labels are 0, 1, 2, and 3.

print("\nRow with index label 1:")
print(df.loc[1])

print("\nRows with index labels 1 and 2:")
print(df.loc[1:2])


# 8. Select rows and columns using loc[]
# We can specify row labels and column names.

print("\nNames and Marks of rows 0 and 1:")
print(df.loc[0:1, ["Name", "Marks"]])


# 9. Select a column using dot notation
# A column can sometimes be accessed using df.ColumnName.
# This works when the column name is a valid Python attribute.

print("\nAge column using dot notation:")
print(df.Age)


# 10. Select specific cells
# iloc[row, column] accesses one specific value.
# Row and column positions start from 0.

print("\nFirst person's marks:")
print(df.iloc[0, 2])

print("\nSecond person's city:")
print(df.iloc[1, 3])


# 11. Select columns using their data type
# select_dtypes() selects columns based on their data type.
# include="number" selects numeric columns.

print("\nNumeric columns:")
print(df.select_dtypes(include="number"))