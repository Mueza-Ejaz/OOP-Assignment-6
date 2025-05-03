# Make a Custom Class Iterable:
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.



# Custom Iterable Class:
class Countdown:
    count_down = 0
    def __init__(self, start):
        self.start = start


    def __iter__(self): # The __iter__ method is called when the iteration is initialized.
        self.count_down = self.start
        return self


# The __next__ method is called to get the next value in the iteration.
    def __next__(self):
        if self.count_down < 0:
            raise StopIteration
        else:
            current = self.count_down
            self.count_down -= 1
            return current
        
# Example Usage:
countdown = Countdown(6)
for number in countdown:
    print(number)  
    
# Output: 
# 6
# 5
# 4
# 3
# 2
# 1
# 0       




