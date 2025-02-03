import pandas as pd

df= pd.read_csv(r'C:/Users/legion/Desktop/Krish_ML_FullCourse/Data_Analysis/Pandas/data.csv')

## Renaming Columns
df = df.rename(columns={'Date':'Sales Date'})
print(df.head())

## change datatypes
df['Value_new']=df['Value'].fillna(df['Value'].mean()).astype(int)
print(df.head())

df['New Value']=df['Value'].apply(lambda x:x*2)
print(df.head())

