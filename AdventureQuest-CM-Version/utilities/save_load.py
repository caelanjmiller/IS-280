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
    save_lines.append(f"{character['name']},{character['health']},{character['strength']},"
                f"{character['level']},{character['gold']},{character['magic']},"
                f"{character['location'][0]},{character['location'][1]}\n")
    save_lines.append("Inventory," + ",".join(character['inventory']) + "\n")
    save_lines.append("ItemsAtLocation\n")
    for loc, items in location_items.items():
        line = f"{loc[0]},{loc[1]}"
        if items:
            line += "," + ",".join(items)
        save_lines.append(line + "\n")
    for quest, info in character['quests'].items():
        save_lines.append(f"{quest},{info['status']}\n")
    save_lines.append("---\n")

    lines = lines[:i] + save_lines + lines[i:]
    with open(filename, "a") as save_file:
        save_file.writelines(lines)

def load_game(character_name):
    """
    Load in state of Adventure Quest from text file
    """
    with open(filename, "r") as save_file:
        return {}


filename = "players.txt"