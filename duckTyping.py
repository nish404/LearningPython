# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present 
#               "if it walks like a duck, and talks like a duck, then it must be a duck"

class Duck:
    def walk(self):
        print("the duck is walking")
    def talk(self):
        print("the duck is quacking")

class Chicken:
    def walk(self):
        print("the chicken is walking")
    def talk(self):
        print("the chicken is clucking")

class Person:
    def catch(self,duck):
        duck.walk()
        duck.talk()
        print("you caught the critter")

duck = Duck()
chicken = Chicken()
person = Person()

#person.catch(duck)
person.catch(chicken)
