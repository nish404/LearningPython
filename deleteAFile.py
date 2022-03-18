import os
import shutil

path = 'folder'

try:
    #os.remove(path)
    #os.rmdir(path)
    shutil.rmtree(path) #CAUTION: this will delete all files and everything contained in it 
except FileNotFoundError:
    print("this file was not found")
except PermissionError:
    print("you do not have the proper permissions to delete this")
except OSError:
    print("you cannot delete that using this function")
else:
    print(path+" was deleted")
