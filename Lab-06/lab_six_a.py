import math
 
# Task 1 Basic Function Creation
print("Task 1 Basic Function Creation")
def greetUser(name: str):
    print(f"Hello {name}!")

name: str = input("What is your name? ")
greetUser(name)
print()

#Task 2 Returning Values 
print("Task 2 Returning Values")
def computeArea(radius):
    area: float = math.pi * pow(radius, 2)
    print(f"The area of a circle with radius {radius} is {area:.2f}")

radius: float = float(input("Enter the radius of a circle: "))
computeArea(radius)
print()

#Task 3 Parameters and Scope
print("Task 3 Parameters and Scope")
def sumOfSquares(a, b):
    sum_of_squares: int = pow(a, 2) + pow(b, 2)
    print(f"The sum of the squares of {a} and {b} is {sum_of_squares}")

a: int = int(input("Enter a number: "))
b: int = int(input("Enter another number: "))
sumOfSquares(a, b)
print()

#Task 4 Optional Parameters
print("Task 4 Optional Parameters")
def fullName(firstName, lastName, middleName=""):
    if middleName:
        print(f"{firstName} {middleName} {lastName}")
    else:
        print(f"{firstName} {lastName}")

firstName: str = input("Enter your first name: ")
middleName: str = input("Enter your middle name if you have one, if not just hit Enter: ")
lastName: str = input("Enter your last name: ")
fullName(firstName, lastName, middleName)
print()

#Task 5 Function with a Control Structure
print("Task 5 Function with a Control Structure")
def gradeClassifier(score):
    if score >= 90:
        grade = "A"
    elif score >= 80 and score < 90:
        grade = "B"
    elif score >= 70 and score < 80:
        grade = "C"
    elif score >= 60 and score < 70:
        grade = "D"
    else:
        grade = "F"
    print(f"Your grade is {grade}")

score: int = int(input("Enter your score: "))
gradeClassifier(score)
print()

#Task 6 Variable Scope
print("Task 6 Variable Scope")
def modifyVariable():
    x: int = 20
    print(f"Inside the function, after modification, x = {x}")
    return x

x: int = 10
print(f"Inside the function, before modification, x = {x}")
x: int = modifyVariable()
print(f"Outside the function, x = {x}")