##DataFrame
#-> It can have multiple rows and columns

#Create a Dataframe from a dictonary of list
import pandas as pd
import numpy as np

data ={
    'Name':['Krish','John','Jack'],
    'Age' : [25,26,45],
    'City' : ['Banglore','Kathmandu','NYC']
}

df = pd.DataFrame(data)
print(df)

nf = np.array(df)
print(nf)

## Create a Data Frame from a List of Dictionaries

data1 = [
    {'Name': 'Krish', 'Age':32, 'City': 'Bangkok'},
    {'Name': 'Krish', 'Age':32, 'City': 'Bangkok'},
    {'Name': 'Krish', 'Age':32, 'City': 'Bangkok'},
    {'Name': 'Krish', 'Age':32, 'City': 'Bangkok'}
]

df1 = pd.DataFrame(data1)
print(df1)

## Read from csv
df2 = pd.read_csv(r'C:/Users/legion/Desktop/Krish_ML_FullCourse/Data_Analysis/Pandas/diabetes.csv')
print(df2.head(5))
print(df2.tail(5))

### Accessing data from Dataframe
print(df['Name']) # When i pick 1 column it becomes a series
 ##OR##
print(df.loc[0])
print(df.iloc[0][0])

## Accessing to the specified element
df.at[2,'Age']
print(df.at[2,'Name'])