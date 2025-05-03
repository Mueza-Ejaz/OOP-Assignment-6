# Creating a Custom Exception:
# Assignment:
# Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.



class InvalidAgeError(Exception):
    """Custom exception for invalid age."""
    pass

def check_age(age):
    try:
        if age < 18:
            raise InvalidAgeError("Age must be 18 or older.")
        else:
            print("Age is valid.")
    except InvalidAgeError as e:
        print(f"InvalidAgeError: {e}")

# Test the function with different ages
check_age(16)   # InvalidAgeError: Age must be 18 or older.    

check_age(20)   # Age is valid.




