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

class Save:
    def __init__(self) -> None:
        pass