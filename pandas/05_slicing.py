# 1. Import Pandas
import pandas as pd

# 2. Create a DataFrame

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [20, 21, 22, 23, 24],
    "Marks": [85, 90, 78, 95, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 3. Slice rows using iloc[]
# Slicing means selecting a range of rows or columns.
#
# The format is:
# df.iloc[start:stop]
#
# The start position is included.
# The stop position is NOT included.

print("\nFirst three rows:")
print(df.iloc[0:3])

# 4. Slice rows from a particular position

print("\nRows from position 2 onwards:")
print(df.iloc[2:])

# 5. Slice rows up to a particular position

print("\nFirst three rows:")
print(df.iloc[:3])

# 6. Slice both rows and columns
# Format:
# df.iloc[row_start:row_stop, column_start:column_stop]

print("\nFirst three rows and first two columns:")
print(df.iloc[0:3, 0:2])

# 7. Select specific columns using slicing

print("\nAll rows and first three columns:")
print(df.iloc[:, 0:3])

# 8. Select specific rows and specific columns

print("\nRows 1 to 3 and columns 1 to 2:")
print(df.iloc[1:4, 1:3])

# 9. Slice using loc[]
# loc[] works with labels.
# Unlike iloc[], the ending label is INCLUDED.

print("\nRows from index 1 to 3:")
print(df.loc[1:3])

# 10. Slice specific columns using loc[]

print("\nName and Marks columns:")
print(df.loc[:, ["Name", "Marks"]])

# 11. Reverse the rows
# A step of -1 moves through the DataFrame backwards.

print("\nDataFrame in reverse order:")
print(df.iloc[::-1])

# 12. Select every second row
# The third value in slicing is the step.

# [start:stop:step]

print("\nEvery second row:")
print(df.iloc[::2])