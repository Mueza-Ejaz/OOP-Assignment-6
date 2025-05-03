#  Python Object-Oriented Programming (OOP) Assignments 

This document contains Python assignments covering core **Object-Oriented Programming (OOP)** concepts, from basics like `self`, constructors, and access modifiers, to advanced topics like decorators, abstract classes, and custom exceptions.

Each assignment includes a focused example to illustrate the topic clearly.

---

## 📘 Table of Contents

1. Using `self`
2. Using `cls`
3. Public Variables and Methods
4. Class Variables and Class Methods
5. Static Variables and Static Methods
6. Constructors and Destructors
7. Access Modifiers (Public, Protected, Private)
8. `super()` Function
9. Abstract Classes and Methods
10. Instance Methods
11. Class Methods
12. Static Methods
13. Composition
14. Aggregation
15. Method Resolution Order (MRO) & Diamond Inheritance
16. Function Decorators
17. Class Decorators
18. Property Decorators (`@property`, `@setter`, `@deleter`)
19. `callable()` and `__call__()`
20. Creating a Custom Exception
21. Making a Custom Class Iterable

---

## 🧠 Concepts & Assignments Overview

### 1. `self`

Defines instance variables unique to each object.
**Assignment**: `Student` class with name & marks initialized using `self`.

### 2. `cls`

Used in class methods to access or modify class-level data.
**Assignment**: `Counter` class tracks total object creation.

### 3. Public Members

Accessible from anywhere.
**Assignment**: `Car` class with public variable and method.

### 4. Class Variables & Methods

Shared across all instances.
**Assignment**: `Bank` class with changeable `bank_name`.

### 5. Static Methods

Belong to class but don’t use instance or class variables.
**Assignment**: `MathUtils.add(a, b)` static method.

### 6. Constructors & Destructors

Special methods for object lifecycle.
**Assignment**: `Logger` shows messages on creation and deletion.

### 7. Access Modifiers

Controls visibility:

* `Public`: accessible anywhere
* `_Protected`: internal use
* `__Private`: restricted access
  **Assignment**: `Employee` class with all three types.

### 8. `super()` Function

Calls parent class’s constructor or method.
**Assignment**: `Teacher` inherits from `Person`.

### 9. Abstract Classes

Define interface but not implementation.
**Assignment**: Abstract `Shape` with implemented `Rectangle`.

### 10. Instance Methods

Operate on object data using `self`.
**Assignment**: `Dog` class with `bark()` method.

### 11. Class Methods

Use `cls` to modify class-level data.
**Assignment**: `Book` tracks total books.

### 12. Static Methods

General utilities unrelated to object state.
**Assignment**: `TemperatureConverter.celsius_to_fahrenheit(c)`.

### 13. Composition

Class **owns** object of another class. Destroying one destroys both.
**Assignment**: `Car` composed of an `Engine`.

### 14. Aggregation

Class **uses** object of another class, but doesn't own it.
**Assignment**: `Department` uses an independent `Employee`.

### 15. MRO (Method Resolution Order)

Controls method call order in **multiple inheritance**.
**Assignment**: Class `D(B, C)` to observe resolution path.

### 16. Function Decorators

Wrap functions to add behavior.
**Assignment**: `log_function_call` prints before function runs.

### 17. Class Decorators

Wrap/modify entire classes.
**Assignment**: `add_greeting` adds `greet()` to any class.

### 18. Property Decorators

Control access to private variables.
**Assignment**: `Product` with `@property`, `@setter`, `@deleter`.

### 19. `callable()` and `__call__()`

Allows object to behave like function.
**Assignment**: `Multiplier` object returns product when called.

### 20. Custom Exception

Define domain-specific errors.
**Assignment**: `InvalidAgeError` raised if age < 18.

### 21. Iterable Class

Make custom objects loopable using `__iter__()` and `__next__()`.
**Assignment**: `Countdown` class counts down in a for-loop.

---

## 🧹Note

These assignments cover essential topics in Python OOP and help reinforce understanding of how real-world object-oriented systems are designed and structured.
