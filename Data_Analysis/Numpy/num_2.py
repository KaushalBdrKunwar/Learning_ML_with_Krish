### Numpy Vectorzied Operation
import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([10,20,30,40,50])

# Element Wise Addition
print("Addition:",arr1+arr2)

# Element Wise Substraction 
print("Substraction:", arr1-arr2)

# Element Wise Multiplication 
print("Multiplication:", arr1*arr2)

# Element Wise Division
print("Division:", arr1/arr2)



arr = np.array([2,3,4,5,6,])

## Square Root
print(np.sqrt(arr))

## Exponential Function
print(np.exp(arr))

##Sine
print(np.sin(arr))

## natural log
print(np.log(arr))

#### Universal Functions

##array slicing and indexing

arr2 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

# print(arr2[0][0])
print(arr2[1:,2:])
print(arr2[0:2,2:]) # Most favouriable
print(arr2[1:,1:3]) # Most favouriable

## Modify array elements
arr2[0][0] = 100
arr2[1:] = 100
print(arr2)