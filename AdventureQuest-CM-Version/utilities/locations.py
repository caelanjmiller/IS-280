"""
Module aims to :
1. Initialize and define locations within Adventure Quest
2. Enable display of game map
3. Enable character movement within appropriate bounds
4. Inspect items present at a given location
"""

game_map = {
    (0, 0): {
        "name": "Uncharted Territory",
        "description": "Uncharted territory is filled with wild, untamed lands with no clear paths or landmarks. Thick vegetation, jagged rocks, and strange sounds make it a perilous place to navigate. What lies within is a mystery to all."
    },
    (0, 1): {
        "name": "Abandoned Village",
        "description": "These abandoned villages are eerily quiet, with crumbling huts and overgrown pathways. Broken tools and forgotten belongings hint at the lives once lived here. Shadows dance along the walls, hinting at hidden dangers."
    },
    (0, 2): {
        "name": "Uncharted Territory",
        "description": "Uncharted territory is filled with wild, untamed lands with no clear paths or landmarks. Thick vegetation, jagged rocks, and strange sounds make it a perilous place to navigate. What lies within is a mystery to all."
    },
    (0, 3): {
        "name": "Haunted Forest",
        "description": "Twisted trees with gnarled roots form a labyrinth of shadows. Faint whispers echo through the air, and an eerie mist clings to the ground. Travelers speak of spirits that haunt these woods, guarding their secrets."
    },
    (0, 4): {
        "name": "Mystical City",
        "description": "Bustling with life, these cities are filled with magical markets, floating lights, and enchanting melodies. Strange merchants offer mysterious wares, and rumors of great treasures abound."
    },
    (1, 0): {
        "name": "Abandoned Village",
        "description": "These abandoned villages are eerily quiet, with crumbling huts and overgrown pathways. Broken tools and forgotten belongings hint at the lives once lived here. Shadows dance along the walls, hinting at hidden dangers."
    },
    (1, 1): {
        "name": "Ancient Ruins",
        "description": "The ancient ruins are towering stone pillars and crumbling walls that rise out of the earth, covered in vines and moss. Strange carvings line the stones, whispering secrets of a lost civilization. A faint glow emanates from deep within."
    },
    (1, 2): {
        "name": "Uncharted Territory",
        "description": "Uncharted territory is filled with wild, untamed lands with no clear paths or landmarks. Thick vegetation, jagged rocks, and strange sounds make it a perilous place to navigate. What lies within is a mystery to all."
    },
    (1, 3): {
        "name": "Magical Springs",
        "description": "Magical Springs are crystal-clear water pools surrounded by vibrant, glowing plants. The sound of gently flowing water is soothing, and the air feels rejuvenating. It is said these springs possess healing properties."
    },
    (1, 4): {
        "name": "Uncharted Territory",
        "description": "Uncharted territory is filled with wild, untamed lands with no clear paths or landmarks. Thick vegetation, jagged rocks, and strange sounds make it a perilous place to navigate. What lies within is a mystery to all."
    },
    (2, 0): {
        "name": "Magical Springs",
        "description": "Magical Springs are crystal-clear water pools surrounded by vibrant, glowing plants. The sound of gently flowing water is soothing, and the air feels rejuvenating. It is said these springs possess healing properties."
    },
    (2, 1): {
        "name": "Uncharted Territory",
        "description": "Uncharted territory is filled with wild, untamed lands with no clear paths or landmarks. Thick vegetation, jagged rocks, and strange sounds make it a perilous place to navigate. What lies within is a mystery to all."
    },
    (2, 2): {
        "name": "Enchanted Castle",
        "description": "The Enchanted Castle is a grand structure with towering spires shimmering in the moonlight. The air is thick with magic, and the walls hum with ancient power. Legends speak of a powerful artifact hidden deep within its chambers."
    },
    (2, 3): {
        "name": "Uncharted Territory",
        "description": "Uncharted territory is filled with wild, untamed lands with no clear paths or landmarks. Thick vegetation, jagged rocks, and strange sounds make it a perilous place to navigate. What lies within is a mystery to all."
    },
    (2, 4): {
        "name": "Forest Camp",
        "description": "Small clearings in the woods, with campfires still smoldering and simple tents pitched. Adventurers and wanderers often use these camps as rest stops. The smell of cooked food lingers in the air."
    },
    (3, 0): {
        "name": "Mystical City",
        "description": "Bustling with life, these cities are filled with magical markets, floating lights, and enchanting melodies. Strange merchants offer mysterious wares, and rumors of great treasures abound."
    },
    (3, 1): {
        "name": "Uncharted Territory",
        "description": "Uncharted territory is filled with wild, untamed lands with no clear paths or landmarks. Thick vegetation, jagged rocks, and strange sounds make it a perilous place to navigate. What lies within is a mystery to all."
    },
    (3, 2): {
        "name": "Mystical City",
        "description": "Bustling with life, these cities are filled with magical markets, floating lights, and enchanting melodies. Strange merchants offer mysterious wares, and rumors of great treasures abound."
    },
    (3, 3): {
        "name": "Uncharted Territory",
        "description": "Uncharted territory is filled with wild, untamed lands with no clear paths or landmarks. Thick vegetation, jagged rocks, and strange sounds make it a perilous place to navigate. What lies within is a mystery to all."
    },
    (3, 4): {
        "name": "Ancient Ruins",
        "description": "The ancient ruins are towering stone pillars and crumbling walls that rise out of the earth, covered in vines and moss. Strange carvings line the stones, whispering secrets of a lost civilization. A faint glow emanates from deep within."
    },
    (4, 0): {
        "name": "Haunted Forest",
        "description": "Twisted trees with gnarled roots form a labyrinth of shadows. Faint whispers echo through the air, and an eerie mist clings to the ground. Travelers speak of spirits that haunt these woods, guarding their secrets."
    },
    (4, 1): {
        "name": "Uncharted Territory",
        "description": "Uncharted territory is filled with wild, untamed lands with no clear paths or landmarks. Thick vegetation, jagged rocks, and strange sounds make it a perilous place to navigate. What lies within is a mystery to all."
    },
    (4, 2): {
        "name": "Forest Camp",
        "description": "Small clearings in the woods, with campfires still smoldering and simple tents pitched. Adventurers and wanderers often use these camps as rest stops. The smell of cooked food lingers in the air."
    },
    (4, 3): {
        "name": "Mystical City",
        "description": "Bustling with life, these cities are filled with magical markets, floating lights, and enchanting melodies. Strange merchants offer mysterious wares, and rumors of great treasures abound."
    },
    (4, 4): {
        "name": "Haunted Forest",
        "description": "Twisted trees with gnarled roots form a labyrinth of shadows. Faint whispers echo through the air, and an eerie mist clings to the ground. Travelers speak of spirits that haunt these woods, guarding their secrets."
    }
}


