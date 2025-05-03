# Class Decorators:
# Assignment:
# Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person


def add_greeting(cls):
    def greet():
        return "Hello from Decorator!"

    cls.greet = greet
    return cls
    
@add_greeting
class Person:
    pass    

# Example usage:
print(Person.greet())  # Output: Hello from Decorator!




