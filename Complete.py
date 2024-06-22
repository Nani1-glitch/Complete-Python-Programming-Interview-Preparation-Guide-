# BODMAS rule
# Brackets -- Orders -- Division and Multiplication -- Addition and Subraction 

a = 10 + 5 *(2**3) - 6/2
print(a)

a = 324523.24512312

print(type(a))

num_int = str(a)

print(num_int)
print(type(num_int)) # Change the data type

my_string = "Nithin Rajulapati"

print(my_string[0:6]) # String Slicing

b = "Let us start learning Python programming from today!"

print(b[0:21]) # String Sllicing 

# Relational Operators

c = 5
d = 4

print(c < d)
 
print(0.1+0.1+0.1 == 0.3) # This was actually FALSE -------> Try it

# AND / OR operators 

a = 5>3
b = 4<2

print(a and b)
print(a or b)

c = 4>3

print(not c) # not operator always prints reciprocal of the actual output. For instance if the output is True and you use not in this case it wil print it as False.

print ("Nithin" == "Nithin")

# Conditional Statements 

a = 100 > 233
if a:                # a holds the position where we have to give the condition 
    print(a)
else:
    print("WTF")

age = int(input("Enter the age to calculate: "))

if age > 18:
    print("You are adult!")
else:
    print("Pilla bacha nayala...")

if age < 18:
    print("You are an pilla bacha")
elif age >= 18  and age < 60:
    print("You are an adult")
else:
    print("emundi le poduko inka (senior ciitzen)")

s = int(input("Enter the number: "))
if s%2 == 0:
    print(str(s) + " is a Even number")
else:
    print(str(s) + " is a Odd number")

x = 10
if x > 0:
    print("x is positive")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")

score = int(input("Enter the score you got: "))
if score >= 90:
    print("You got A grade")
elif score >= 80:
    print("You got B grade")
    if score >= 85:
        print("You are at B and all the best for the next time..")
elif score >= 70:
    print("You are at grade C")
else:
    print("Fail ayinav ra batta.")

# LOOPS

# While Loop
start = 1
while start <= 20:
    print(start)
    start += 1

count = 10 
while count > 0:
    print(count)
    count -= 1

product = 1
ans = int(input(" Enter the number for calculating the factorial: "))
count = 1 
while (count <= ans):
    product *= count 
    count += 1
print(product)

# For Loop
for num in range (1,10):
    print(num)

# Example 1
for each in "hello":
    print(each)
# Example 2
string = " "
for num in range(1,10):
    string = string + str(num) + " "
print(string)


# STRING METHODS 

string = "Hello! How aRe yoU tODay?" 
print(len(string)) # Show's the no.of characters in the string 
print(string.lower()) # Converts all the characters in the string into the small case letters
print(string.strip())# Removes all the empty/extra spaces 
print(string.replace("Hello", "Heyyyy")) # Replaces the particular word 


# NESTED LOOPS 

n = int(input("Enter the no.of line to print: "))
for i in range(1,n+1):
    for j in range(i): # Loop inside the loop 
        print("*", end = " ")
    print()

# Example problem
count = 1 
string = " "
for i in range(5):
    for j in range(5):
        string += str(count) + " "
        count += 1
    print(string)
    string = " "


# LOOP CONTROL STATEMENTS

# break | continue | pass
for num in range(1,10):
    if num == 7:
        break
    print(num)

for num in range(1,20):
    if num % 2 == 0:
        continue
    print(num)

num = 100
for num in range(1,10):
    pass


# LISTS

num = [1,2,3,4,5]
num[1] = "nithin"
num1 = ["Nithin", "Hello", "How", "are", "You"]
num1.append("Hey") # Adds the string_value at the end of the above string 
print(num1)

# TUPLES

a = (1,2,34,3,12,13, "nithin")
# a[1] = "Hello" # Throws an error (Tuple object does not support item assignment) beacause tuples are immutable
# print(a)
print(type(a))


# DICTIONARIES 

student = {
    "name": "Nithin Rajulapati",
    "age": 23,
    "major": "AI",
    "gpa": 3.55
}
print(student["age"])


# SETS
# Cannot repeat the elements multiple times | Sets do not allow duplicates

set = {1,23,2,31,12,11,1,1,1,1,1,123,2,212,12,1232,3121,21232323242,11,12,12,1}
print(set) # Removes all the duplicate values

myset = {"apple", "banana", "orange"}
print(myset) # Prints all the elements in the set randomly everytime it runs. 

myset.remove("apple") # Removes the certain element from the set.
print(myset)

# Example problem
set1 = {1,2,3,4,5,6,7,8}
set2 = {6,7,8,9,10,11,12}

