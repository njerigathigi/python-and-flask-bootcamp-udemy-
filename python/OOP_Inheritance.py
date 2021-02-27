class Animal(): #base class
    def __init__(self, species, name, color): #called automatically
        self.species = species
        self.name = name
        self.color = color
        print("Animal created.")

    def report(self): #methods are functions written inside a class.allow us to perform operations on the class' attributes.
        print(self.species)

    def eat(self):
        print("{0} is Eating!".format(self.name))

pet1 = Animal("cat", "Nala", "Grey")
pet1.eat()
pet1.report()
print()

class Elephant(Animal): #derived class
    
    def __init__(self, species, name, color):
        Animal.__init__(self,species, name, color) #if you want to inherit the attribues of the parent class.
        print("Elephant:An empathetic creature.")

    def report(self): #overwrite parent's methods by defining methods with the same name.
        print("I am an Elephant!")


    


elephant1 = Elephant("elephant", "Nguvu", "brown")
elephant1.eat()
elephant1.report()
print(elephant1.color)
