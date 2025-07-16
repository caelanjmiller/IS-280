import os

character: dict = {}

items_at_location = {
    (0, 1): ["Health Potion", "Magic Scroll"],
    (0, 3): ["Shield", "Ancient Scroll"],
    (0, 4): ["Ancient Relic", "Enchanted Sword", "Health Potion"],
    (1, 0): ["Ancient Scroll", "Magic Scroll", "Shield", "Old Sword"],
    (1, 1): ["Ancient Relic", "Enchanted Sword"],
    (1, 3): ["Water", "Water", "Water"],
    (2, 0): ["Water", "Water", "Water"],
    (2, 2): ["Enchanted Amulet", "Emulated Sword"],
    (2, 4): ["Old Sword", "Magic Scroll", "Ancient Relic", "Health Potion"],
    (3, 0): ["Water", "Food", "Enchanted Amulet"],
    (3, 2): ["Old Sword", "Food", "Old Sword"],
    (3, 4): ["Ancient Relic", "Shield", "Old Sword"],
    (4, 0): ["Food", "Magic Scroll"],
    (4, 2): ["Ancient Scroll", "Enchanted Sword", "Magic Scroll", "Enchanted Amulet"],
    (4, 3): ["Water", "Shield", "Old Sword"],
    (4, 4): ["Food", "Health Potion"]
}

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


def save_game(character, location_items, filename="players.txt"):
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

def load_game(character, filename="players.txt"):
    pass

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def createCharacter():
    print("Create your Character!\n")
    character_name: str = input("Enter your character's name: ")
    character_health: int = 100
    character_strength: int = 10
    global character
    character = {
            'name': character_name,
            'health': character_health,
            'strength': character_strength,
            'level': 1,
            'gold': 0,
            'inventory': ['Food', 'Water'],
            'magic': 0,
            'location': (0,0)
        }
    print(f"Character created! Name: {character['name']}, Health: {character['health']}, Strength: {character['strength']}\n")
    clearScreen()
    playGame()

