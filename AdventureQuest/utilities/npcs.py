"""
Module aims to:
1. Define NPCs and their locations on the game map
2. Initialize these NPCs in main.py
3. Provide functionality for:
    A. Trading
    B. Quests
    C. Interactions
"""

from utilities.quests import *
from utilities.save_load import wrapped_text, wrapped_text_prompt

# Renaming NPCs dict to npcs_aq due to namespace collisions I experienced with my function in main.py
npcs_aq = {
    (0, 1): {
        "name": "Elder",
        "quest": "Retrieve Ancient Scroll",
        "interaction": "The Elder looks at you expectantly.",
        "dialogue": "The scroll lies deep within the Enchanted Castle. We must recover it before darkness falls."
    },
    (1, 3): {
        "name": "Merchant",
        "quest": "Trade with the Merchant",
        "interaction": "The Merchant sizes you up with a practiced eye.",
        "dialogue": "Gold talks and gear walks. Care to make a deal, traveler?"
    },
    (2, 0): {
        "name": "Warrior",
        "quest": "Test of Strength",
        "interaction": "The Warrior cracks his knuckles and smirks at you.",
        "dialogue": "Let's see what you're made of. Best me in combat, and I'll respect your strength."
    },
    (3, 2): {
        "name": "Healer",
        "quest": "Healing Aid",
        "interaction": "The Healer gently examines your wounds.",
        "dialogue": "Rest easy. I can mend your wounds… for a fair price."
    },
    (4, 0): {
        "name": "Mystic",
        "quest": "Treasure Hunt Clues",
        "interaction": "through you as if seeing your fate.",
        "dialogue": "Fate twists lie a river... bring me a token of value, and I shall read the currents for you."
    },
    (2, 4): {
        "name": "Guard Captain",
        "quest": "Defend the Village",
        "interaction": "The Guard Captain grips his sword tightly, eyes alert.",
        "dialogue": "Our scouts spotted movement beyond the ridge. Will you stand with us when the time comes?"
    },
    (1, 1): {
        "name": "Scholar",
        "quest": "The Scholar's Collection",
        "interaction": "The Scholar flips through an ancient tome, barely noticing you.",
        "dialogue": "Curious... I need specimens not found in these parts. Bring them to me and be rewarded."
    },
    (3, 4): {
        "name": "Blacksmith",
        "quest": "Weapon Upgrade",
        "interaction": "The Blacksmith inspects your equipment with a critical eye.",
        "dialogue": "Your blade’s seen better days. I can forge it anew — if you’ve got the coin.'"
    },
    (0, 3): {
        "name": "Adventurer",
        "quest": "Locate Hidden Relic",
        "interaction": "The Adventurer leans in with a grin, eager to talk.",
        "dialogue": "Heard tales of a relic buried beneath the cliffs. Think you’ve got the guts to find it?"
    }
}

def initialize_npcs():
    """
    Sets up NPCs, their locations and associated quests
    """
    return npcs_aq

def interact_with_npc(character, location):
    """
    Displays dialogue and allows interaction with the NPC at the current location
    """
    npc_info: dict = npcs_aq.get(location, {})
    if npc_info:
        npc_name: str = npc_info['name']
        npc_dialogue: str = npc_info['dialogue']
        npc_quest: str = npc_info['quest']
        wrapped_text(f"You meet the {npc_name}!")
        print()
        wrapped_text(f"{npc_name}: {npc_dialogue}")
        print()
        choice: str = wrapped_text_prompt(f"Do you want to accept the quest '{npc_quest}'?", "(yes/no): ")
        if choice.lower() == "yes":
            npc_give_quest(npc_name, character)
        elif choice.lower() == "no":
            wrapped_text(f"You declined '{npc_quest}'")
        else:
            wrapped_text(f"Invalid choice.")
    else:
        return

def npc_give_quest(npc_name, character):
    """
    Initiates a quest from the specified NPC
    """
    for npc in npcs_aq.values():
        if npc['name'] == npc_name:
            quest_name = npc['quest']
            accept_quest(quest_name, character)
            break

def npc_trade(npc_name, character):
    """
    Handles item trading with NPCs
    """
    pass