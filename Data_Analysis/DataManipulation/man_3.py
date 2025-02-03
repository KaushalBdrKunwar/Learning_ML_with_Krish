import pandas as pd

df= pd.read_csv(r'C:/Users/legion/Desktop/Krish_ML_FullCourse/Data_Analysis/Pandas/data.csv')

## Data Aggregrating and Grouping
print(df.head())
grouped_mean= df.groupby('Product')['Value'].mean()
print(grouped_mean)

#Grouped_Sum
grouped_sum = df.groupby(['Product','Region'])['Value'].sum()
print(grouped_sum)

## Aggregrate multiple function
grouped_agg = df.groupby('Region')['Value'].agg(['mean','sum','count'])
print(grouped_agg)