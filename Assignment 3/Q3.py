"""
Q3) Navigate the DataFrame and do the following task for the table created in question 1:
    1. Select row from index 3 to 7.
    2. Select row from index 4 to 8, and column 2 to 4.
    3. Select all rows with column index 1 to 3 (include index 3 during selection).  
"""


import pandas as pd

data = {
    "Tid" : list(range(1,11)),
    "Refund" : ["Yes", "No", "No", "Yes", "No", "No", "Yes", "No", "No", "No"],
    "Marital Status" : ["Single", "Married", "Single", "Married", "Divorced", "Married", "Divorced", "Single", "Married", "Single"],
    "Taxable Income" : ["125K", "100K", "70K", "120K", "95K", "60K", "220K", "85K", "75K", "90K"],
    "Cheat" : ["No", "No", "No", "No", "Yes", "No", "No", "Yes", "No", "Yes"]
}
df = pd.DataFrame(data)
# 1)
print(df.iloc[3:8])

# 2)
print(df.iloc[4:9, 2:5])

# 3)
print(df.iloc[:, 1:4])