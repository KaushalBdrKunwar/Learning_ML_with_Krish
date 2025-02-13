# When to use?
#--> IO bound tasks: Tasks that spend more time waiting for I/O operations(e.g., file operation, network requests).
### When you want to improve throughput of application by performimng multiple task concurently

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_word():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

t1= threading.Thread(target=print_numbers)
t2= threading.Thread(target=print_word)

t = time.time()
## start the thread
t1.start()
t2.start()

## Wait for the threads to complete
t1.join()
t2.join()


# print_numbers()
# print_word()

finished_time = time.time()-t
print(f"finished_time: {finished_time}")