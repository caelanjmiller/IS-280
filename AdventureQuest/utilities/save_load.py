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