def hello(name = "Njeri"):
    print("hello {} from file one".format(name))

print("print statement from file one.py")

if __name__ == "__main__":
    print("file one is being run directly")
else:
    print("file one has been imported")
    
# __name__ is a built-in variable which evaluate to the name of the current module.
# However, if a module is being run directly , then __name__ instead is set to the
# string "__main__". Thus, you can test whether your script is being run directly
# or being imported by something else by testing.
# if __name__ == "__main__":
# If that code is being imported into another module, the various function and
# class definitions will be imported, but the main() code won't get run.
