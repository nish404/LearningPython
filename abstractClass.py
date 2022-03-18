# abstract classes = prevent a user from creating an object of that class 
# comples a user to override any abstract method in a child class
# abstract class = a class that contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementation 

from abc import ABC,abstractmethod # abc is short for abstract

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def go(self):
        print("you drive the car ")
    def stop(self):
        print("this car has stopped")

class Motorcycle(Vehicle):
    def go(self):
        print("you drive the motorcycle")
    def stop(self):
        print("this motorcycle has stopped")

#vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

#vehicle.go()
car.go()
motorcycle.go()

car.stop()
motorcycle.stop()
