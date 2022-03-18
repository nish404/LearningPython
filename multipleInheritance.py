# multiple inheritance = when a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("this creature is either a coward or only has self defense")

class Predator:
    def hunt(self):
        print("this creature is searching for his dinner")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

# rabbit.flee()
# hawk.hunt()
fish.flee()
fish.hunt()
