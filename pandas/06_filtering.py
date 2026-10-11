# 1. Import Pandas
import pandas as pd

# 2. Create a DataFrame

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Age": [20, 21, 22, 23, 24],
    "Marks": [85, 90, 78, 95, 88],
    "City": ["Mysuru", "Bengaluru", "Mysuru", "Chennai", "Bengaluru"]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# 3. Filter rows using a condition
# We can use a condition to select only the rows
# that satisfy that condition.

print("\nStudents with marks greater than 85:")
print(df[df["Marks"] > 85])

# 4. Filter using equality
# == checks whether a value is equal to something.

print("\nStudents from Mysuru:")
print(df[df["City"] == "Mysuru"])

# 5. Filter using less than

print("\nStudents younger than 23:")
print(df[df["Age"] < 23])

# 6. Filter using greater than or equal to

print("\nStudents with marks >= 90:")
print(df[df["Marks"] >= 90])

# 7. Multiple conditions using AND (&)
# Both conditions must be True.
#
# Each condition should be written inside parentheses.

print("\nStudents from Bengaluru with marks above 85:")
print(df[(df["City"] == "Bengaluru") & (df["Marks"] > 85)])

# 8. Multiple conditions using OR (|)
# At least one condition must be True.

print("\nStudents from Mysuru OR Bengaluru:")
print(df[(df["City"] == "Mysuru") | (df["City"] == "Bengaluru")])

# 9. Filter using NOT (~)
# ~ reverses the condition.
# Here, we select students who are NOT from Mysuru.

print("\nStudents who are NOT from Mysuru:")
print(df[~(df["City"] == "Mysuru")])

# 10. Filter using isin()
# isin() checks whether values belong to a given list.

print("\nStudents from Mysuru or Chennai:")
print(df[df["City"].isin(["Mysuru", "Chennai"])])

# 11. Filter and select specific columns
# We can filter rows and then select only the columns we need.

print("\nNames and marks of students scoring above 85:")
print(df.loc[df["Marks"] > 85, ["Name", "Marks"]])

# 12. Create a Boolean condition separately
# A condition produces True or False for every row.

high_marks = df["Marks"] > 85

print("\nBoolean condition:")
print(high_marks)

print("\nStudents with high marks:")
print(df[high_marks])