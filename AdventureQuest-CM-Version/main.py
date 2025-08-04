from utilities.character import *
from utilities.quests import *
from utilities.quests import *
from utilities.challenges import *
from utilities.combat import *
from utilities.npcs import *
from utilities.save_load import *
from utilities.locations import *

game_map, items_at_location = locations.initialize_map()
npcs_aq = npcs.initialize_npcs()
player_quests = quests.initialize_quests()

def playGame():
    game_running: bool = True
    narrative = (
        f"Welcome, {player.name}! You stand at the edge of the Uncharted Territory, where danger and "
        "opportunity lurk at every turn. Your journey to the Enchanted Castle begins here. "
        "To the east lies an Abandoned Village shrouded in mystery, and to the south, a "
        "Haunted Forest beckons with eerie silence."
    )
    wrapped_text(narrative)
    clearScreen()
    while game_running:
        print("=" * 80)
        print(f"{'Adventure Quest':^80}")
        current_coordinates = player.location
        current_location = game_map[current_coordinates]['name']
        print(f"{'Location: ' + current_location + ' ' + str(current_coordinates):^80}")        
        print("=" * 80)

        print(f"| Name: {player.name:<16} Health: {player.health:<14} Strength: {player.strength:<20} |")
        print(f"| Level: {player.level:<15} Gold: {player.gold:<16} Magic: {player.magic:<23} |")
        print("=" * 80)

        available_commands = [
            'Move: north (n), south (s), east (e), west (w)',
            'Actions: inspect (c), talk (t)',
            'Item Actions: pick up (p), drop (d), use (u)',
            'View Inventory (i)',
            'View Map (m)',
            'View Quest(s) Progress (r)',
            'Quit (q)'
        ]

        print("| Available Commands:".ljust(80) + "|")
        for command in available_commands:
            print(f"| - {command:<75} |")
        print("=" * 80)

        wrapped_text(game_map[current_coordinates]['description'])
        print()
        
        if current_coordinates in npcs_aq:
            npc_interaction: str = npcs_aq[current_coordinates]['interaction']
            wrapped_text(npc_interaction)
            wrapped_text(f"Press 't' to speak with them.")

        player_command: str = input("\nEnter your command: ")
    
        if player_command == 'n':
            locations.move_character('n', player)
        
        elif player_command == 'w':
            locations.move_character('w', player)

        elif player_command == 'e':
            locations.move_character('e', player)

        elif player_command == 's':
            locations.move_character('s', player)

        elif player_command == 'i':
            player.view_inventory()
            
        elif player_command == 'm':
            locations.display_map(player)
        
        elif player_command.startswith('u '):
            item_used = player_command[2:].strip()
            items.use_item(player, item_used)

        elif player_command.startswith('p '):
            item_picked = player_command[2:].strip()
            items.pick_up_item(player, items_at_location, item_picked)

        elif player_command.startswith('d '):
            item_dropped = player_command[2:].strip()
            items.drop_item(player, items_at_location, item_dropped)

        elif player_command == 'c':
            locations.inspect_location(player, items_at_location)
           
        elif player_command == 'q':
            print("Thank you for playing Adventure Quest!")
            save_game(player, items_at_location)
            game_running: bool = False

        elif player_command == 't':
            npcs.interact_with_npc(player, current_coordinates)

        
        elif player_command == 'r':
            quests.check_quest_progress(player)
            print()

        else:
            print("Invalid command. Please try again.")

        clearScreen()



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
    player: Character = create_character()
    playGame()

# Come back to this section after fixing load
elif menu_choice == '2':
    print("Load a Saved Game!\n")
    player_name = wrapped_text_prompt("Enter your character's name", "; ")
    player: Character = Save.load_game(player_name)
    if player.name == player_name:
            print(f"Welcome back, {player.name}! Let's begin where you left off.")
            playGame()
    else:
        print("Failed to load the game. Starting a new game...")
        create_character()
        playGame()

elif menu_choice == '3':
    print("Thank you for playing Adventure Quest!")

else:
    print("Invalid option. Please try again.")