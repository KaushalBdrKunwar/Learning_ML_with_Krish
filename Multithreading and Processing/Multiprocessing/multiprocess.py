## Processes that runs in parallel 
### CPU-Bound Tasks
## Parallel execution- Multiple cores of the CPU

import multiprocessing
import time

def square_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"square: {i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube: {i*i*i}")

if __name__=="__main__":
    
    #Create two processes
    p1 = multiprocessing.Process(target=square_numbers)
    p2 = multiprocessing.Process(target=cube_numbers)
    t = time.time()

    # Start the process
    p1.start()
    p2.start()

    #Wait the process
    p1.join()
    p2.join()

    #Final time
    final_time = time.time()-t
    print(f"final_time:{final_time}")

