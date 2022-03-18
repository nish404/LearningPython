# while loop = a statement that will execute it's block of code, as long as it's condition remains true

#name = ""

#1 = true
#0 = false

#while len(name) == 0:

#    name = input("enter your name: ")

#print("hello "+name)

name = None

while not name:
    name = input("enter your name: ")

print("hello "+name)
