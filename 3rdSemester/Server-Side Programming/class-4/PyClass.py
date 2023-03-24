class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def welcome(self):
        print(f'User: {self.name}, {self.age}')


user1 = User(name='Mateus', age=19)

user1.welcome()

# __init__ is the constructor of the python class
# self is the equivalent of this on java

# It is a good practice to always start the constructor and
# the methods of a class with the parameter self
# to be able to work with its attributes
