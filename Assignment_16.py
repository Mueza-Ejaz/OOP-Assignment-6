# Function Decorators
# Assignment:
# Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().


def log_function_call(func):
    def wraper():                             # add new function
        print("Function is being called")     # add new work
        return func()
    return wraper


@log_function_call # apply decorator to function we want to print message before it executes
def say_hello():
    print("Hello, World!")


say_hello()

# Output:
# Function is being called
# Hello, World!



