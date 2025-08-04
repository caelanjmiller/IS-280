from save_load import wrapped_text, wrapped_text_prompt
from items import Item
from quests import Quest

class Character():
    def __init__(self, name, health=100, strength=10, level=1, gold=0, inventory=None, location=(0,0), magic=0, quests=None) -> None:
        self.name = name
        self.health = health
        self.strength = strength
        self.level = level
        self.gold = gold
        self.inventory = inventory if inventory is not None else [Item('Food'), Item('Water')]
        self.location = location
        self.magic = magic
        self.in_combat: bool = False
        self.quests = quests

    def update_character(self, health=0, strength=0, gold=0, magic=0, level=0):
        """
        Updates character stats based upon provided in game changes
        """
        self.health += health
        self.strength += strength
        self.gold += gold
        self.magic += magic
        self.level += level

    def view_inventory(self):
        """
        Displays the character's current inventory
        """
        if self.inventory:
            print("Inventory:", ", ".join(str(item) for item in self.inventory))
        else:
            print(f"No items in inventory.")

    def add_to_inventory(self, item: Item):
        """
        Adds an item to the character's inventory
        """
        self.inventory.append(item)
        print(f"You picked up {str(item)}.")

    def remove_from_inventory(self, item: Item):
        """
        Removes an item from the character's inventory
        """
        if item in self.inventory:
            self.inventory.remove(item)

def create_character() -> Character:
    """
    Creates a new character via player input(s)
    """
    wrapped_text("Create your Character!\n")
    character_name: str = wrapped_text_prompt("Enter your character's name", ": ")
    new_character: Character = Character(character_name)
    wrapped_text(f"Character created! Name: {new_character.name}, Health: {new_character.health}, Strength: {new_character.strength}\n")
    return new_character