def playGame():
    isPlaying: bool = True
    global character
    narrative = (
        f"Welcome, {character['name']}! You stand at the edge of the Uncharted Territory, where danger and "
        "opportunity lurk at every turn. Your journey to the Enchanted Castle begins here. "
        "To the east lies an Abandoned Village shrouded in mystery, and to the south, a "
        "Haunted Forest beckons with eerie silence."
    )
    print(narrative)
    print("Press Enter to Begin!")
    input()
    while isPlaying:
        print("=" * 80)
        print(f"{'Adventure Quest':^80}")
        x,y = character['location']
        current_coordinates = character['location']
        current_location = game_map[current_coordinates]
        print(f"{'Location: ' + current_location + ' ' + str(current_coordinates):^80}")        
        print("=" * 80)

        print(f"| Name: {character['name']:<15} Health: {character['health']:<15} Strength: {character['strength']:<25}|")
        print(f"| Level: {character['level']:<14} Gold: {character['gold']:<17} Magic: {character['magic']:<24} |")
        print("=" * 80)

        available_commands = [
            'Move: north (n), south (s), east (e), west (w)',
            'Actions: inspect (c), talk (t)',
            'Item Actions - add [item_name]: pick up (p), drop (d), use (u)',
            'View Inventory (i)',
            'View Map (m)',
            'Quit (q)'
        ]

        print("=" * 80)
        print(f"{'Adventure Quest':^80}")
        print("=" * 80)
        print("| Available Commands:".ljust(80) + "|")
        for command in available_commands:
            print(f"| - {command:<75} |")
        print("=" * 80)

        player_command: str = input("\nEnter your command: ")

        if player_command == "q":
            print("Thank you for playing Adventure Quest!")
            isPlaying: bool = False
    
        if player_command == 'n': 
            if x > 0:
                x -= 1
            else:
                print("You cannot move further north.")
        
        elif player_command == 'e':
            if y < 4:
                y += 1
            else:
                print("You cannot move further east.")
        
        elif player_command == 's':
            if x < 4:
                x += 1
            else:
                print("You cannot move further south.")

        elif player_command == 'w':
            if y > 0:
                y -= 1
            else:
                print("You cannot move further west.")

        elif player_command == 'i':
            print("=" * 80)
            print(f"{'Inventory':^80}")
            print("=" * 80)
            print("You are carrying:")
            for item in character['inventory']:
                print(f"- {item}")
            print("=" * 80)
            continue
        
        elif player_command == 'm':
            print("=" * 80)
            print(f"{'Adventure Quest - Game Map':^80}")
            print("=" * 80)
            print("| Coordinates | Location Name        |")
            print("|-------------|----------------------|")
            for coord, location in game_map.items():
                coordinates_str = f"({coord[0]}, {coord[1]})"
                print(f"| {coordinates_str:<11} | {location:<20} |")
            print("=" * 80)
            continue
        
        elif player_command.startswith('u '):
            item_used = player_command[2:].strip()
            if item_used in character["inventory"]:
                if item_used == "Health Potion":
                    character['health'] += 20
                    print("You used the Health Potion and gained 20 health points!")
        
                elif item_used == "Magic Scroll":
                    character['magic'] += 10
                    print("You used the Magic Scroll and gained 10 magic points!")

                elif item_used == "Food":
                    print("You ate the food.")

                elif item_used == "Water":
                    print("You drank the water.")

                elif item_used == "Shield":
                    character['strength'] += 5
                    print("You used the shield and your strength increased by 5!")

                elif item_used == "Old Sword":
                    character['strength'] += 10
                    print("Old Sword has no effect outside of combat!")

                elif item_used == "Enchanted Amulet":
                    character['health'] += 5
                    character['magic'] += 5
                    print("You used the Enchanted Amulet and gained 5 health points and 5 magic points!")

                elif item_used == "Ancient Scroll":
                    character['level'] += 1
                    print("You used the Ancient Scroll and your level increased by 1!")

                elif item_used == "Gold Coin":
                    print("You used the gold coin!")

                elif item_used == "Enchanted Sword":
                    character['strength'] += 15
                    print("You used the Enchanted Sword and your strength increased by 15!")

                elif item_used == "Ancient Relic":
                    print("You used the Ancient Relic and revealed a hidden path!")

                character['inventory'].remove(item_used)

            else:
                print(f"You don't have {item_used} in your inventory.")

        elif player_command.startswith('p '):
            item_picked = player_command[2:].strip()
            if item_picked in items_at_location.get((x, y), []):
                character['inventory'].append(item_picked)
                items_at_location[(x, y)].remove(item_picked)
                print(f"You picked up {item_picked}.")

        elif player_command.startswith('d '):
            item_dropped = player_command[2:].strip()
            if item_dropped in character['inventory']:
                items_at_location[(x, y)].append(item_dropped)
                print(f"You dropped {item_dropped}.")
        
        elif player_command == 'c':
            items_at_current_location = items_at_location.get(character['location'], [])
            print(f"You look around and find the following items:")
            for item in items_at_current_location:
                print(f"- {item}")
           
        else:
            print("Invalid command. Please try again.")
        
        character['location'] = (x,y)


print("=" * 80)
print(f"{'Adventure Quest':^80}")
print("=" * 80)
print(f"""Welcome to Adventure Quest!

In this mystical land, you will embark on a thrilling journey to find the Enchanted
Castle, rescue allies, and rebuild communities. Along the way, you will encounter 
various challenges, meet different characters, and collect valuable resources.
Good luck on your adventure!
""")
print("=" * 80)

print("| Main Menu:".ljust(80) + "|")
print("| 1. Start New Game".ljust(80) + "|")
print("| 2. Load Game".ljust(80) + "|")
print("| 3. Quit".ljust(80) + "|")
print("=" * 80)

menu_choice = input("Please select an option: ")
print("=" * 80)
print(f"{'Adventure Quest':^80}")
print("=" * 80)

if menu_choice == '1':
    createCharacter()

elif menu_choice == '2':
    print("Load a Saved Game!\n")
    character_name = input("Enter your character's name: ")
    load_game(character_name)
    if character['name'] == character_name:
            print(f"Welcome back, {character['name']}! Let's begin where you left off.")
            playGame()
    else:
        print("Failed to load the game. Starting a new game...")
        createCharacter()

elif menu_choice == '3':
    print("Thank you for playing Adventure Quest!")

else:
    print("Invalid option. Please try again.")