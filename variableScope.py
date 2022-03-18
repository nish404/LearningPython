# scope = the region that a variable is recognized
# a variable is only available from inside the region it is created 
# a global and locally scope versions of a variable can be created 

name = "Nish" # global scope (available inside & outside functions)

def displayName():
    name = "Code" # local scope (available only inside this function)
    print(name)

displayName()
print(name)
