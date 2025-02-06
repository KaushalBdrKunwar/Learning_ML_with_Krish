## Sales Data Visualization
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r'Data_Analysis/Matplotlib/sales_data.csv')
print(df.head(5))

## plot total sales by products

total_sales_by_product = df.groupby('Product Category')['Total Revenue'].sum()
print(total_sales_by_product)

#Bar plot
total_sales_by_product.plot(kind='bar',color='teal')
plt.show()
