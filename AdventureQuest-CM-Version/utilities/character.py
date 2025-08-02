"""
Module aims to:
1. Initialize new characters
2. Handle character stats & inventory
"""

def create_character() -> dict:
    """
    Creates a new character via player input(s)
    """
    print("Create your Character!\n")
    character_name: str = input("Enter your character's name: ")
    character: dict = default_character.copy()
    character['name'] = character_name
    print(f"Character created! Name: {character['name']}, Health: {character['health']}, Strength: {character['strength']}\n")
    return character

def update_character(character, changes):
    """
    Updates character stats based upon provided in game changes
    """
    for key, value in changes.items():
        character[key] += value

def view_inventory(character):
    """
    Displays the character's current inventory
    """
    print("Inventory:", ", ".join(character["inventory"]))

def add_to_inventory(character, item):
    """
    Adds an item to the character's inventory
    """
    character['inventory'].append(item)
    print(f"You picked up {item}.")

def remove_from_inventory(character, item):
    """
    Removes an item from the character's inventory
    """
    if item in character["inventory"]:
        character["inventory"].remove(item)

default_character = {
    'name': "",
    'health': 100,
    'strength': 10,
    'level': 1,
    'gold': 0,
    'inventory': ['Food', 'Water'],
    'magic': 0,
    'location': (0, 0)
}

inCombat: bool = False