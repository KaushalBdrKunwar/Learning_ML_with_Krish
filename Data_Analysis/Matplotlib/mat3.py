import pandas as pd
import matplotlib.pyplot as plt

#Create a bar plot
categories=['A','B','C','D','E']
values=[5,7,3,8,6]

plt.bar(categories,values,color='purple')
plt.show()

#Histograms
#Sample Data
data = [1,2,3,3,3,4,4,4,5,5,5,5,5]

#create a histogram
plt.hist(data,bins=5)
plt.show()

#create a scatter plot
x = [1,2,3,4]
y = [5,6,7,8]
plt.scatter(x,y)
plt.show()

#create a pie chart
labels = ['A','B','C','D']
sizes=[30,20,40,10]
colors=['gold','yellowgreen','lightcoral','lightskyblue']
explode=(0.2,0,0,0) #Moves out the first slice
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct="%1.1f%%",shadow=True)
plt.show()