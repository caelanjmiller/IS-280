"""
Module aims to :
1. Initialize and define locations within Adventure Quest
2. Enable display of game map
3. Enable character movement within appropriate bounds
4. Inspect items present at a given location
"""

game_map: dict = {
     (0,0): "Uncharted Territory",
     (0,1): "Abandoned Village",
     (0,2): "Uncharted Territory",
     (0,3): "Haunted Forest",
     (0,4): "Mystical City",
     (1,0): "Abandoned Village",
     (1,1): "Ancient Ruins",
     (1,2): "Uncharted Territory",
     (1,3): "Magical Springs",
     (1,4): "Uncharted Territory",
     (2,0): "Magical Springs",
     (2,1): "Uncharted Territory",
     (2,2): "Enchanted Castle",
     (2,3): "Uncharted Territory",
     (2,4): "Forest Camp",
     (3,0): "Mystical City",
     (3,1): "Uncharted Territory",
     (3,2): "Mystical City",
     (3,3): "Uncharted Territory",
     (3,4): "Ancient Ruins",
     (4,0): "Haunted Forest",
     (4,1): "Uncharted Territory",
     (4,2): "Forest Camp",
     (4,3): "Mystical City",
     (4,4): "Haunted Forest",
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
    current_location = game_map[current_coordinates]
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