class Animal:
    def eat(self):
        print("this creature is eating")

class Shark(Animal):
    def eat(self):
        print("the shark is eating other sea creatures")

shark = Shark()
shark.eat()
