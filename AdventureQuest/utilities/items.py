"""
Module aims to:
1. Manage item interaction:
    A. Picking Up
    B. Dropping
    C. Usage
"""

def pick_up_items(character: dict, items_at_location: dict):
    """
    Adds an item from the current location to the character's inventory
    """
    pass

def drop_item(character: dict, items_at_location: dict):
    """
    Drops an item from the current inventory and places it at the current location
    """
    pass

def manage_items(command: str, character: dict, items_at_location: dict):
    """
    Routes item commands (pick up, drop & use) to appropriate handlers
    """
    pass