# callable() and __call__():
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.


class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Store the multiplier value

# Allows the object to be called like a function; multiplies input with facto
    def __call__(self, value):  
        return value * self.factor
        

# Create an instance of Multiplier with a factor of 3
multiplier = Multiplier(3)

print(multiplier(5))  # Output: 15  __call__(5) → 15 

print(callable(multiplier))  # Output: True



