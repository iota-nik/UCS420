"""
Q) Read a csv file and display its first five rows.  Note-: Download dataset from https://www.kaggle.com/datasets/uciml/iris)  
"""

import pandas as pd

dfCSV = pd.read_csv('Iris.csv')
print(dfCSV.head())