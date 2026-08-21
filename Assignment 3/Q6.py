"""
Q) Create a sample dataset (employees.csv) containing information about employees in a company. 
WAP to determine the following using dataset in Q6
    a) Shape (number of rows and columns) of the DataFrame.
    b) Summary of the DataFrame that includes the data types and non-null counts for each column.
    c) Generate descriptive statistics.
    d) Display the first 5 rows and last 3 rows of the dataset.
    e) Calculate the following statistics from the dataset:
        i. The average salary of employees.
        ii. The total bonus paid to all employees.
        iii. The youngest employee's age.
        iv. The highest performance rating.
    f) Sort the DataFrame by the Salary column in descending order.
    g) Add a new column that categorizes employees based on their performance rating:
        i. Excellent for ratings >= 4.5
        ii. Good for ratings >= 4.0 but < 4.5
        iii. Average for ratings < 4.0
    h) Identify missing values in the DataFrame.
    i) Rename the Employee_ID column to ID.
    j) Find all employees who:
        i. Have more than 5 years of experience.
        ii. Belong to the IT department.
    k) Modify the dataset by adding a new column, Tax, which deducts 10% of the Salary.
    l) Save the modified DataFrame (with added columns) to a new CSV file.  
"""


import pandas as pd

data = {
    "Employee_ID" : list(range(101, 106)),
    "Name" : ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department" : ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age" : [29, 34, 41, 28, 38],
    "Salary" : [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience" : [4, 8, 10, 3, 12],
    "Joining_Date" : ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "Gender" : ["Female", "Male", "Male", "Female", "Male"],
    "Bonus" : [5000, 7000, 6000, 4500, 5000],
    "Rating" : [4.5, 4.0, 3.8, 4.7, 3.5]
}
temp = pd.DataFrame(data)
temp.to_csv("employees.csv", index=False)
df = pd.read_csv("employees.csv")

# a)
print(df.shape)

# b)
print(df.info())

# c)
print(df.describe())

# d)
print(df.head(5))
print(df.tail(3))

# e)
print(df["Salary"].mean())
print(df["Bonus"].sum())
print(df["Age"].min())
print(df["Rating"].max())

# f)
df.sort_values(by="Salary", ascending=False)

# g)
def categorizeRating(rating):
    if rating>=4.5:
        return "Excellent"
    elif rating>=4.0:
        return "Good"
    else:
        return "Average"

df["Performance_Category"] = df["Rating"].apply(categorizeRating)

# h)
print(df.isnull().sum())

# i)
df.rename(columns={"Employee_ID" : "ID"}, inplace=True)

# j)
expGt5 = df[df["Years_of_Experience"] > 5]
itDept = df[df["Department"]=="IT"]
print(expGt5[["ID", "Name", "Years_of_Experience"]])
print(itDept[["ID", "Name", "Department"]])

# k)
df["Tax"] = df["Salary"]*0.10
print(df[["Name", "Salary", "Tax"]])

# l)
df.to_csv("Modified_employees.csv", index=False)