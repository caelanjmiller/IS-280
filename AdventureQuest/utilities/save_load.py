"""
Module aims to:
1. Save game into text file
2. Load in previous save from text file
3. Misc function to clear terminal screen
"""

from pathlib import Path
import os

def clearScreen(delay=True):
    """
    Clear the terminal screen upon input (Enter)
    """
    if delay:
        input("Press Enter to Continue")
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def save_game(character: dict, location_items: dict):
    """
    Save state of Adventure Quest into a text file
    """
    with open(filename, "a") as save_file:
        save_file.write("Character\n")
        save_file.write(f"{character['name']},{character['health']},{character['strength']},"
                   f"{character['level']},{character['gold']},{character['magic']},"
                   f"{character['location'][0]},{character['location'][1]}\n")
        save_file.write("Inventory," + ",".join(character['inventory']) + "\n")
        save_file.write("ItemsAtLocation\n")
        for loc, items in location_items.items():
            line = f"{loc[0]},{loc[1]}"
            if items:
                line += "," + ",".join(items)
            save_file.write(line + "\n")
        save_file.write("---\n")

def load_game(character_name: str) -> dict:
    """
    Load in state of Adventure Quest from text file
    """
    with open(filename, "r") as save_file:
        return {}


filename: Path = Path("players.txt")

