import random

# Task 1: Integers and Floats
length_int: int = 5
width_float: float = 3.7
area_float: float = length_int * width_float
print(f"Area of the rectangle: {area_float:.2f}")

# Task 2: Strings
user_input_str: str = input("Enter a string: ")
reverse_str: str = user_input_str[::-1]
print(f"Reversed string: {reverse_str}")


# Task 3: Lists
random_int_list: list = [random.randint(0, 100) for random_int in range(0,2)]
print(f"Updated list: {random_int_list}")


# Task 4: Tuples
mixed_data_tuple: tuple = ("STL", 3.14, "π", True)
print(f"Tuple contents: \n{mixed_data_tuple}")

# Task 5: Dictionaries
book_info_dict: dict = {
    'title': 'Unwind',
    'author': 'Neal Shusterman',
    'publication year': 2007,
    'rating': 5
}
print(f"Book information: {book_info_dict}")


# Task 6: Boolean Values
bool_var_a = True
bool_var_b = False

print(f"Logical AND: {bool_var_a and bool_var_b}")
print(f"Logical OR: {bool_var_a or bool_var_b}")
print(f"Logical NOT on A: {not bool_var_a}")


# Task 7: Sets
random_list: list = [random.randint(0, 10) for random_int in range(0,5)]
unique_numbers_set: set = set(random_list)
print(f"Original list: {random_list}")
print(f"Unique numbers set: {unique_numbers_set}")

# Task 8: Data Type Conversion
number_string: str = "123456"
number_list: list = [int(number) for number in number_string]


# Task 9: Formatting Task
large_float: float = float(input("Enter a random float $$$: "))
print(f"Formatted as currency ($): {large_float:,.2f}")