# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.

class Car:
    def __init__(self, brand):
        self.brand = brand
    
    # Public method
    def start(self):
        print(f"The {self.brand} car has started.")

c1 = Car("Land cruiser") 
print(c1.brand)       
c1.start() 

# output:
# Land cruiser
# The Land cruiser car has started.






