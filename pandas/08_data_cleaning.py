# 1. Import Pandas
import pandas as pd
import numpy as np

# 2. Create a DataFrame with missing and duplicate data
# Data cleaning means identifying and fixing incorrect,
# missing, or duplicate data.

data = {
    "Name": ["Alice", "Bob", "Charlie", "Bob", "Eve"],
    "Age": [20, np.nan, 22, np.nan, 24],
    "Marks": [85, 90, np.nan, 90, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# 3. Fill missing values with a fixed value
# fillna() replaces missing values with the value provided.
# Here, missing values in Age are replaced with 0.

df["Age"] = df["Age"].fillna(0)

print("\nAfter filling missing Age values:")
print(df)


# 4. Fill missing values with the mean
# Mean is the average of the available values.
# This is useful for numerical columns when appropriate.

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nAfter filling missing Marks with mean:")
print(df)


# 5. Fill missing values with the median
# Median is the middle value after sorting the data.
# It is often useful when data contains extreme values.

df["Age"] = df["Age"].replace(0, np.nan)
df["Age"] = df["Age"].fillna(df["Age"].median())

print("\nAfter filling missing Age with median:")
print(df)


# 6. Remove rows containing missing values
# dropna() removes rows that contain at least one missing value.
# We use a copy so the original DataFrame remains unchanged.

df_with_missing = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Marks": [85, np.nan, 78]
})

print("\nRows removed if missing values exist:")
print(df_with_missing.dropna())


# 7. Remove duplicate rows
# duplicated() identifies repeated rows.
# drop_duplicates() removes duplicate rows.

print("\nDuplicate rows:")
print(df[df.duplicated()])

df = df.drop_duplicates()

print("\nAfter removing duplicate rows:")
print(df)


# 8. Replace incorrect or unwanted values
# replace() substitutes a specific value with another value.

df["Name"] = df["Name"].replace("Eve", "Eva")

print("\nAfter replacing a value:")
print(df)


# 9. Rename columns
# rename() changes column names.
# The columns argument takes a dictionary of old and new names.

df = df.rename(columns={"Marks": "Score"})

print("\nAfter renaming the column:")
print(df)


# 10. Reset the index
# Resetting creates a fresh numerical index after removing rows.
# drop=True prevents the old index from becoming a column.

df = df.reset_index(drop=True)

print("\nFinal cleaned DataFrame:")
print(df)