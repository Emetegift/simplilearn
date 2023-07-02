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

# class Person:
#     def __init__(self, n, g, a):
#         self.name=n
#         self.gender=g
#         self.age=a
#          ## Where all these are regarded features of the class person
        
#     def talk (self):
#         print("Hi! I am ", self.name)
        
#     def vote (self):
#         if self.age <18 :
#             print("I am not eligible to vote")
#         else:
#             print("I am eligible to vote")

# obj1 = Person("Sam","Male", 22)
# obj2 = Person("Ani", "Male", 45)
# obj1.talk()
# obj1.vote()
# obj2.talk()
# obj2.vote()


"""
What is OOPs?
Object oriented programming language (OOP) is a 
programming paradigm that focuses on objects.
An object has both an attribute aand behaviour.
Attributes, that is, features are the data that data that describes an object, 
while the behaviour(s) are the methods on the attributes
"""

# class Car():
#     def __init__(self, year, speed):
#         self.year=year
#         self.speed=speed
    
#     def getSpeed(self):
#         print("Maximum speed is:", self.speed)
        
#     def setSpeed(self, speed):
#         self.speed=speed
        
# BMW = Car (2018, 155)
# FORD =Car (2016,140)
# BMW.getSpeed()
# BMW.setSpeed(145)
# BMW.getSpeed()

# FORD.getSpeed()
# FORD.setSpeed(120)
# FORD.getSpeed()


# """
# Inheritance: This is the mechanism in which a new class known as a child class 
# or subclass uses the features of the main class also referred to as the parent class.
# """
# # Using class above as the parent class, the classes below will have to inherit from the parent class.

# class Sedan(Car):
#     def accelerate(self):
#         print('137')
        
#     def openTrunk(selt):
#         print("Trunk has been open")
        
# class Suv(Car):
#     def accelerate(self):
#         print('127')
        
# Honda = Sedan(2019, 179)
# Audi = Suv(2020, 188)
# Honda.getSpeed()
# Honda.setSpeed(143)
# Honda.getSpeed()
# Audi.getSpeed()
# Audi.setSpeed(173)
# Audi.getSpeed()

"""

Encapsulation: This is a mechanism that prevent data from direct access.
In this, the child class can only make changes to the data in it, 
but can not alter or chnage data in the parent class. 
"""

"""
Polymorphism: In this mechanism, a single feature can be used in multiple ways
"""

class Car:
    def __init__(self, name):
        self.name =name

class Sedan(Car):
    def accelerate(self):
        print('156')
    
class Suv(Car):
    def accelerate(self):
        print('144')
        
objL = [Sedan("camery"), Suv("Scorpion")]

for obj in objL:
    print(obj.name+ ":", end=" ")
    obj.accelerate() 