# OOP (Object-Oriented Programming):

# 🔹 OOP ka matlab:
# Object-Oriented Programming matlab programming real-life cheezon (objects) ki tarah karna.
# 🔸 Jaise:
# mery paas ek mobile hai. Uska color hai, brand hai, aur wo on/off hota hai.
# OOP me hum aisy hi cheezon ko programming me bhi object bana ke samajhtay hain.

# 🔹 OOP ka simple idea:
# Cheez ka design banao (class)
# Us design ka asli piece banao (object)

# 🔹 1. Class kya hoti hai?
# Class ek design / blueprint hoti hai.
# Yeh batata hai ke ek object kaisa dikhega, kya kar sakta hai.

# 🔸 Example:
# Socho ke  me "Car" ka ek design bana rahi ho — usme likha hai:

# - Car ka color
# - Car ka model
# - Car chalegi (function)

# Yeh sirf design hai — abhi koi asli car nahi bani.
# Yeh design ko hum class kehtay hain.


# 🔹 2. Object kya hota hai?
# Object wo asli cheez hoti hai jo class (design) se banti hai.

# 🔸 Example:
# Class ka design tha: Car
# Ab me is design se ek red Toyota banati ho.

# - Is car ka color: Red
# - Model: Toyota 2020
# - Feature: Chalti hai

# Yeh jo asli car bani hai, usko object kehtay hain.

# Syntax of class and object:
# creating class
class Car: # class k name ko hamesha capital letter sy likhna hy
    name = "Landcrozer"

# creating object(instance)
c1 = Car()
print(c1)  # <__main__.Car object at 0x00000203E7629E20>

# check karny k liye k car ka name kiya tha
print(c1.name)  # Landcrozer


# 🔹 Constructor:  __init__() function 
# __init__ means initializing
# Constructor ek special function hota hai jo object banate waqt automatically chal jaata hai.
# Iska kaam hota hai object ko initialize karna — yani object ke andar pehli baar values daalna.

# syntax:(creating class)
# class Student:
#     def __init__(self, fullname):
#         self.name = fullname

# creating  object:
# s1 = Student("mueza")
# print(s1.name)


# aik class banany k baad jab object banaty hy to init function lazmi isk saat execute hota hy .

# method 1:
# default constructor: (agr hum inhy nahi banai gy to by dfault python bana dy ga)
class Learnng:
    def __init__(self):
        print(self) # <__main__.Learnng object at 0x0000029CB1DDAA20>
        print("This is a contructor")

# ye aik constructor ka object hy 
c1 = Learnng() #  This is a contructor   
   
# method 2:
# parameterized constructor
class Student:
    def __init__(self, fullname):
        self.name = fullname
        print("Adding a new student")


s1 = Student("Mueza")   # Adding a new student  
print(s1.name)          # Mueza 

s1 = Student("Ali")  # Adding a new student 
print(s1.name)       # Ali 

# - har object k liye alag sy aik constructor call hota  hy.
# - (s1.name)  ye jitny bhi variables k liye data store kiya jata hy usy hum **attributes** khety
# hy attributes means data / variables.

# method 3:
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding a new student")


s1 = Student("Mueza", 99)   # Adding a new student  
print(s1.name, s1.marks)    # Mueza 99

s1 = Student("Ali", 80)    # Adding a new student 
print(s1.name, s1.marks)   # Ali 80


# class and instance attributes:
class Student:
    collage_name = "Apwa College"
    name = "anonymous" # class attr

    def __init__(self, name, marks):
        self.name = name # obj attr > class attr 
        self.marks = marks
        print("Adding a new student")   

s1 = Student("Mueza", 80)    
print(s1.name)  # Mueza

# Methods:
# Methods are functions that belong to objects.
class Student:
    collage_name = "Apwa College"

    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

    # methods (koi work karwana)
    def welcome(self):
        print("Welcome Student,", self.name)

    def get_marks(self):
        return self.marks      

s1 = Student("Mueza", 80)    
s1.welcome()
print(s1.get_marks)


# STATIC METHODS:
# Static method class ke andar hota hai, lekin:
# -na object (instance) se related hota hai
# -na self ya cls leta hai
# Sirf normal function ki tarah hota hai, jo class ke andar hota hai.

# 📦 Kab use karte hain?
# Jab tumhe aisa function banana ho jo kisi object ki property ko use na kare, sirf kuch kaam kare (e.g., print, calculate).

# syntax
class Student:
    @staticmethod # decorator (isy use kar k self parameter ki zaroorat nahi hogi )
    def college():
        print("hello")

# Example:
class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

# Use without creating object
print(MathOperations.add(5, 3))  # Output: 8

# "Static method kyun use karte hain? Agar self wala function banayein to kya hoga?"

# Answer:
# Agar hamara function kisi bhi object ki properties (like self.name) use nahi karta, to @staticmethod ka use karna best practice hai.
# Agar hum self use karty hy, to Python samajhta hai: "Is function ko object ki koi property chahiye hogi."
         

#TYPES OF OOP:
# 1- Abstraction
# 2- Encapsulation
# 3- Inheritance
# 4- Polymorphism


# 1- Abstraction:
#"Hiding the implementation details of a class and only showing the essential features to the user."
# unneccessary cheezo ko hide kar daina or sirf wo show karwana ya unka access daina jo zaroori hoo jaisy aik car hy ab us me andar ka 
# system engine to dikhaii nahi daita nak driver ko us sy matlab hy wo sirf car chal rahi hy us sy matlab rakhta hy kaisy chal rahi hy 
# us sy iska matlab nahi. 

class Car:
    def __init__(self): 
        # unneccessary data 
        self.acc = False 
        self.brk = False
        self.clutch = False

    def start(self):
        # unneccessary data
        self.clutch = True
        self.acc = True
        print("Car Started...")


# useful data
car1 = Car()
car1.start() # Car Started...                    


# 2- Encapsulation:
# "Wrapping data and functions into a single unit(object)."
# ye aik capsule ki tarha hy abhi tak humny jitna bhi work kiya hy code likha hy woo humny aik class banai phir us me function
# or phir object k anadar attributes to ye sab encapsulation hy.








