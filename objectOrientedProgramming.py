# object = an instance of a class 
# creating a class outside of your main method you would create your class and in your main method input from (name of the module) name import (name of the class) Name

### MAIN PROGRAM ###

from car import Car

car1 = Car("McLaren","P1",2021,"Black")
car2 = Car("Lotus","Evija",2022,"Anthracite")

print(car1.make,car1.model,car1.year,car1.color)
print(car2.make,car2.model,car2.year,car2.color)

car1.drive()
car2.stop()

### CLASS ###

class Car:
    
    def __init__(self,make,model,year,color) -> None: # __init__ = constructs objects for in other languages this is known as the constructor 
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    def drive(self): #self refers to the object that is using this method 
        print("this "+self.model+" is drving")
    def stop(self):
        print("this "+self.model+" is stopped ")
