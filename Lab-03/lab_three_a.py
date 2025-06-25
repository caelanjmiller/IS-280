# Task 1

numbers_list: list = []
print("Enter five numbers:")
for number in range(5):
    number_input: float = float(input(f"Number {number + 1}: "))
    numbers_list.append(number_input)

print(f"Numbers: {numbers_list}")

total_sum: float = sum(numbers_list)
average_value: float = total_sum / len(numbers_list)
max_value: float = max(numbers_list)
min_value: float = min(numbers_list)

print(f"Sum: {total_sum}")
print(f"Average: {average_value}")
print(f"Min: {min_value}")
print(f"Max: {max_value}")

# Task 2

user_grade: int = int(input("Enter your grade: "))
if user_grade >= 90 and user_grade <= 100:
    letter_grade: str = "A"
    print(f"Your letter grade is: {letter_grade}")
elif user_grade >= 80 and user_grade <= 89:
    letter_grade: str = "B"
    print(f"Your letter grade is: {letter_grade}")
elif user_grade >= 70 and user_grade <= 79:
    letter_grade: str = "C"
    print(f"Your letter grade is: {letter_grade}")
elif user_grade >= 60 and user_grade <= 69:
    letter_grade: str = "D"
    print(f"Your letter grade is: {letter_grade}")
elif user_grade >= 0 and user_grade <= 59:
    letter_grade: str = "F"
    print(f"Your letter grade is: {letter_grade}")
else:
    print("Invalid grade entered.")

# Task 3

user_age: int = int(input("Enter your age: "))

if user_age >= 0 and user_age <= 12:
    print("You are a child.\n")
elif user_age >= 13 and user_age <= 19:
    print("You are a teenager.\n")
elif user_age >= 20 and user_age <= 64:
    print("You are an adult.\n")
elif user_age >= 65:
    print("You are a senior.\n")
else:
    print("Invalid age entered.\n")

# Task 4

user_age: int = int(input("Enter your age: "))

can_drive: bool = True if user_age >= 16 else False
can_vote: bool = True if user_age >= 18 else False

if can_drive and can_vote:
    print("You can drive and vote.")
elif can_drive and not can_vote:
    print("You can drive but cannot vote.")
else:
    print("You can neither drive nor vote.")

# Task 5

fruits_list: list = ["apple", "banana", "cherry", "date"]
user_fruit: str = input("Enter a fruit name: ").lower()

if user_fruit in fruits_list:
    print("Fruit is available")
else:
    print("Fruit is not available")


# Task 6

list_a: list = [1,2,3]
list_b: list = list_a

if list_a is list_b:
    print(f"list_a and list_b refer to the same object")
else:
    print(f"list_a and list_b do not refer to the same object")

# Task 7

test_score: float = float(input("Enter your test score: "))
test_result: str = "Pass" if test_score >= 60 else "Fail"
print(f"{test_result}")

# Task 8
string_one: str = input("Enter the first string: ")
string_two: str = input("Enter the second string: ")

if string_one == string_two:
    print(f"{string_one} is equal to {string_two}")
elif string_one < string_two:
    print(f"{string_one} comes before {string_two}")
elif string_one > string_two:
    print(f"{string_one} comes after {string_two}")