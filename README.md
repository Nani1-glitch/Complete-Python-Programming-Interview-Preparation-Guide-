
markdown
Copy code
# 📚 Python Programming Basics for Beginners

Welcome to the ultimate guide for Python programming basics! This repository is designed to help beginners get started with Python in a fun and engaging way. Let's dive into the world of Python with practical examples, explanations, and exercises.

## 📑 Table of Contents

1. [BODMAS Rule](#bodmas-rule)
2. [Data Types and Conversion](#data-types-and-conversion)
3. [String Slicing](#string-slicing)
4. [Relational and Logical Operators](#relational-and-logical-operators)
5. [Conditional Statements](#conditional-statements)
6. [Loops](#loops)
7. [String Methods](#string-methods)
8. [Nested Loops](#nested-loops)
9. [Loop Control Statements](#loop-control-statements)
10. [Collections: Lists, Tuples, Dictionaries, and Sets](#collections)
11. [Functions](#functions)
12. [Built-in Functions](#built-in-functions)
13. [Map and Reduce Functions](#map-and-reduce-functions)

## ✏️ BODMAS Rule

```python
a = 10 + 5 * (2**3) - 6/2
print(a)  # Output: 48.0
🔄 Data Types and Conversion
python
Copy code
a = 324523.24512312
print(type(a))  # Output: <class 'float'>

num_int = str(a)
print(num_int)
print(type(num_int))  # Output: <class 'str'>
✂️ String Slicing
python
Copy code
my_string = "Nithin Rajulapati"
print(my_string[0:6])  # Output: Nithin

b = "Let us start learning Python programming from today!"
print(b[0:21])  # Output: Let us start learning
⚖️ Relational and Logical Operators
python
Copy code
c = 5
d = 4
print(c < d)  # Output: False

print(0.1 + 0.1 + 0.1 == 0.3)  # Output: False

a = 5 > 3
b = 4 < 2
print(a and b)  # Output: False
print(a or b)  # Output: True

c = 4 > 3
print(not c)  # Output: False

print("Nithin" == "Nithin")  # Output: True
🛤️ Conditional Statements
python
Copy code
age = int(input("Enter the age to calculate: "))

if age > 18:
    print("You are adult!")
else:
    print("Pilla bacha nayala...")

if age < 18:
    print("You are an pilla bacha")
elif age >= 18 and age < 60:
    print("You are an adult")
else:
    print("emundi le poduko inka (senior citizen)")
🔄 Loops
While Loop
python
Copy code
start = 1
while start <= 20:
    print(start)
    start += 1

count = 10
while count > 0:
    print(count)
    count -= 1
For Loop
python
Copy code
for num in range(1, 10):
    print(num)

for each in "hello":
    print(each)

string = " "
for num in range(1, 10):
    string = string + str(num) + " "
print(string)
🧵 String Methods
python
Copy code
string = "Hello! How aRe yoU tODay?"
print(len(string))  # Output: 24
print(string.lower())  # Output: hello! how are you today?
print(string.strip())  # Output: Hello! How aRe yoU tODay?
print(string.replace("Hello", "Heyyyy"))  # Output: Heyyyy! How aRe yoU tODay?
🔄 Nested Loops
python
Copy code
n = int(input("Enter the no.of lines to print: "))
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print()
🔄 Loop Control Statements
Break and Continue
python
Copy code
for num in range(1, 10):
    if num == 7:
        break
    print(num)

for num in range(1, 20):
    if num % 2 == 0:
        continue
    print(num)
📚 Collections
Lists
python
Copy code
num = [1, 2, 3, 4, 5]
num[1] = "nithin"
num1 = ["Nithin", "Hello", "How", "are", "You"]
num1.append("Hey")  # Adds the string_value at the end of the list
print(num1)
Tuples
python
Copy code
a = (1, 2, 34, 3, 12, 13, "nithin")
print(type(a))  # Output: <class 'tuple'>
Dictionaries
python
Copy code
student = {
    "name": "Nithin Rajulapati",
    "age": 23,
    "major": "AI",
    "gpa": 3.55
}
print(student["age"])  # Output: 23
Sets
python
Copy code
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {6, 7, 8, 9, 10, 11, 12}

union_set = set1.union(set2)
print(union_set)

intersection_set = set1.intersection(set2)
print(intersection_set)

difference_set = set1.difference(set2)
print(difference_set)

symmetric_difference = set1.symmetric_difference(set2)
print(symmetric_difference)
🔧 Functions
Basic Functions
python
Copy code
def add(a, b):
    return a + b
a = add(2, 3)
print(a)  # Output: 5

def greet(name):
    print(f"Hello, {name}")
greet("Nithin")
Scope of Variables
python
Copy code
global_variable = "I'm Global"
def function_with_local_variable():
    local_variable = "I'm Local"
    print(global_variable)
    print(local_variable)
function_with_local_variable()
print(global_variable)
Positional and Keyword Arguments
python
Copy code
def say(name, age):
    print(f"Hello, {name}! You are {age} years old.")
say("Nithin", 23)

def say(name, age):
    print(f"Hello, {name}! You are {age} years old.")
say(name="Vinay", age=30)
🔍 Built-in Functions
python
Copy code
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 22, 24324, 212]
print(max(a))
print(min(a))
print(sum(a))
print(len(a))
🔄 Map and Reduce Functions
python
Copy code
def addition(n):
    return n + n

numbers = (1, 2, 3, 4, 5, 6, 7)
result = map(addition, numbers)
print(list(result))
