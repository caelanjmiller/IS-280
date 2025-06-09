print("Task 1: Input/Output")
# User prompt for demographics
first_name: str = input("Enter your first name: ")
last_name: str = input("Enter your last name: ")
# Input is of str type, so type cast to integer
age: int = int(input("Enter your age: "))

# Print out demographic information
print(f"Hello, {first_name} {last_name}! You are {age} years old.")

print("\nTask 2: Variables")

# Account for real prices as floats
item_one: float = float(input("Enter the price of item 1: "))
item_two: float = float(input("Enter the price of item 2: "))
item_three: float = float(input("Enter the price of item 3: "))

# Group all three numbers in list & calculate sum over it
subtotal: float = sum([item_one, item_two, item_three])
tax: float = subtotal * 0.085
total: float = subtotal + tax

# Print all three values
print(f"Subtotal: ${subtotal:.2f}\nTax: ${tax:.2f}\nTotal: ${total:.2f}")

print("\nTask 3: String Basics")
favorite_color: str = input("Enter your favorite color: ")
print(f"The length is {len(favorite_color)}.")

print("\nTask 4: Number Basics")
num_1: float = float(input("Enter first number: "))
num_2: float = float(input("Enter second number: "))
results: int = int(sum([num_1, num_2]))
print(f"The sum is {results}.")

print("\nTask 5: Error Message")
print("Hello")

print("\nTask 6: Comments")

# Creating a function that prints both an inline program and docstring; returns None since we're only printing
def string_and_docstring() -> None:
    """
    This script prints a simple message
    """
    # Display a greeting
    print("Welcome to Python!")

string_and_docstring()