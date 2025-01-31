# Pandas is used for data analysis and data cleaning.

## Series = 1-D array like object that can hold any data type. It is similar to column in a table.
import pandas as pd
data = [1,2,3,4,5]
index = ['a','b','c','d','e']
series = pd.Series(data,index)
print("Series \n", series)

## Create a Series from dictionary.
data = {'a':1,'b':2,'c':3}
series_dict = pd.Series(data)
print(series_dict)

## DataFrame
