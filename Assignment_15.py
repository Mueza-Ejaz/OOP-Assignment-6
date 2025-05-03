# Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# - A with a method show(),
# - B and C that inherit from A and override show(),
# - D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.


# Base class A
class A:
    def show(self):
        print("Class A: show() method called")


# First subclass inheriting from A
class B(A):
    def show(self):
        print("Class B: show() method called")


# Second subclass inheriting from A
class C(A):
    def show(self):
        print("Class C: show() method called")                


# Class D inheriting from both B and C
class D(B, C):
    pass

# Creating object of D and calling show()
d = D()
d.show()

# Let's print MRO to observe method resolution order
print(D.mro()) 

# Output:

# Class B: show() method called
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]







