# Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).


class Logger:
    def __init__(self): # constructor
        print("Logger object created.")

    def __del__(self): # destructor
        print("Logger object destroyed.")    

obj_1 = Logger() 

# output:
# Logger object created.
# Logger object destroyed.       







