"""
Module aims to:
1. Define quests for Adventure Quest
2. Handle acceptance & completion of quests
3. Checking current quest(s) progress
4. Check for quest/object interaction based upon location
"""
quests_aq = {
    "Retrieve Ancient Scroll": {
        "description": "Retrieve the Ancient Scroll from the Enchanted Castle.",
        "status": "Not Started",
        "start_location": (0, 1),
        "objective_location": (2, 2),
        "reward": {"gold": 50, "items": ["Ancient Scroll"]},
        "choices": {
            "accept": "You agree to retrieve the scroll and set off on your journey.",
            "decline": "The Elder looks disappointed."
        }
    },
    "Defend the Village": {
        "description": "Help defend the village from an imminent attack.",
        "status": "Not Started",
        "start_location": (2, 4),
        "objective_location": None,  # No specific location
        "reward": {"gold": 30, "items": ["Shield"]},
        "choices": {
            "accept": "You prepare to defend the village by gathering weapons and traps.",
            "decline": "The Guard Captain warns of the consequences."
        }
    },
    "The Scholar's Collection": {
        "description": "Gather three rare items for the Scholar's research.",
        "status": "Not Started",
        "start_location": (1, 1),
        "objective_location": None,  # Items are scattered
        "reward": {"gold": 40, "items": ["Research Notes"]},
        "choices": {
            "accept": "The Scholar thanks you and gives you a list of items to find.",
            "decline": "The Scholar expresses disappointment."
        }
    },
    "Treasure Hunt Clues": {
        "description": "The Mystic offers clues to locate hidden treasures in the Haunted Forest.",
        "status": "Not Started",
        "start_location": (4, 0),
        "objective_location": (0, 3),
        "reward": {"gold": 20, "items": ["Treasure Map"]},
        "choices": {
            "ask for advice": "The Mystic shares cryptic clues about the treasure.",
            "offer an item": "The Mystic provides a detailed map in exchange for a rare item.",
            "ignore": "You leave the Mystic without any information."
        }
    },
    "Test of Strength": {
        "description": "Prove your strength in a contest with the Warrior.",
        "status": "Not Started",
        "start_location": (2, 0),
        "objective_location": None,  # Event happens on the spot
        "reward": {"items": ["Upgraded Sword"]},
        "choices": {
            "accept": "The Warrior challenges you to a test of strength.",
            "decline": "The Warrior remarks on your lack of courage."
        }
    },
    "Healing Aid": {
        "description": "The Healer offers to restore your health or sell you a potion.",
        "status": "Not Started",
        "start_location": (3, 2),
        "objective_location": None,  # Event happens on the spot
        "reward": {"gold": -10, "items": ["Healing Potion"]},  # Cost 10 gold
        "choices": {
            "request healing": "The Healer restores your health for a fee.",
            "decline": "You leave without assistance."
        }
    },
    "Weapon Upgrade": {
        "description": "The Blacksmith offers to upgrade your weapon or armor.",
        "status": "Not Started",
        "start_location": (3, 4),
        "objective_location": None,  # Event happens on the spot
        "reward": {"items": ["Upgraded Armor"]},
        "choices": {
            "upgrade": "The Blacksmith upgrades your equipment for gold or an item.",
            "decline": "You keep your current equipment."
        }
    },
    "Trade with the Merchant": {
        "description": "The Merchant offers to trade, buy, or sell items.",
        "status": "Not Started",
        "start_location": (1, 3),
        "objective_location": None,  # Event happens on the spot
        "reward": None,  # Based on trades
        "choices": {
            "buy": "You purchase items, deducting gold from your inventory.",
            "sell": "You sell items, receiving gold in return.",
            "trade": "You exchange an item for another.",
            "decline": "You walk away from the transaction."
        }
    },
    "Locate Hidden Relic": {
        "description": "The Adventurer shares clues about a hidden relic in the Mystical City.",
        "status": "Not Started",
        "start_location": (0, 3),
        "objective_location": (4, 3),
        "reward": {"items": ["Hidden Relic"]},
        "choices": {
            "listen": "The Adventurer shares vital information about the relic.",
            "ignore": "You leave without further interaction."
        }
    }
}

def initialize_quests():
    """
    Sets up available quests and their objectives
    """
    return quests_aq

def accept_quest(quest_name, character):
    """
    Adds a quest to the character's active quest
    """
    if 'quests' not in character:
        character['quests'] = {}
    if quest_name not in character['quests']:
        character['quests'][quest_name] = {'status': "In Progress"}
        print(f"Quest '{quest_name}' has been added to your quest log.")
    else:
        print(f"'{quest_name}' is already part of your quest log.")

def complete_quest(quest_name, character):
    """
    Updates quest status to completed and applies rewards
    """
    character['quests'][quest_name]['status'] = "Completed"
    for item, reward in quests_aq[quest_name]['reward'].items():
        if item == 'gold':
            character['gold'] += reward
        else:
            character['inventory'].extend(reward)

def check_quest_progress(character):
    """
    Displays the status of active quests
    """
    if 'quests' not in character or not character['quests']:
        print(f"You have no active quests.")
    for quest, info in character['quests'].items():
        print(f"- {quest} : {info['status']}")

def quest_interaction(location, character):
    """
    Triggers quests or objectives based on player's location
    """
    quest_info: dict = quests_aq.get(location, {})
    if quest_info:
        pass
        
    else:
        return