food_input: str = input("Enter your favorite foods, separated by commas: ")
print("\n")
food_list: list = food_input.split(",")
cleaned_list: list = []
for food in food_list:
    clean_food: str = food.strip().capitalize()
    cleaned_list.append(clean_food)
list_length: int = len(cleaned_list)
print(f"You entered {list_length} favorite foods.")
sorted_foods: list = sorted(cleaned_list)
print("Here they are in alphabetical order:")
print(sorted_foods)
print()
top_three = f"Your top three favorite foods are: {sorted_foods[0]}, {sorted_foods[1]}, and {sorted_foods[2]}."
print(top_three)