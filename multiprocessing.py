# multiprocessing = running task in parallel on different cpu cores, bypasses GIL used for threading
#                   multiprocessing = better for cpu bound tasks (heavy cpu usage)
#                   multithreading = better for io bound tasks (waiting around)

from multiprocessing import Process, cpu_count, process
import time

def counter(num):
    count = 0
    while count < num:
        count += 1

def main():
    a = Process(target=counter, args=(10000000000,))
    a.start()
    b = Process(target=counter, args=(10000000000,))
    b.start()
    a.join()
    b.join()
    print("finished in:",time.perf_counter(), "seconds")

if __name__== '__main__': # may need to run if you are running a windows os
    main()