union_set = set1.union(set2)
print(union_set)

intersection_set = set1.intersection(set2)
print(intersection_set)

difference_set = set1.difference(set2)
print(difference_set)

symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)


# FUNCTIONS

def add(a,b):
    return(a+b)
a = add(2,3)
print(a)

def greet(name):
    print(f"Hello, {name}")
greet("Nithin")

# Scope of Variables
global_variable = "I'm Global"
def function_with_local_variable():
    local_variable = "I'm Local"
    print(global_variable)
    print(local_variable)
function_with_local_variable()
print(global_variable) 
""" Here if you give the local variable to print, It will throw some error saying that "I do not know any local variable to print it out".
    This is because the local variable which is defined inside the function has no memory outside of it. Hence it is known as the local 
    variable.
"""

# Positional Arguments
def say(name, age):
    print(f"Hello, {name}! You are {age} years old.")
say("Nithin", 23) 
""" If you have changed the 'age' as 'Nithin' and name as '23'. Positional argument do not have that much memory to sort the situation.
    So it will print the output as Hello 23! You are Nithin years old. Which is absolutely wrong. Hence we have keyword arguments.
"""

# Keyword Arguments
def say(name, age):
    print(f"Hello, {name}! You are {age} years old.")
say(name = "Vinay", age = 30) # Here it can have key/value pair for the better understanding.


# BUILT_IN FUNCTIONS

a = [1,2,3,4,5,6,7,8,9,10,11,12,22,24324,212]

# These are some example built_in fucntions that can be used and there are many more built_in functions availble on internet!
print(max(a))
print(min(a))
print(sum(a))
print(len(a)) 


# MAP AND REDUCE FUNCTIONS 

def addition(n):
    return n + n

numbers = (1,2,3,4,5,6,7)
result = map(addition, numbers) # MAP ---> Combines both the above(addition function and below numbers)
print(list(result)) # Converts the result to list and prints it out 


from functools import reduce

lis = [1,2,3,4,5,6,3,2,1]
def multiply(x,y):
    return x * y

result = reduce(multiply, numbers) # Used to apply a given function cumulatively to the items of an iterable (like a list), from left to right, so as to reduce the iterable to a single value. It is part of the functools module.
print(result)


# PACKAGES AND MODULES
"""
A package is a collection of Python modules organized under a common namespace. 
It is essentially a directory containing a special __init__.py file, which can be empty or contain package initialization code.
mypackage/
    __init__.py
    module1.py
    module2.py
"""
# Defining a function greet in a "virtual" module1
def module1_greet():
    print("Hello from module1!")

# Defining a function farewell in a "virtual" module2
def module2_farewell():
    print("Goodbye from module2!")

# Simulating the use of a package by calling the functions
if __name__ == "__main__":
    # Calling the function greet from the simulated module1
    module1_greet()
    
    # Calling the function farewell from the simulated module2
    module2_farewell()
print("Modules Executed")
   

# OBJECT ORIENTED PROGRAMMING(oop)

# Encapsulation and Abstraction

class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        return self.__name

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age")

# Inheritance and Polymorphism

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # Abstract method

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        print(f"{self.name} says Meow!")

# Composition

class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car has an Engine

    def start(self):
        self.engine.start()
        print("Car started")

# Association

class Author:
    def __init__(self, name):
        self.name = name

    def write_book(self):
        print(f"{self.name} is writing a book")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author  # Book has an association with Author

    def show_author(self):
        print(f"The author of '{self.title}' is {self.author.name}")

# Aggregation

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

class Employee:
    def __init__(self, name):
        self.name = name

# Demonstration of all concepts

# Encapsulation
person = Person(name="Alice", age=30)
print(person.get_name())  # Output: Alice
person.set_age(35)
person.set_age(-5)  # Output: Invalid age

# Inheritance and Polymorphism
dog = Dog(name="Buddy", breed="Golden Retriever")
cat = Cat(name="Whiskers", breed="Siamese")

dog.speak()  # Output: Buddy says Woof!
cat.speak()  # Output: Whiskers says Meow!

# Composition
car = Car()
car.start()

# Association
author = Author(name="J.K. Rowling")
book = Book(title="Harry Potter", author=author)
book.show_author()  # Output: The author of 'Harry Potter' is J.K. Rowling

# Aggregation
dept = Department(name="HR")
emp1 = Employee(name="John")
emp2 = Employee(name="Jane")

dept.add_employee(emp1)
dept.add_employee(emp2)

print(f"Department: {dept.name}")
for emp in dept.employees:
    print(f"Employee: {emp.name}")

# Output:
# Department: HR
# Employee: John
# Employee: Jane
