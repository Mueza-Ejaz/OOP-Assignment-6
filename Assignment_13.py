# Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.


class Engine:
    def start(self):
        print("Engine started!") 

class Car:
    def __init__(self, engine):
        self.engine = engine  # Composition(using object of Engine class)

    def start_engine(self):
        self.engine.start()  # Accessing Engine's method        
    
# Example usage
engine = Engine() 
car = Car(engine)  
car.start_engine()  # Output: Engine started!






