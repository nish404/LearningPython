# thread = a flow of execution. Like a separate order of instructions 
# however each thread tales a turn running to achieve concurrency 
# GIL = (global interpreter lock),
# allows only one thread to hold the control of the python intepreter at any one time 
# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive) use multiprocessing
# io bound = program/task spends most of it's time waiting for external events (user input, web scraping) use multithreading 

import threading
import time

def eatBreakfast():
    time.sleep(3)
    print("you eat breakfast")

def drinkCoffee():
    time.sleep(4)
    print("you drink coffee")

def study():
    time.sleep(5)
    print("you finish studying")

x = threading.Thread(target=eatBreakfast, args=())
x.start()

y = threading.Thread(target=drinkCoffee, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join()
y.join()
z.join()

#eatBreakfast()
#drinkCoffee()
#study()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter()
