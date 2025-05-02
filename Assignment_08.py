#  The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

# parent class
class Person:
    def __init__(self, name):
        self.name = name

class Teacher(Person):  # child class
    def __init__(self, name, subject):
        super().__init__(name)  # Call the constructor of the base class (Person)
        self.subject = subject      


teac_data =  Teacher("Mueza", "Mathematics")       
print(teac_data.name)  # Output: Mueza
print(teac_data.subject)  # Output: Mathematics








