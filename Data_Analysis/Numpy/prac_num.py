### Statistical concepts --Normalization
## to have a mean of 0 and sd of 1
import numpy as np

data = np.array([1,2,3,4,5])

# Calculate the mean and sd 
mean = np.mean(data)
std_dev = np.std(data)

# Normalize the data
normalized_data = (data - mean)/ std_dev
print("Normalized data:", normalized_data)

## Logical Operation

data1 = np.array([1,2,3,4,5,6,7])

print(data1[data1>5])



