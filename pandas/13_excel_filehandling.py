# 1. Import Pandas
import pandas as pd

# To work with Excel files, install openpyxl:
# pip install openpyxl


# 2. Create a DataFrame
# We will use this data to practice reading and writing Excel files.

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [20, 21, 22, 23],
    "Marks": [85, 90, 78, 95]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# 3. Write data to an Excel file
# to_excel() saves a DataFrame as an Excel file.
# index=False prevents row indexes from being saved as a column.

df.to_excel("students.xlsx", index=False)

print("\nData saved to students.xlsx")


# 4. Read data from an Excel file
# read_excel() loads Excel data into a DataFrame.

df_read = pd.read_excel("students.xlsx")

print("\nData read from Excel:")
print(df_read)


# 5. Read a specific sheet
# Excel files can contain multiple worksheets.
# sheet_name specifies which worksheet to read.
# Here, we use the default first sheet, named Sheet1.

df_sheet = pd.read_excel("students.xlsx", sheet_name="Sheet1")

print("\nData from Sheet1:")
print(df_sheet)


# 6. Write data to a sheet with a custom name
# sheet_name sets the worksheet name in the Excel file.

df.to_excel(
    "students_named_sheet.xlsx",
    sheet_name="StudentData",
    index=False
)

print("\nData saved to StudentData worksheet")


# 7. Read specific columns
# usecols selects only the columns we need.
# Here, we load only Name and Marks.

df_selected = pd.read_excel(
    "students.xlsx",
    usecols=["Name", "Marks"]
)

print("\nSelected columns:")
print(df_selected)


# 8. Read a limited number of rows
# nrows specifies how many rows to load from the worksheet.

df_limited = pd.read_excel("students.xlsx", nrows=2)

print("\nFirst two rows:")
print(df_limited)


# 9. Write multiple DataFrames to different sheets
# ExcelWriter allows us to save multiple DataFrames
# into separate worksheets in one Excel file.

top_students = df[df["Marks"] >= 90]

with pd.ExcelWriter("student_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="AllStudents", index=False)
    top_students.to_excel(writer, sheet_name="TopStudents", index=False)

print("\nMultiple worksheets saved to student_report.xlsx")


# 10. Read a specific worksheet from the report
# We can select the worksheet by its name.

df_top = pd.read_excel(
    "student_report.xlsx",
    sheet_name="TopStudents"
)

print("\nTop Students:")
print(df_top)