"""
Module aims to:
1. Save game into text file
2. Load in previous save from text file
3. Misc function to clear terminal screen
4. Misc function to wrap text
"""
import os
import textwrap


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

def save_game(character, location_items):
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
        for quest, info in character['quests'].items():
            print(f"{quest},{info['status']}")
        save_file.write("---\n")

def load_game(character_name):
    """
    Load in state of Adventure Quest from text file
    """
    with open(filename, "r") as save_file:
        return {}


filename = "players.txt"