class Car:
    color = None

class Motorcylce:
    color = None
def changeColor(car,color):
    car.color = color

car1 = Car()
car2 = Car()
car3 = Car()
bike1 = Motorcylce()

changeColor(car1,"anthracite")
changeColor(car2,"matte grey")
changeColor(car3, "white")
changeColor(bike1, "matte black")

print(car1.color)
print(car2.color)
print(car3.color)
print(bike1.color)
