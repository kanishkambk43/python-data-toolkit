# 1. Import Pandas
import pandas as pd


# 2. Create a DataFrame
# A DataFrame is a two-dimensional data structure.
# It contains rows and columns, similar to an Excel table.

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [20, 21, 22],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)


# 3. Access a single column
# We can access a column using its name.
# The result is a Pandas Series.

print("\nNames:")
print(df["Name"])


# 4. Access multiple columns
# Pass a list of column names to select multiple columns.

print("\nNames and Marks:")
print(df[["Name", "Marks"]])


# 5. Access a row using iloc[]
# iloc[] accesses rows using their integer position.
# Index position starts from 0.

print("\nFirst row:")
print(df.iloc[0])


# 6. Access a row using loc[]
# loc[] accesses rows using their index labels.
# Here, the default index labels are 0, 1, and 2.

print("\nSecond row:")
print(df.loc[1])


# 7. DataFrame attributes
# shape: Returns (number of rows, number of columns).
# size: Returns the total number of elements.
# columns: Returns the column names.
# dtypes: Returns the data type of each column.

print("\nShape:", df.shape)
print("Size:", df.size)
print("Columns:", df.columns)
print("Data types:")
print(df.dtypes)


# 8. Add a new column
# We can create a new column by assigning values to a column name.

df["Passed"] = [True, True, True]

print("\nDataFrame after adding Passed column:")
print(df)


# 9. Delete a column
# drop() removes a row or column.
# axis=1 means we are removing a column.
# inplace=True applies the change directly to the DataFrame.

df.drop("Passed", axis=1, inplace=True)

print("\nDataFrame after deleting Passed column:")
print(df)


# 10. Display basic information
# head() displays the first 5 rows by default.
# tail() displays the last 5 rows by default.
# info() displays DataFrame structure and data types.

print("\nFirst rows:")
print(df.head())

print("\nLast rows:")
print(df.tail())

print("\nDataFrame Information:")
df.info()