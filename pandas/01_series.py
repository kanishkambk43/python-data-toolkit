
# 1. Import Pandas
import pandas as pd


# 2. Create a Series
# A Series is a one-dimensional labeled data structure.
# By default, Pandas assigns an index starting from 0.

data = pd.Series([10, 20, 30, 40, 50])

print("Series:")
print(data)


# 3. Create a Series with a custom index
# We can provide our own labels instead of using default indexes.

marks = pd.Series(
    [85, 90, 78],
    index=["Alice", "Bob", "Charlie"]
)

print("\nCustom Index Series:")
print(marks)


# 4. Access values using labels
# We can access a value using its custom index label.

print("\nAlice's marks:", marks["Alice"])
print("Bob's marks:", marks["Bob"])


# 5. Access values using position
# iloc[] is used to access values based on their integer position.
# Position starts from 0.

print("\nFirst value:", marks.iloc[0])
print("Second value:", marks.iloc[1])


# 6. Series attributes
# shape: Returns the number of elements as a tuple.
# size: Returns the total number of elements.
# dtype: Returns the data type of the values.

print("\nShape:", marks.shape)
print("Size:", marks.size)
print("Data type:", marks.dtype)


# 7. Basic Series operations
# Pandas provides built-in methods to perform calculations.

numbers = pd.Series([10, 20, 30, 40, 50])

print("\nSum:", numbers.sum())       # Adds all values
print("Mean:", numbers.mean())      # Calculates average
print("Maximum:", numbers.max())    # Finds largest value
print("Minimum:", numbers.min())    # Finds smallest value


# 8. Filtering values in a Series
# We can apply a condition to select specific values.
# numbers > 25 creates a Boolean Series.
# Only values satisfying the condition are displayed.

print("\nValues greater than 25:")
print(numbers[numbers > 25])