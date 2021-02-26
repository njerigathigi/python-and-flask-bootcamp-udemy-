def food_ready():
    return "The food is ready"

def name(func):
    print("Njeri")

    #func passed in is a function
    print(func())

name(food_ready)
         