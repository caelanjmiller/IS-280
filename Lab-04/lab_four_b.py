print("Task 1: Creating Lists")
colors: list = ["red", "green", "blue", "yellow"]
print(colors)
print()

print("Task 2: List Methods")
colors.append("purple")
print(colors)
print()

print("Task 3: Iterating Over a List")
for color in colors:
    print(f"Color: {color}")
print()

print("Task 4: List Games")
user_input: str = input("Guess a color: ")
while user_input not in colors:
    print("Try again.")
    user_input: str = input("Guess a color: ")
else:
    print("Correct guess!")
print()

print("Task 5: List Nesting")
points: list = [[2,3], [5,6], [8,9]]
print(points)
print()

print("Task 6: List Slicing")
print(points[:2])
print()

print("Task 7: Loops Modifying Lists")
for point in points:
    point[0] *= 2
    point[1] *= 2
print(points)
print()

print("Task 8: List Comprehensions")
squares: list = [x ** 2 for x in range(1,11)]
print(squares)
print()

print("Task 9: Sorting Lists")
print(sorted(colors))