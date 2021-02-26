class Circle():
    
    pi = 22//7
    
    def __init__(self, radius = 7):
        self.radius = radius

    def area(self):
        return self.pi * (self.radius ** 2)

    def circumference(self):
        return self.pi * (self.radius * 2)

circle1 = Circle(14)
print(circle1.radius)
print(circle1.area())
print(circle1.circumference())
