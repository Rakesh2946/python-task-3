# ---------------------------------------------
# Data Analysis using Pandas
# ---------------------------------------------

import pandas as pd

print("=" * 50)
print("EMPLOYEE DATA ANALYSIS USING PANDAS")
print("=" * 50)

# ---------------------------------------------
# Step 1: Load CSV File
# ---------------------------------------------
try:
    df = pd.read_csv("employees.csv")
    print("\nCSV File Loaded Successfully!\n")
except FileNotFoundError:
    print("Error: employees.csv not found.")
    exit()

# ---------------------------------------------
# Step 2: Inspect Dataset
# ---------------------------------------------
print("First 5 Records")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())

# ---------------------------------------------
# Step 3: Data Cleaning
# ---------------------------------------------

# Fill missing salary with average salary
average_salary = df["Salary"].mean()
df["Salary"] = df["Salary"].fillna(average_salary)

# Fill missing experience with average experience
average_exp = df["Experience"].mean()
df["Experience"] = df["Experience"].fillna(round(average_exp))

print("\nMissing values after cleaning")
print(df.isnull().sum())

# ---------------------------------------------
# Step 4: Filtering
# ---------------------------------------------
print("\nEmployees earning more than 40,000")

high_salary = df[df["Salary"] > 40000]
print(high_salary)

# ---------------------------------------------
# Step 5: Grouping and Aggregation
# ---------------------------------------------
print("\nAverage Salary Department Wise")

department_salary = df.groupby("Department")["Salary"].mean()

print(department_salary)

print("\nMaximum Salary Department Wise")

print(df.groupby("Department")["Salary"].max())

print("\nEmployee Count Department Wise")

print(df.groupby("Department")["ID"].count())

# ---------------------------------------------
# Step 6: Highest Paid Employee
# ---------------------------------------------
highest = df.loc[df["Salary"].idxmax()]

print("\nHighest Paid Employee")
print(highest)

# ---------------------------------------------
# Step 7: Save Cleaned Data
# ---------------------------------------------
df.to_csv("cleaned_employees.csv", index=False)

print("\nCleaned dataset saved as cleaned_employees.csv")

print("\nAnalysis Completed Successfully!")
