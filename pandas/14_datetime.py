import pandas as pd

# -------------------- 1. Creating a DataFrame with Dates --------------------

data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
    "Joining_Date": ["2024-01-15", "2023-06-20", "2024-03-10", "2022-12-05", "2023-09-25"],
    "Salary": [40000, 35000, 50000, 45000, 38000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# -------------------- 2. Converting to Datetime --------------------

# Convert a column into datetime format.
# This allows Pandas to perform date-related operations.
df["Joining_Date"] = pd.to_datetime(df["Joining_Date"])

print("\nDataFrame after converting to datetime:")
print(df)

print("\nData type of Joining_Date:")
print(df["Joining_Date"].dtype)


# -------------------- 3. Extracting Date Components --------------------

# .dt.year extracts the year from each date.
df["Year"] = df["Joining_Date"].dt.year

# .dt.month extracts the month number.
df["Month"] = df["Joining_Date"].dt.month

# .dt.day extracts the day of the month.
df["Day"] = df["Joining_Date"].dt.day

print("\nExtracted date components:")
print(df)


# -------------------- 4. Extracting Day Name --------------------

# .dt.day_name() returns the weekday name, such as Monday or Tuesday.
df["Day_Name"] = df["Joining_Date"].dt.day_name()

print("\nDay names:")
print(df[["Name", "Joining_Date", "Day_Name"]])


# -------------------- 5. Filtering Data Using Dates --------------------

# Select employees who joined after January 1, 2024.
filtered_df = df[df["Joining_Date"] > "2024-01-01"]

print("\nEmployees who joined after January 1, 2024:")
print(filtered_df[["Name", "Joining_Date"]])


# -------------------- 6. Sorting Dates --------------------

# Sort employees by joining date, from oldest to newest.
sorted_df = df.sort_values(by="Joining_Date")

print("\nSorted by joining date:")
print(sorted_df[["Name", "Joining_Date"]])


# -------------------- 7. Calculating Date Differences --------------------

# Define a reference date.
reference_date = pd.to_datetime("2024-12-31")

# Subtract each joining date from the reference date.
# .dt.days extracts the difference in days.
df["Days_Since_Joining"] = (
    reference_date - df["Joining_Date"]
).dt.days

print("\nDays between joining date and reference date:")
print(df[["Name", "Joining_Date", "Days_Since_Joining"]])


# -------------------- 8. Adding Days to Dates --------------------

# Add 30 days to every joining date.
df["After_30_Days"] = df["Joining_Date"] + pd.Timedelta(days=30)

print("\nJoining dates after 30 days:")
print(df[["Name", "Joining_Date", "After_30_Days"]])


# -------------------- 9. Generating a Date Range --------------------

# Generate 5 consecutive daily dates starting from January 1, 2024.
dates = pd.date_range(start="2024-01-01", periods=5, freq="D")

print("\nGenerated date range:")
print(dates)