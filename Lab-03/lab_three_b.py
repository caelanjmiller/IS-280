import random

# Task 1

end_number: int = int(input("Enter a number: "))
i: int = 1
while i <= end_number:
    print(i)
    i += 1

# Task 2

for number in range(1, 11):
    print(number)

# Task 3

start_number: int = int(input("Enter a starting number: "))
while start_number != 0:
    print(start_number)
    start_number -= 1

for i in range(0, start_number):
    print(start_number)
    start_number -= 1
    

# Task 4

for outer_number in range(1,6):
    for inner_number in range(1,6):
        print(f"{outer_number} * {inner_number} = {outer_number * inner_number}")

# Task 5

target_number: int = random.randint(1,10)
guess: int = int(input("Guess the number (between 1 and 10): "))

while guess != target_number:
    if guess < target_number:
        print("Too low!")
    elif guess > target_number:
        print("Too high!")
    guess: int = int(input("Try again: "))
print(f"Correct! The number was {target_number}")
    

# Task 6

for i in range(1, 11):
    if i % 5 == 0:
        print(i)
        break
    elif i % 2 == 0:
        continue
    else:
        print(i)

# Task 7

for i in range(1, 11):
    number: int = i
    if number % 4 == 0:
        print(f"Found number divisible by 4: {number}")
        break
    if number == 10:
        print("No numbers divisible by 4.")
    


# Task 8

colors: list = ["red", "green", "blue", "yellow"]

for index, color in enumerate(colors):
    print(f"{index}: {color}")