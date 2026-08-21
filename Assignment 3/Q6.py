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