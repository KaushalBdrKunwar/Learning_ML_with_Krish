import numpy as np

## Create array using numpy
arr1 = np.array([1,2,3,4,5])
print(arr1)
print(type(arr1))
print(arr1.shape)
print(arr1.ndim)
print(arr1.size)
print(arr1.dtype)
print(arr1.itemsize)

#2-D array from 1-D:
arr2 = np.array([1,2,3,4,5])
print(arr2.reshape(1,5)) #reshaping the columns in numpy.

#Also 2-D array can be created from:
arr2 = np.array([[1,2,3,4,5],[2,3,4,5,6]])
print(arr2)
print(arr2.shape)

 # Create Arrays using inbuilt functions:
np.arange(0,10,2).reshape(5,1)

#1. np.ones
print(np.ones((3,4)))

#2. Identity matrix
print(np.eye(3))