# exception = events detected during execution that interrupts the flow of a program

try:
    numerator = int(input("enter a number to divide by: "))
    denominator = int(input("enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e: # as e is standard practice, but not necessary
    print("you can't divide by zero idiot")
except ValueError as e:
    print("enter only numbers please")
except Exception as e:
    print("something went wrong")
else:
    print(result)
finally:
    print("this will always execute")
