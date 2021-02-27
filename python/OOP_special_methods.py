class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self): #use return not print. #special method used to represent a class's objects as a string.
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __len__(self):
        return self.pages


feb_book = Book("why didn't they teach me this in school", "carl siegel", 174) 
print(feb_book)
print(len(feb_book)) #len works by calling an object's __len__ method. 

# Special methods are a set of predefined methods used to enrich your classes. Also called Dunder methods.
# Dunder or magic methods in Python are the methods having two prefix and suffix underscores 
# in the method name. Dunder here means “Double Under (Underscores)”.
