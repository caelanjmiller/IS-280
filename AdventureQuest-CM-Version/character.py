class Character():
    def __init__(self, name, health=100, strength=10, level=1, gold=0, inventory=[], location=(0,0)) -> None:
        self.name = name
        self.health = health
        self.strength = strength
        self.level = level
        self.gold = gold
        self.inventory = inventory
        self.location = location

    def update_character(self, health_change=0, strength_change=0):
        """
        Updates character stats based upon provided in game changes
        """
        self.health += health_change
        self.strength += strength_change

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

in_combat: bool = False