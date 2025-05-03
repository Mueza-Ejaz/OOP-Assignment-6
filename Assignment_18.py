# Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.



class Product:
    def __init__(self, price):
        self.__price = price
    
    @property
    def price(self):
        return self.__price 

    @price.setter # using setter to set the new price
    def price(self, new_price):
        self.__price = new_price

    @price.deleter
    def price(self):
        del self.__price
        print("Price deleted successfully!")
              


# Example usage:
p = Product(200)
print(p.price)  # Get the price using the getter method

p.price = 300   # Update the price using the setter method
print(p.price)  

del p.price  # Delete the price using the deleter method



