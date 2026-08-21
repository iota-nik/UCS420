"""
Q) From the csv file (uploaded in the Q.4) delete row 4, and delete column 3. Display the result.  
"""


import pandas as pd

dfCSV = pd.read_csv('Iris.csv')
dfCSV.drop(4, axis=0, inplace=True)
dfCSV.drop(columns=dfCSV.columns[3], inplace=True)
print(dfCSV)