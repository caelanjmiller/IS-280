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

class Save:
    def __init__(self, filename="players.txt") -> None:
        self.filename = filename
    
    def save_game(self, player: Character, items_at_location: dict, quests: dict)
        """
        Save state of Adventure Quest into a text file
        """
        try:
            with open(self.filename, "r") as save_file:
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
        for quest, info in player.quests.items():
            save_lines.append(f"{quest},{info['status']}\n")
        save_lines.append("---\n")

        lines = lines[:i] + save_lines + lines[i:]
        with open(self.filename, "a") as save_file:
            save_file.writelines(lines)

    def load_game(self, player_name: str) -> Character:
        """
        Load prior user's game save
        """
        return Character("pass")