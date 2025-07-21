"""
Module aims to:
1. Manage item interaction:
    A. Picking Up
    B. Dropping
    C. Usage
"""

import utilities.character as char

def pick_up_item(character: dict, items_at_location: dict, item: str):
    """
    Adds an item from the current location to the character's inventory
    """
    x, y = character['location']
    if item in items_at_location.get((x,y), []): 
        char.add_to_inventory(character, item)
        items_at_location[(x,y)].remove(item)

def drop_item(character: dict, items_at_location: dict, item: str):
    """
    Drops an item from the current inventory and places it at the current location
    """
    x, y = character['location']
    if item in character['inventory']:
        char.remove_from_inventory(character, item)
        items_at_location[(x,y)].append(item)

def use_item(character: dict, item: str):
    """
    Applies the item's effect and removes it from the inventory
    """
    effects: dict = item_effects[item]
    char.update_character(character, effects)

def manage_items(command: str, character: dict, items_at_location: dict):
    """
    Routes item commands (pick up, drop & use) to appropriate handlers
    """
    item: str = command[2:].strip()

    if command.startswith('p '):
        pick_up_item(character, items_at_location, item)
    
    elif command.startswith('d '):
        pick_up_item(character, items_at_location, item)

item_effects: dict = {
    "Health Potion": {
        "health": 20
    },
    "Magic Scroll": {
        "magic": 10
    },
    "Food": {

    },
    "Water": {

    },
    "Shield": {
        "strength": 5
    },
    "Old Sword": {
        "strength": 10
    },
    "Enchanted Amulet": {
        "health": 5,
        "magic": 5
    },
    "Ancient Scroll": {
        "level": 1
    },
    "Gold Coin": {

    },
    "Enchanted Sword": {
        "strength": 15
    },
}