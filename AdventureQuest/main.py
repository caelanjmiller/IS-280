from character import Character

def game_header():
    pass

def game_narrative_banner() -> str:
    narrative: str = (f"""
    Welcome to Adventure Quest!
    In this mystical land, you will embark on a thrilling journey to find the Enchanted
    Castle, rescue allies, and rebuild communities. Along the way, you will encounter 
    various challenges, meet different characters, and collect valuable resources. 
    Good luck on your adventure!
    """)
    return narrative

def character_creation_banner() -> str:
    pass


def display_main_menu():
    """
    Create main menu screen for Adventure Quest
    """
    pass

def character_creation(name: str, health: int, strength: int, inventory: list) -> Character:
    """Create a character for Adventure Quest"""
    generated_character: Character = Character(
        name,
        health,
        strength,
        inventory
    )
    return generated_character

def main_loop():
    pass


main_loop()