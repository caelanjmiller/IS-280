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
    isPlaying: bool = True
    print("Create your Character!\n")
    character_name: str = input("Enter your character's name: ")
    character_health: int = 100
    character_strength: int = 10
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

        available_commands: list = [
            "Move: north (n), south (s), east (e), west (w)",
            "Actions: pick up (p), drop (d), use (u), talk (t)",
            "Inventory: view inventory (i)",
            "View Map (m)",
            "Save Game (z), Load Game (l), Quit (q)"
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
        
        elif player_command == 'p':
            print("This feature is under construction.")
        
        else:
            print("Invalid command. Please try again.")
        
        character['location'] = (x,y)

elif menu_choice == '2':
    print("Load game option is under construction.")
elif menu_choice == '3':
    print("Thank you for playing Adventure Quest!")
else:
    print("Invalid option. Please try again.")