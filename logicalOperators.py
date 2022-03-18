# logical operators (and,or,not) = used to check if two or more conditional statements is true

temp = int(input("what is the temperature outside?: "))
if not temp >= 32 and temp <= 89:
    print("go outside the temperature is good today")
elif not(temp < 32 or temp > 89):
    print("stay inside the temperature is bad today")
