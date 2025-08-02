"""
Module aims to:
1. Manage item interaction:
    A. Picking Up
    B. Dropping
    C. Usage
"""

from character import Character

class Item():

    item_effects: dict = {
        "Health Potion": {
            "health": 20
        },
        "Magic Scroll": {
            "magic": 10
        },
        "Food": {
            "health": 2
        },
        "Water": {
            "health": 2
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
        "Enchanted Sword": {
            "strength": 15
        },
    }

    def __init__(self) -> None:
        pass

    @staticmethod
    def item_messages(item):
        """
        Print out proper item usage message
        """
        usage_message: dict = {
            "Health Potion": "You used the Health Potion and gained 20 health points!",
            "Magic Scroll": "You used the Magic Scroll and gained 10 magic points!",
            "Food": "You ate the food.",
            "Water": "You drank the water.",
            "Shield": "You used the shield and your strength increased by 5!",
            "Old Sword": "You used Old Sword and your strength increased by 10!",
            "Enchanted Amulet": "You used the Enchanted Amulet and gained 5 health and 5 magic!",
            "Ancient Scroll": "You used the Ancient Scroll and your level increased by 1!",
            "Enchanted Sword": "You used the Enchanted Sword and your strength increased by 15!",
            "Ancient Relic": "You used the Ancient Relic and revealed a hidden path!",
            "Gold Coin": "You traded the Gold Coin!",
        }
        return usage_message.get(item, f"You used {item}.")

    @staticmethod
    def use_item(character: Character, item: str):
        """
        Applies the item's effect and removes it from the inventory
        """
        item_effects = Item.item_effects.get(item, {})
        if item_effects:
            character.update_character(**item_effects)
            character.remove_from_inventory(item)
            print(Item.item_messages(item))
        else:
            print(f"You don't have {item} in your inventory.")

    @staticmethod
    def pick_up_item(character: Character, items_at_location: dict, item: str):
        """
        Adds an item from the current location to the character's inventory
        """
        x, y = character.location
        if item in items_at_location.get((x,y), []): 
            character.add_to_inventory(item)
            items_at_location[(x,y)].remove(item)
    
    @staticmethod
    def drop_item(character: Character, items_at_location: dict, item: str):
        """
        Drops an item from the current inventory and places it at the current location
        """
        x, y = character.location
        if item in character.inventory:
            character.remove_from_inventory(item)
            items_at_location[(x,y)].append(item)
    
    @staticmethod
    def manage_items(command: str, character: Character, items_at_location: dict):
        """
        Routes item commands (pick up, drop & use) to appropriate handlers
        """
        item: str = command[2:].strip()

        if command.startswith('p '):
            Item.pick_up_item(character, items_at_location, item)
        
        elif command.startswith('d '):
            Item.pick_up_item(character, items_at_location, item)