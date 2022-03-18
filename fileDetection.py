import os

path = "C:\\Users\\nish\\Desktop"

if os.path.exists(path):
    print("that location exists")
    if os.path.isfile:
        print("that is a file")
    elif os.path.isdir(path):
        print("that is a directory")
else:
    print("that location does not exist")
