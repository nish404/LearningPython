### MAIN PROGRAM ###

from car import Car

car1 = Car("McLaren","P1",2021,"Black")
car2 = Car("Lotus","Evija",2022,"Anthracite")
car3 = Car("Honda","Rebel",2020,"Slate Grey")

car3.wheels = 2
Car.wheels = 3

print(car1.wheels)
print(car3.wheels)

### CLASS ###


class Car:
    
    wheels = 4 #class variable
    def __init__(self,make,model,year,color):
        self.make = make #instance variable
        self.model = model #instance variable
        self.year = year #instance variable
        self.color = color #instance variable
