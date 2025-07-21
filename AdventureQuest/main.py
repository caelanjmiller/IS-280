import os

from utilities import character as char
from utilities import locations, npcs, quests, items, save_load

game_map, items_at_location = locations.initialize_map()

def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def playGame():
    game_running: bool = True
    narrative = (
        f"Welcome, {character['name']}! You stand at the edge of the Uncharted Territory, where danger and "
        "opportunity lurk at every turn. Your journey to the Enchanted Castle begins here. "
        "To the east lies an Abandoned Village shrouded in mystery, and to the south, a "
        "Haunted Forest beckons with eerie silence."
    )
    print(narrative)
    print("Press Enter to Begin!")
    input()
    while game_running:
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
    
        if player_command == 'n':
            locations.move_character('n', character)
        
        elif player_command == 'w':
            locations.move_character('w', character)

        elif player_command == 'e':
            locations.move_character('e', character)

        elif player_command == 's':
            locations.move_character('s', character)

        elif player_command == 'i':
            char.view_inventory(character)
            continue
        
        elif player_command == 'm':
            locations.display_map(character)
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
            items.pick_up_item(character, items_at_location, item_picked)

        elif player_command.startswith('d '):
            item_dropped = player_command[2:].strip()
            items.drop_item(character, items_at_location, item_dropped)
        
        elif player_command == 'c':
            locations.inspect_location(character, items_at_location)
           
        elif player_command == 'q':
            print("Thank you for playing Adventure Quest!")
            save_load.save_game(character, items_at_location)
            game_running: bool = False

        else:
            print("Invalid command. Please try again.")

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
    character: dict = char.createCharacter()
    playGame()

elif menu_choice == '2':
    print("Load a Saved Game!\n")
    character_name = input("Enter your character's name: ")
    character: dict = save_load.load_game(character_name)
    if character['name'] == character_name:
            print(f"Welcome back, {character['name']}! Let's begin where you left off.")
            playGame()
    else:
        print("Failed to load the game. Starting a new game...")
        char.createCharacter()
        playGame()

elif menu_choice == '3':
    print("Thank you for playing Adventure Quest!")

else:
    print("Invalid option. Please try again.")