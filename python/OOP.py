

    #class object attribute
    # class_attr = 0
    # def __init__(self, instance_attr):
    # instance_attr is an instance attribute defined inside the constructor.
    # class_attr  is a class attribute defined outside the constructor.
    # The instance_attr is only accessible from the scope of an object. 
    # The class attribute (class_attr) is accessible as both a property of the class and as a property of objects, 
    # as it is shared between all of them.
    
    
class Cat():  
    
     #class object attribute
    temperament = "wants to kill you but is cute."
    
    def __init__(self, name, age):
        self.jina = name
        self.age = age

print(Cat.temperament)
print()


cat1 = Cat("Nala", 1)

print(cat1.jina)
print(cat1.age)
print(cat1.temperament)
print(cat1)
print()

cat2 = Cat("Sarabi", 1)
print(cat2.jina)
print(cat2.age)
print(cat2.temperament)
print(cat2)
