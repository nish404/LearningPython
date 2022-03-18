import time

print(time.ctime(0)) # convert a time expressed in seconds since epoch and convert to a readable string
#                      epoch = when your computer thinks time began (reference point)

print(time.time()) # return current seconds since epoch

print(time.ctime(time.time()))

timeObject = time.localtime()
print(timeObject)
localTime = time.strftime("@B %D %Y %H:%M:%S",timeObject)
