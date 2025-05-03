# *****************ABSTRACT CLASS:*****************************

# 🔹 Normal Class vs Abstract Class
# Normal Class:
# - Hum jo roz banate hain, jaise:


class Car:
    def start(self):
        print("Car started")



# - Ismein methods ka code hota hai.
# - Is class ka direct object bana sakte hain.


# 🧩 Abstract Class:
# - Ye ek design ya idea hoti hai.
# - Ismein kuch methods sirf declare hote hain, lekin likhe nahi jaate.
# - Ye abc module se banai jaati hai.
# - Iska direct object nahi bana sakte.

# Python me abstract class ka pata hamesha kuch specific cheezon se chalta hai:
# 1. ABC ka use
# Agar class parenthesis me ABC likha ho, to woh abstract class hoti hai:


from abc import ABC, abstractmethod

# ABC = Abstract Base Class
class Shape(ABC): 
    @abstractmethod
    def area(self): # This is an abstract method
        pass




# ab ye ABC hum isi liye use karty hy k hamri class abstarct ban jaii.

# Q - ye sab hum kaam q kar rahy hy doosry methods sy bhi to ho sakta hy?

# Without Abstract Class (Normal Class)
# Agar hum ek normal class banate hain, jaise:


class Shape:
    def area(self):
        pass



# To, hum ne area ka method bana diya, lekin is class ko koi bhi cheez override (ya change) kar sakti hai, jaise Rectangle ya Circle, aur wo bhool sakti hai area method likhna.
# Aur agar wo area ko na likhe — toh jab hum code run karenge, tab error aayega, jo risky hai.

# With Abstract Class
# Ab agar hum abstract class use karte hain, jaise:


from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass



# Toh ab Python automatically har shape ko force karega ke wo apna area method likhe. Agar koi class area method nahi likhe — to Python error dega aur hum samajh jayenge ke kuch missing hai.

# Why use Abstract Classes?
# - Ensure implementation: Tum chahti ho ke har shape mein area method ho. Abstract class ensure karti hai ke sab child classes is method ko implement karenge.
# - Avoid mistakes: Agar koi class bhool bhi jaye area likhna, to Python hume direct error dega. Matlab koi mistake code mein na rahe.



# 💡 Important Rule:
# Agar ek bhi method abstract ho (@abstractmethod use hua ho), to poori class abstract ban jati hai, aur uska object direct nahi ban sakta.

#  Example (Error):
# a = MyClass()  # ❌ Error: Can't instantiate abstract class

# --------from abc import ABC, abstractmethod-----------
# abstract class banany k liye isy import karna zaroori hy.

# 🔹 abc kya hai?
# abc ka matlab hai Abstract Base Classes.

# Ye Python ka built-in module hai jisko hum import karte hain jab hume abstract class banana hota hai.

# 🔹 abstractmethod kya hai?
# Ye ek decorator hai (@abstractmethod) jo hum method ke upar likhte hain batane ke liye ke ye method sirf design hai, iska code abhi nahi likha gaya — aur har child class ko is method ka code likhna lazmi hai.


#-------------------------------------------------------------------------------------------------------#

#  COMPOSITION:

# Composition ka matlab hai jab ek class ke andar doosri class ka object banaya jata hai aur woh sirf usi ke sath kaam karta hai.
# Agar baahar wali cheez (jaise Car) khatam ho jaye to andar wali cheez (jaise Engine) bhi khatam ho jati hai.
# Yani andar wali cheez apne aap kaam nahi kar sakti, woh sirf baahar wali cheez ke sath hi kaam karti hai.


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

#-------------------------------------------------------------------------------------------------------#
# AGGREGATION:

# Isme ek class doosri class ka object apne andar rakhti hai, lekin dono ka apna alag wajood (existence) hota hai.
# Yani agar parent class ka object delete ho jaye, to child class ka object phir bhi zinda rehta hai.

# Aggregation ki pehchaan:

# Ek object dusre ke andar reference ke tor par hota hai (not created inside).
# Inner object independent hota hai.
# Agar outer class delete ho jaye, inner object phir bhi use ho sakta hai.

class Employee:
    def __init__(self, name):
        self.name = name

    def show_employee(self):
        return f"Employee Name: {self.name}"    

class Department:
    def __init__(self,department_name, employee):
        self.department_name = department_name
        self.employee = employee

    def show_department(self):
        return f"Department Name: {self.department_name}, {self.employee.show_employee()}"


emp_1 = Employee("Mueza Ejaz") 
department_1 = Department("HR", emp_1)

print(department_1.show_department())  # Output: Department Name: HR, Employee Name: Mueza Ejaz
        
#-------------------------------------------------------------------------------------------------------#
# MRO (Method Resolution Order):

# MRO yeh batata hai ki jab aap multiple inheritance use karte ho, to Python kis order me parent classes ko check karega 
# jab koi method ya attribute call kiya jaye.

# MRO ka use kyun hota hai?

# Jab ek class multiple classes se inherit karti hai, aur un sab me same naam ka method ho, to Python ko yeh decide karna hota hai ki pehle kahan se method uthaye.
# MRO ka rule Python me define hai taake ambiguity na ho.

class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

d = D()
d.show()
print(D.__mro__)

# Output:
# B
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

# Yeh output yeh batata hai:

# -Python ne d.show() call kiya:
# -Pehle D me dekha
# -Phir B me (mil gaya, print "B")
# -C aur A me jaana hi nahi pada
# Agar B me show() nahi hota, to C me dekhta, phir A me.
        



