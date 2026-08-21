"""
Q) From the above table that you have created, locate row 0, 4, 7 and 8 using DataFrame.  
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
print(df.iloc[[0, 4, 7, 8]])