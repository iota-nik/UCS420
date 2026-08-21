import pandas as pd

dfCSV = pd.read_csv('Iris.csv')
dfCSV.drop(4, axis=0, inplace=True)
dfCSV.drop(columns=dfCSV.columns[3], inplace=True)
print(dfCSV)