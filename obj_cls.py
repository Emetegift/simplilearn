"""
what is an object??
Python is an object oriented progamming language
An object oriented programming language (OOP) is like  every other object that is touchable.
This implies that every instance in python is an object.
"""

"""
what is a class?
A class is a blueprint of similar objects.
"""

class Person:
    def __init__(self, n, g, a):
        self.name=n
        self.gender=g
        self.age=a
         ## Where all these are regarded features of the class person
        
    def talk (self):
        print("Hi! I am ", self.name)
        
    def vote (self):
        if self.age <18 :
            print("I am not eligible to vote")
        else:
            print("I am eligible to vote")

obj1 = Person("Sam","Male", 22)
obj2 = Person("Ani", "Male", 45)
obj1.talk()
obj1.vote()
obj2.talk()
obj2.vote()