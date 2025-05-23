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
# e.g: yani kisi ki qualities ko get karna jaisy kuch qualities ya talent hamey apny parents sy milla hai.
# Python me ek class dusri class ke properties aur methods le leti hai, usko inheritance kehte hain.
# "When one class(child/derived) derives the properties and methods of another class(parent/base), it is called inheritance."

# Types of Inheritance:

# 1- Single Inheritance: 
# Ek parent aur ek child class hoti hai.
# Child class, parent ki cheezen use kar sakti hai.  
# Example:

class Parent:
    def talent(self):
        print("I can paint")

class Child(Parent):  # Inheriting from Parent
    def name(self):
        print("My name is Mueza")

c = Child()
c.name()       # My name is Mueza
c.talent()     # I can paint  → inherited from Parent


# 2- Multiple Inheritance: 
# Ek child, do ya zyada parents se inherit karta hai..

# Example:

class Mother:
    def cook(self):
        print("I can cook")

class Father:
    def drive(self):
        print("I can drive")

class Child(Mother, Father):  # Inheriting from both
    def play(self):
        print("I love to play")

c = Child()
c.cook()   # From Mother
c.drive()  # From Father
c.play()   # From Child



# 3- Multi-level Inheritance:
# Parent → Child → Grandchild
# Ek ke baad ek class inherit hoti hai.

# Example:

class GrandParent:
    def house(self):
        print("I have a big house")

class Parent(GrandParent):
    def car(self):
        print("I have a car")

class Child(Parent):
    def bike(self):
        print("I have a bike")

c = Child()

c.house()  # From GrandParent
c.car()    # From Parent
c.bike()   # From Child


# Super() Method:
# super() ka kaam hota hai:Parent class ka method ya constructor ko call karna child class sy.
# -super() ka matlab hota hai: "parent class ko bulao".


# Example without super():
# Agar super() na lagao, to hamey parent class ka code dobara likhna padega, ya kuch cheezein call hi nahi hongi.

#  Example WITHOUT super():
class Car:
    def __init__(self, type):
        self.type = type

class Toyota(Car):
    def __init__(self, name, type):
        self.name = name
        self.type = type  # Repeating parent class logic

car1 = Toyota("Corolla", "Petrol")
print(car1.type)

# Note:
# Yahan hum parent class ka logic dobara likh rahe hain (self.type = type).
# Agar parent class ka logic zyada complex ho, to ye galat practice hai.

# Now WITH super():
class Car:
    def __init__(self, type):
        self.type = type

class Toyota(Car):
    def __init__(self, name, type): # # ✔ Receive type from parent class
        self.name = name
        super().__init__(type)  # Reuse parent class logic


car1 = Toyota("Corolla", "Petrol")
print(car1.type)


# Benefits:
# - Code reusable hai.
# - Parent ka kaam dobara likhne ki zarurat nahi.
# - Agar kal ko Car class me self.type = type.upper() likha gaya ho, to child ko automatically updated version mil jayega.


                              # ****CLASS METHOD*****:

# poori class se related hota hai
# cls (class) ko argument leta hai
# Ye method class ki properties ko access/change kar sakta hai.

# Kab use karte hain?

# -Jab tumhe class-level ka kaam karna ho — jaise:
# -multiple objects banane ka special way
# -class variables ko update karna

# class Student:
#     @classmethod  # decorator
#     def college(cls):
#         pass

# ab class method me class attributes ko change karny k bohat sy methods hoty hy.
class Person:
    name = "Mueza"

    # def changeName(self,name):
    #     Person.name = name # method 1
    #     self.__class__. name =  "Anoo Naatkhuwan" # method 2

     # method 3
    @classmethod
    def changeName(cls, name): # ye class method class k attributes name waly variable me directly changes karta hy
        cls.name = name

p1 = Person()
p1.changeName("Anoo Naatkhuwan")
print(p1.name)      #Anoo Naatkhuwan 
print(Person.name)  # Anoo Naatkhuwan


# Example 2:
class Pizza:
    def __init__(self, size):
        self.size = size

    @classmethod

    def large_pizza(cls):
        return cls("Large")

    @classmethod
    def medium_pizza(cls):
        return cls("Medium") # method 2
    

# Ab object banate hain
pizza1 = Pizza.large_pizza()
pizza2 = Pizza.medium_pizza()

print(pizza1.size)   # Output: Large
print(pizza2.size)   # Output: Medium







