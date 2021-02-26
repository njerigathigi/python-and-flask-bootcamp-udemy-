def squares(func):

    def power_two():
        return func() ** 2
        # print("power two")
        # return func() 

    
    return power_two()

@squares
def addition():

    return 2 + 2

print(addition)
    