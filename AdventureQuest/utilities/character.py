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

