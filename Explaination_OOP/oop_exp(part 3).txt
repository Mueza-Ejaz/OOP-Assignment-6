# More explore Getter and setter decoraator.
# Real life Example:
# Socho hamary paas ek glass hai.
# me dekhti ho usme kitna paani hai → ye getter hai (value lena)
# Glass mein paani daalti ho → ye setter hai (value dena)

# Technical words:
# Definition:
# -Getter → class ke andar wali value read (get) karne ke liye function
# -Setter → class ke andar wali value change (set) karne ke liye function


# without decorator example:
class Student:
    def __init__(self):
        self._name = ""

    def get_name(self):     # getter function
        return self._name

    def set_name(self, value):   # setter function
        self._name = value

# output:
s = Student()
s.set_name("Mueza")         # name set kiya
print(s.get_name())         # name get kiya


# with decorator example:
# Python kehata hai:
# “Tum get_name() na likho, seedha s.name likho!”
# Iske liye hum decorators use karte hain:

class Student:
    def __init__(self):
        self._name = ""

    @property
    def name(self):          # yeh getter ban gaya
        return self._name

    @name.setter
    def name(self, value):   # yeh setter ban gaya
        self._name = value


# Use:
s = Student()
s.name = "Mueza"     # setter chala
print(s.name)        # getter chala

# -----------------------------------------------------------------------------------------------------------------------------

# property decorator: (Method ko attribute ki tarah banata hai)
# Python mein @property ek decorator hai jo ek method ko attribute ki tarah use karne ki sahulat deta hai. Iska matlab yeh hai ke aap kisi method ko call () ke bagair access kar sakti ho, jaise ek normal variable.

# without use @property:
class Student:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

student = Student("Mueza")
print(student.get_name())  # method call

# with use @property:
class Student:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

student = Student("Mueza")
print(student.name)  # no parentheses!

# Is tarah se aap method ko attribute ki tarah use kar sakte hain, jo code ko zyada readable aur samajhne mein asaan banata hai. Yeh encapsulation ka bhi ek hissa hai, jahan aap data ko access karne ke liye methods ka istemal karte hain, lekin unhe attribute ki tarah dikhate hain.
# Iska fayda yeh hai ke agar aapko kabhi method ki implementation change karni ho, toh aapko sirf method ke andar changes karne hain, aur baaki code ko nahi touch karna padega. Yeh encapsulation aur abstraction ka ek acha example hai.



                                 #********************POLYMORPHISM********************#


# Polymorphism: Operator Overloading
# poly means many and morphism means forms.

# Iska matlab hai ke ek hi naam ya operator ka istemal alag alag tarikon se kiya ja sakta hai. Python mein, aap operators ko overload kar sakte hain, yani unki functionality ko change kar sakte hain, taake woh custom objects ke liye bhi kaam karein.

print(1 + 2) # 3
print("Hello" + "World") # HelloWorld # concatenation
print([1, 2] + [3, 4]) # [1, 2, 3, 4] # merge

# this is what ye implicit overloading hai.aik operator hy jis ki alag alag forms hy meanings hy.ye already python ny apny liye 
# kar rakhi hy.ab isii tarha hum aoni classes k liye karingy.

# Real Life Example:
# Agar aap ke paas "Cat", "Dog" aur "Cow" hain, aur sab ke paas speak() method hai — to naam same hoga (speak) lekin awaaz alag hogi:

# operators and dunder functions:

# a + b  # addition             a.__add__(b)

# a - b  # subtraction          a.__sub__(b)

# a * b  # multiplication       a.__mul__(b)

# a / b  # division             a.__truediv__(b)

# a % b  # modulus              a.__mod__(b)

# isk ilawa bhi bohat sary operators hy jin ka apna aik dunder function hota hy. ye hum python k document me ja kar read kar sakty hy.

# Example1:
# __add__() → + operator ka behavior define karta hai

class Book:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

b1 = Book(100)
b2 = Book(200)

print(b1 + b2)  # 300

# Example 2:
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        # New complex number banega dono ka real aur imag part add karke
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

# output:

num1 = ComplexNumber(2, 3)    # 2 + 3i
num2 = ComplexNumber(4, 5)    # 4 + 5i

result = num1 + num2          # __add__() call hoga
print(result)                 # 6 + 8i






