# Task 1: IO

# User prompt for demographics
first_name: str = input("What is your first name?: ")
last_name: str = input("What is your last name?: ")
# Input is of str type, so type cast to integer
age: int = int(input("What is your age?: "))

# Print out demographic information
print(f"Hello, {first_name} {last_name}! You are {age} years old.")

# Task 2: Variables

# Account for real prices as floats
item_one: float = float(input("Price of Item One: "))
item_two: float = float(input("Price of Item Two: "))
item_three: float = float(input("Price of Item Three: "))

# Group all three numbers in list & calculate sum over it
subtotal: float = sum([item_one, item_two, item_three])
tax: float = subtotal * 0.085
total: float = subtotal + tax

# Print all three values
print(f"Subtotal: {subtotal:.2f}\nTax: {tax:.2f}\nTotal: {total:.2f}")

# Task 3: String Basics
favorite_color: str = input("What is your favorite color?: ")
print(f"Length of your favorite color: {len(favorite_color)} characters")

# Task 4: Number Basics
num_1: float = float(input("Number 1: "))
num_2: float = float(input("Number 2: "))
results: float = sum([num_1, num_2])
print(f"Sum of Number 1 & 2: {results}")

# Task 5: Error Message
print('Original statement:  print(Hello" ')
print('Corrected statement: print("Hello")')

# Task 6: Comments

# Creating a function that prints both an inline program and docstring; returns None since we're only printing
def string_and_docstring() -> None:
    """
    This script prints a simple message
    """
    # Display a greeting
    print("Welcome to Python!")

string_and_docstring()