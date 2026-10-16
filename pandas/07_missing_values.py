# 1. Import Pandas
import pandas as pd
import numpy as np

# 2. Create a DataFrame with missing values
# NaN represents a missing numerical value.
# None can also represent missing data.

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [20, np.nan, 22, 23, np.nan],
    "Marks": [85, 90, np.nan, 95, 88],
    "City": ["Mysuru", None, "Chennai", "Bengaluru", None]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# 3. Check for missing values
# isna() returns True where a value is missing
# and False where a value is present.

print("\nMissing values:")
print(df.isna())


# 4. Count missing values in each column
# sum() counts the True values returned by isna().

print("\nMissing values in each column:")
print(df.isna().sum())


# 5. Check whether any values are missing
# isna().any() checks if each column has at least
# one missing value.

print("\nMissing values exist in each column?")
print(df.isna().any())


# 6. Get the total number of missing values
# The first sum() counts missing values per column.
# The second sum() adds those counts together.

print("\nTotal missing values:")
print(df.isna().sum().sum())


# 7. Select rows containing missing values
# isna().any(axis=1) checks whether each row
# contains at least one missing value.

print("\nRows with missing values:")
print(df[df.isna().any(axis=1)])


# 8. Select rows without missing values
# notna() returns True for values that are present.
# all(axis=1) selects rows where every column is present.

print("\nRows without missing values:")
print(df[df.notna().all(axis=1)])


# 9. Check missing values in a specific column

print("\nMissing Age values:")
print(df["Age"].isna())


# 10. Detect missing values using notna()
# notna() is the opposite of isna().

print("\nValues present in the Marks column:")
print(df["Marks"].notna())