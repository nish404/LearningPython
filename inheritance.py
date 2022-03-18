class Animal: #parent class
    alive = True
    def eat(self):
        print("this animal is eating")
    def sleep(self):
        print("this animal is sleeping")

class Dragon(Animal): #child class; will inherit everything from the parent class
    
    def fly(self):
        print("the dragon is flying")

class Jaguar(Animal):
    
    def sprint(self):
        print("the jaguar is sprinting")

class Lemur(Animal):
    
    def medicate(self):
        print("the lemur is self medicating")

dragon = Dragon()
jaguar = Jaguar()
lemur = Lemur()

#print(dragon.alive)
#print(jaguar.eat())
#print(lemur.sleep())

dragon.fly()
jaguar.sprint()
lemur.medicate()
