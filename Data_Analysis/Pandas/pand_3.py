import numpy as np
import pandas as pd

### Data Manipulation with DataFrame

data ={
    'Name':['Krish','John','Jack'],
    'Age' : [25,26,45],
    'City' : ['Banglore','Kathmandu','NYC']
}

df = pd.DataFrame(data)
print(df)

df['Salary'] = [50000,60000,70000]
print(df)

## Remove a column
df.drop('Salary', axis=1,inplace=True)
print(df)

# Add age to the column
df['Age'] = df['Age']+1
print(df)