# Key Concepts in Python Memory Management
#1. Memory Allocation and Deallocation
#2. Reference Counting
#3. Garbage Collection
#4. The gc Module
#5. Memory Management Best Practices

## Reference Counting: Each object in python maintains a count od references pointing to it. When the reference count drops to zero, the memory occupied by the object is deallocated.

import sys

a = []
print(sys.getrefcount(a)) # 1 for a and 1 for getrefcount function

b=a
print(sys.getrefcount(b))

### Garbage Collection: It handles reference cycles. Ref cycle occurs when objects reference each other,preventing their reference counts from reaching zero.
import gc # garbage collection

gc.enable()
gc.disable()
gc.collect()

## Get garbage collection stats
print(gc.get_stats())

## Get unreachable objects
print(gc.garbage)

#Points: 1. Use local Variables 2. Avoid circular references(eg. a=b and b =c). 3.Use Generators(create 1 obj at a time) .4. Explicitly Delete Objects(use del operator) . 5. Profile Memory Usage(eg. tracemalloc and memory_profiler)
