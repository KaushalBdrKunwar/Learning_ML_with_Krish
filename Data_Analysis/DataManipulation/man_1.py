import pandas as pd

df= pd.read_csv(r'C:/Users/legion/Desktop/Krish_ML_FullCourse/Data_Analysis/Pandas/data.csv')

## Fetch the first 5 rows
print(df.head(5))
print(df.tail(5))
print(df.describe())
print(df.dtypes)

# Handling Missing Values
# print(df[df.isnull()])
# print(df.isnull().any(axis=1))
print(df.isnull().sum())
df_filled = df.fillna(0)

##Filling missing values with mean of the column
df['Sales_fillNA']=df['Sales'].fillna(df['Sales'].mean())
print(df)