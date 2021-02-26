from file_one import hello

print("print statement from file two.")

hello()

if __name__ == "__main__":
    print("file two is being run directly")
else:
    print("file two has been imported")