items_at_location = {
    (0, 1): ["Old Sword", "Health Potion"],
    (0, 3): ["Magic Scroll", "Gold Coin"],
    (0, 4): ["Gold Coin", "Ancient Relic"],
    (1, 0): ["Old Sword", "Health Potion"],
    (1, 1): ["Magic Scroll", "Gold Coin"],
    (1, 3): ["Health Potion", "Gold Coin"],
    (2, 0): ["Shield", "Health Potion"],
    (2, 2): ["Enchanted Amulet", "Enchanted Sword", "Ancient Scroll"],
    (2, 4): ["Ancient Relic", "Gold Coin"],
    (3, 0): ["Gold Coin", "Ancient Relic"],
    (3, 2): ["Enchanted Amulet", "Ancient Scroll", "Health Potion", "Gold Coin"],
    (3, 4): ["Ancient Relic", "Gold Coin"],
    (4, 0): ["Magic Scroll", "Gold Coin"],
    (4, 2): ["Enchanted Amulet", "Ancient Scroll", "Health Potion", "Gold Coin"],
    (4, 3): ["Health Potion", "Gold Coin"],
    (4, 4): ["Ancient Relic", "Gold Coin"]
        }

def initialize_map() -> tuple:
    """
    Sets up game map and initial items at each location
    """
    return game_map, items_at_location

def display_map(character: dict):
    """
    Prints the game map, showing the player's current location
    """
    current_coordinates = character['location']
    current_location = game_map[current_coordinates]['name']
    print(f"{'Location: ' + current_location + ' ' + str(current_coordinates):^80}")        
    print("=" * 80)
    print(f"| Name: {character['name']:<15} Health: {character['health']:<15} Strength: {character['strength']:<25}|")
    print(f"| Level: {character['level']:<14} Gold: {character['gold']:<17} Magic: {character['magic']:<24} |")
    print("=" * 80)
    print(f"{'Adventure Quest - Game Map':^80}")
    print("=" * 80)
    print("| Coordinates | Location Name        |")
    print("|-------------|----------------------|")
    for coord, location in game_map.items():
        coordinates_str = f"({coord[0]}, {coord[1]})"
        print(f"| {coordinates_str:<11} | {location:<20} |")
    print("=" * 80)

def move_character(direction: str, character: dict):
    """
    Updates the character's location based upon a movement command (n, s, e, w)
    Ensures valid movement within bounds
    """
    x,y = character['location']
    if direction == 'n': 
        if x > 0:
            x -= 1
        else:
            print("You cannot move further north.")
            
    elif direction == 'e':
        if y < 4:
            y += 1
        else:
            print("You cannot move further east.")
            
    elif direction == 's':
        if x < 4:
            x += 1
        else:
            print("You cannot move further south.")
            
    elif direction == 'w':
        if y > 0:
            y -= 1
        else:
            print("You cannot move further west.")       

    character['location'] = (x,y)

def inspect_location(character: dict, items_at_location: dict):
    """
    List items available at the character's current location
    """
    items_at_current_location = items_at_location.get(character['location'], [])
    if not items_at_current_location:
        print(f"There are no items at this location.")
    else:
        print(f"You look around and find the following items:")
        for item in items_at_current_location:
            print(f"- {item}")