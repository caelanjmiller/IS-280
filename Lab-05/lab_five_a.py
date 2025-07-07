# Task 1: Creating Dictionaries
print("Task 1: Creating Dictionaries")
capitals: dict = {
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}
print(capitals)
print()

# Task 2: Dictionary Methods
print("Task 2: Dictionary Methods")
capitals["Germany"] = "Berlin"
print(capitals)
print()

# Task 3: Iterating Over a Dictionary
print("Task 3: Iterating Over a Dictionary")
for country, capital in capitals.items():
    print(f"The capital of {country} is {capital}.")
print()

# Task 4: Dictionary Nesting
print("Task 4: Dictionary Nesting")
library: dict = {
    'Fantasy': {'Harry Potter': 'J.K. Rowling'}, 
    'Sci-Fi': {'Dune': 'Frank Herbert'}
}
print(library)