# del keyword:
# Used to delete objects properties or objects.
# del s1.name
# del s1

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Mueza")
print(s1.name) # Mueza
del s1.name 
# print(s1.name) # getting some error     

#Private(like) attributes and methods:
# Conceptual Implementations in Python:
# "Private attributes and methods are meant to be used only within the class and are not accessible from outside the class."

class Person:
    __name = "anonymous" # private variable

    def __hello(self):
        print("Hello Person!") # it's a private function

    def welcome(self):
        self.__hello()

p1 = Person() # error 
print(p1.welcome()) # Hello Person!


# Inheritance:
# yani kisi ki qualities ko get karna jaisy kuch qualities ya talent hamey apny parents sy milla hai.
# "When one class(child/derived) derives the properties and methods of another class(parent/base), it is called inheritance."

# class Parent: # ye wo class hy parent jo apni qualities ko share karta hy
# class Child(Parent): # ye wo class hy jo parent ki qualities ko inherit karta hy

# Types of Inheritance:
# 1- Single Inheritance:   
# Example:

class Car:
    color = "grey"
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")

class Toyota(Car): # Inheriting Car class
    def __init__(self, name):
        self.name = name

car1 = Toyota("Corolla")
car2 = Toyota("Yaris")

print(car1.name) # Corolla
print(car2.name) # Yaris
print(car1.color) # grey

# 2- Multiple Inheritance: # Base(Parent) => Derived(Child)-parent => Derived(Child)
# ye sab ki properties ko apy andar inherit kary ga last wali class
# Example

class Car:
    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")

class Toyota(Car): # Inheriting Car class
    def __init__(self, brand):
        self.brand = brand

class Corolla(Toyota): # Inheriting Toyota class
    def __init__(self, type):
        self.type = type 

car1 = Corolla("diesel")
car1.start() # Car Started...


# 3- Multilevel Inheritance:
# is me phely parent classes banaii gy or phir aik saat child class me use kary gy inherit kary gy.

# Example
class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A, B): # Inheriting A and B class
    varC = "Welcome to class C"

var1 = C.varA 
print(var1)   # Welcome to class A

# Super Method:
# "Super() method is used to access methods of the parent class."
# isy hum parent class k methods ko access kary gy child class me.

# Example
class Car:
    def __init__(self, type): # is type ko acces karny k liye super() use kary gy
        self.type = type

    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")

class Toyota(Car): # Inheriting Car class
    def __init__(self, name, type):
        self.name  = name
        super().__init__(type)
        super().start()


car1 = Toyota("prius", "electric")
print(car1.type) # electric


# class Method:




# class Student:
#     @classmethod  # decorator
#     def college(cls):
#         pass




