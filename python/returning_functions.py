def cat(name = "Nala"):
    print(name)

    def new_cat():
        return "Sarabi"

    def newer_cat():
        return "mufasa"

    if name == "Nala":
        return new_cat
    else:
        return newer_cat

returned_function = cat(name = "Nala")
print(returned_function())
