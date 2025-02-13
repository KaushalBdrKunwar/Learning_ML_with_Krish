# Real world example of Multiprocessing
# Factorial of very large number

import multiprocessing
import sys
import math
import time

# Maximum of number of digits
sys.set_int_max_str_digits(100000)

# Function to calculate the factorial

def compute_factorial(number):
    print(f"Compute the factorial of a {number}")
    result = math.factorial(number)
    print(f"The factorial of  {number} is {result}")
    return result

if __name__=="__main__":
    n = int(input("Enter the number of elements:"))

    numbers = []
    for i in range(n):
        num = int(input(f"Enter the element {i+1}:"))
        numbers.append(num)
    
    start_time = time.time()

    # Create the pool
    with multiprocessing.Pool() as pool:
        results= pool.map(compute_factorial,numbers)
    
    end_time = time.time()

    print(f"Results: {results}")
    print(f"Time Taken: {end_time - start_time} seconds")
    

