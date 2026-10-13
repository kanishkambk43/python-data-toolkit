# 1. Import Pandas
import pandas as pd

# 2. Create a DataFrame
# We will use this data to practice sorting rows.

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [22, 20, 24, 21, 23],
    "Marks": [85, 95, 78, 90, 88]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# 3. Sort by a single column in ascending order
# sort_values() sorts rows based on a column.
# Ascending order means smallest to largest.

print("\nSorted by Age (Ascending):")
print(df.sort_values(by="Age"))


# 4. Sort in descending order
# ascending=False sorts from largest to smallest.

print("\nSorted by Marks (Descending):")
print(df.sort_values(by="Marks", ascending=False))


# 5. Sort by multiple columns
# First, sort by Age.
# If two rows have the same Age, sort those rows by Marks.

print("\nSorted by Age and Marks:")
print(df.sort_values(by=["Age", "Marks"]))


# 6. Sort strings alphabetically
# String values are sorted alphabetically by default.

print("\nSorted by Name:")
print(df.sort_values(by="Name"))


# 7. Sort the DataFrame in place
# inplace=True modifies the original DataFrame.
# Without it, sort_values() returns a new sorted DataFrame.

df.sort_values(by="Marks", ascending=False, inplace=True)

print("\nOriginal DataFrame after sorting:")
print(df)


# 8. Reset the index after sorting
# Sorting does not automatically reset the index.
# reset_index(drop=True) creates a fresh index from 0.

df.reset_index(drop=True, inplace=True)

print("\nDataFrame after resetting index:")
print(df)


# 9. Sort by index
# sort_index() sorts rows using their index labels.

print("\nSorted by Index:")
print(df.sort_index())


# 10. Find the highest and lowest values
# nlargest() returns the rows with the largest values.
# nsmallest() returns the rows with the smallest values.

print("\nTop 2 students by Marks:")
print(df.nlargest(2, "Marks"))

print("\nBottom 2 students by Marks:")
print(df.nsmallest(2, "Marks"))