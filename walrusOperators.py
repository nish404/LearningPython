# walrus operator :=
# new to Python 3.8 
# assignment expression aka walrus operator
# assigns to variable as part of a larger expression

#foods = list()
#while True:
#    food = input("what food do you like?: ")
#    if food == "quit":
#        break
#    foods.append(food)

foods = list()
while food := input("what food do you like?: ") != "quit":
    foods.append(food)
