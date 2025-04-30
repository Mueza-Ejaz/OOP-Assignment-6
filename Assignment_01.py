# 1. Using self
# Assignment:

# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks): # Constructor to initialize name and marks
        self.name = name
        self.marks = marks

    # Method to display student details 
    def display(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")    
        

# Creating instances of the Student class
std_1 =  Student("Mueza", 90)
std_2 =  Student("Rapanzual", 85)

# Displaying student details using the display method
std_1.display()   # Student Name: Mueza, Marks: 90  
std_2.display()    # Student Name: Rapanzual, Marks: 85










