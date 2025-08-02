class Character():
    def __init__(self, name, health=100, strength=10, level=1, gold=0, inventory=None, location=(0,0), magic=0) -> None:
        self.name = name
        self.health = health
        self.strength = strength
        self.level = level
        self.gold = gold
        self.inventory = inventory if inventory is not None else ['Food', 'Water']
        self.location = location
        self.magic = magic

    def update_character(self, health=0, strength=0, gold=0):
        """
        Updates character stats based upon provided in game changes
        """
        self.health += health
        self.strength += strength
        self.gold += gold

    def view_inventory(self):
        """
        Displays the character's current inventory
        """
        if self.inventory:
            print("Inventory:", ", ".join(self.inventory))
        else:
            print(f"No items in inventory.")

    def add_to_inventory(self, item):
        """
        Adds an item to the character's inventory
        """
        self.inventory.append(item)
        print(f"You picked up {item}.")

    def remove_from_inventory(self, item):
        """
        Removes an item from the character's inventory
        """
        if item in self.inventory:
            self.inventory.remove(item)

def create_character() -> Character:
    """
    Creates a new character via player input(s)
    """
    print("Create your Character!\n")
    character_name: str = input("Enter your character's name: ")
    new_character: Character = Character(character_name)
    print(f"Character created! Name: {new_character.name}, Health: {new_character.health}, Strength: {new_character.strength}\n")
    return new_character

in_combat: bool = False