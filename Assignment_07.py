# Access Modifiers: Public, Private, and Protected
# Assignment:

# Create a class Employee with:
# - a public variable name,
# - a protected variable _salary, and
# - a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name  # Public variable
        self._salary = salary  # Protected variable(using single underscore) Accessible but not recommended (protected)
        self.__ssn = ssn  # Private variable(using double underscore) Not accessible outside the class

   

data = Employee("Mueza Ejaz", 40000, "123-45-6789") 

# Accessing the variables
print(data.name)  # Mueza Ejaz (Public variable can be accessed directly).

print(data._salary) # 40000 (Protected variable can be accessed directly, but it's not recommended). 

print(data.__ssn)  # Raises an AttributeError: 'Employee' object has no attribute '__ssn'(private variable cannot be accessed directly).










