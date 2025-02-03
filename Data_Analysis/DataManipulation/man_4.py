## Merging and joining DataFrames
import pandas as pd

df= pd.read_csv(r'C:/Users/legion/Desktop/Krish_ML_FullCourse/Data_Analysis/Pandas/data.csv')

#1. Create sample DataFrames
df1= pd.DataFrame({'Key': ['A','B','C'], 'Value1': [1,2,3]})
df2= pd.DataFrame({'Key': ['A','B','D'], 'Value2': [4,5,6]})

## Merge DataFrame on the 'Key Columns'
print(pd.merge(df1,df2,on="Key", how="inner"))

##joins == inner,outer etc
