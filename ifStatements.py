# if statement = a block of code that will execute if it's condition is true

age = int(input("how old are you?: "))

if age == 100:
    print("you are pretty old")
elif age >= 21:
    print("congrats you're legal")
elif age < 0:
    print("you weren't even thought of yet")
else:
    print("you're not an adult")
