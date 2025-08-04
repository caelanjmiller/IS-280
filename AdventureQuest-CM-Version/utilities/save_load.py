"""
Module aims to:
1. Save game into text file
2. Load in previous save from text file
3. Misc function to clear terminal screen
4. Misc function to wrap text
"""
import os
import textwrap
from utilities.character import Character
from utilities.items import Item, item_registry
from utilities.quests import Quest, quests

def clearScreen(delay=True):
    """
    Clear the terminal screen upon input (Enter)
    """
    if delay:
        input("Press Enter to continue...")
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def wrapped_text(text: str):
    """
    Wrap text for terminal throughout Adventure Quest
    """
    wrapped_text: str = textwrap.fill(text, width=80)
    for line in wrapped_text.splitlines():
        print(f"{line:<76}")
    
def wrapped_text_prompt(text: str, prompt: str = ""):
    """
    Wrap text (input) for terminal throughout Adventure Quest 
    """
    wrapped_text(text)
    return input(prompt)
class SaveLoad():
    def __init__(self, filename="players.txt") -> None:
        self.filename = filename
    
    def save_game(self, player: Character, items_at_location: dict, filename="players.txt"):
        """
        Save state of Adventure Quest into a text file
        """
        try:
            with open(filename, "r") as save_file:
                lines = save_file.readlines()
        except FileNotFoundError:
            lines = []

        i = 0
        while i < len(lines) and lines[i].strip() != "---":
            i += 1
        if i < len(lines):
            i += 1

        save_lines = []
        save_lines.append("Character\n")
        save_lines.append(f"{player.name},{player.health},{player.strength},"
                    f"{player.level},{player.gold},{player.magic},"
                    f"{player.location[0]},{player.location[1]}\n")
        save_lines.append("Inventory," + ", ".join(item.name for item in player.inventory) + "\n")
        save_lines.append("ItemsAtLocation\n")
        for loc, items in items_at_location.items():
            line = f"{loc[0]},{loc[1]}"
            if items:
                line += "," + ",".join(str(items))
            save_lines.append(line + "\n")
        for quest in player.quests:
            save_lines.append(f"{quest.name},{quest.status}\n")
        save_lines.append("---\n")

        lines = lines[:i] + save_lines + lines[i:]
        with open(filename, "a") as save_file:
            save_file.writelines(lines)

    def load_game(self, player_name: str):
        """
        Load prior user's game save
        """
        try:
            with open("players.txt") as file:
                lines = file.read().splitlines()
        except FileNotFoundError:
            wrapped_text(f"Save File Not Found")
            return None

        starting_index = None

        for index, line in enumerate(lines):
            if line.strip() == "Character":
                if index + 1 < len(lines):
                    name = lines[index + 1]
                    if name.startswith(player_name + ","):
                        starting_index = index
                        break
            if starting_index is None:
                wrapped_text(f"Player '{player_name}' not found in save file.")
                return None
        
        save_data: list = []
        for line in lines[starting_index:]:
            if line.strip() == "---":
                break
            save_data.append(line)
        
        character_stats = save_data[1].split(",")
        name = character_stats[0]
        health, strength, level, gold, magic = character_stats[1:6]
        location = (save_data[5], save_data[6])
        character: Character = Character(name=name, health=health, strength=strength, level=level, gold=gold, magic=magic, location=location)

        if "Inventory" in save_data:
            inventory_index = save_data.index("Inventory")
            if inventory_index + 1 < len(save_data):
                inventory_items = [item.strip() for item in save_data[inventory_index + 1].split(",") if item.strip()]
                for item_name in inventory_items:
                    if item_name in item_registry:
                        character.add_to_inventory(item_registry[item_name])
        
        items_at_location: dict = {}

        if "ItemsAtLocation" in save_data:
            location_index = save_data.index("ItemsAtLocation") + 1
            for index in range(location_index, len(save_data)):
                line = save_data[index].strip()
                if not line or line.startswith("Quests"):
                    break
                locations_and_items = [entry.strip() for entry in line.split(",")]
                x_coordinate = int(locations_and_items[0])
                y_coordinate = int(locations_and_items[1])

                item_names = locations_and_items[2:]
                items_in_this_location: list = []
                for item_name in item_names:
                    if item_name in item_registry:
                        matched_item = item_registry[item_name]
                        item_copy = Item(
                            name=matched_item.name,
                            health=matched_item.health,
                            magic=matched_item.magic,
                            strength=matched_item.strength,
                            level=matched_item.level
                        )
                        items_in_this_location.append(item_copy)
                
                items_at_location[(x_coordinate, y_coordinate)] = items_in_this_location

        if "Quests" in save_data:
            quests_index = save_data.index("Quests") + 1
            for line in save_data[quests_index:]:
                if not line.strip():
                    break
                name_of_quest, status = [data.strip() for data in line.split(",", 1)]
                if name_of_quest in quests:
                    quest = Quest(name_of_quest, quests[name_of_quest])
                    quest.status = status
                    character.quests.append(quest)
        
        wrapped_text(f"Successfully loaded player '{player_name}'.")
        return character, items_at_location