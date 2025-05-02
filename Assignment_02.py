# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. Use a class variable and a class method with cls to manage and display the count.


class Counter:
    count = 0  # Class variable to keep track of the number of objects created

    def __init__(self):
        Counter.count += 1  # Increment the count whenever a new object is created

    @classmethod
    def display_count(cls):
        print(f"Number of objects created: {cls.count}")


c1 = Counter()
c2 = Counter()
c3 = Counter()
Counter.display_count()  # Output: Number of objects created: 3






