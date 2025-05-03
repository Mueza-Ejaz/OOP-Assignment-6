# DECORATOR FUNCTION:

# Decorator kya hota hai?
# Python mein decorator ek aisa function hota hai jo kisi dusre function ke upar kuch naya behavior add karta hai, 
# bina us function ka code badle.

# Jaise:
# hamry pass ek gift (function) hai. hum us par gift wrap (decorator) kar dete hy — gift andar se wahi rehta hai, 
# lekin upar se acha piyara ho jata hai.

def log_function_call(func):
    def wraper():
        print("Function is being called")
        return func()
    return wraper


@log_function_call
def say_hello():
    print("Hello, World!")


say_hello() 

# Output:
# Function is being called
# Hello, World!

# @log_function_call ka matlab hai: "is function ke upar log_function_call ka kaam lagao."
# Jab say_hello() chalayenge to pehle "Function is being called" print hoga, uske baad "Hello!"
