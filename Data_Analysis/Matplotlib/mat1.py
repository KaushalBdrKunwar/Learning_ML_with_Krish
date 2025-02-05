# For creation of static, animated and interactive visualizations. It is widely used for data visualization in data science and analytics.
import matplotlib.pyplot as plt

x =[1,2,3,4,5]
y = [1,4,9,16,25]

## Create a line plot
print(plt.plot(x,y))
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title("Basic Line Plot")
print(plt.show())

#Create a customized line plot
plt.plot(x,y,color='red',linestyle='-',marker='o',linewidth=2,markersize=9)
plt.grid(True)
plt.show()
