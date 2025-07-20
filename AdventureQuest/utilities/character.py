"""
Module aims to:
1. Initialize new characters
2. Handle character stats & inventory
"""

def createCharacter() -> dict:
    """
    Creates a new character via player input(s)
    """
    print("Create your Character!\n")
    character_name: str = input("Enter your character's name: ")
    character: dict = default_character.copy()
    character['name'] = character_name
    print(f"Character created! Name: {character['name']}, Health: {character['health']}, Strength: {character['strength']}\n")
    return character

def update_character(character: dict, changes: dict):
    """
    Updates character stats based upon provided in game changes
    """
    for char_stat, effect in changes.items():
        if char_stat in character:
            character[char_stat] += effect
        else:
            character[char_stat] = effect

def view_inventory(character):
    """
    Displays the character's current inventory
    """
    print("=" * 80)
    print(f"{'Inventory':^80}")
    print("=" * 80)
    print("You are carrying:")
    for item in character['inventory']:
        print(f"- {item}")
    print("=" * 80)

def add_to_inventory(character, item):
    """
    Adds an item to the character's inventory
    """
    if item not in character['inventory']:
        character['inventory'].append(item)
        print(f"You picked up {item}.")

def remove_from_inventory(character, item):
    """
    Removes an item from the character's inventory
    """
    if item in character['inventory']:
        character['inventory'].remove(item)
        print(f"You dropped {item}.")

default_character: dict = {
    'health' : 100,
    'strength': 10,
    'level': 1,
    'gold': 0,
    'inventory': ['Food', 'Water'],
    'magic': 0,
    'location': (0,0),
}

inCombat: bool = False