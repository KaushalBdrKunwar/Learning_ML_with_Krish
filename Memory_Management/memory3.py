import gc

# Generators For Memory Efficiency

def generate_numbers(n):
    for i in range(n):
        yield i

# Using this generator
for num in generate_numbers(100000):
    print(num)
    if num>10:
        break

### Profiling memory usage with tracemalloc
import tracemalloc

def create_list():
    return [i for i in range(10000)]

def main():
    tracemalloc.start()

    create_list()

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    print("[ Top 10 ]")
    for stat in top_stats[:10]:
        print(stat)

main()