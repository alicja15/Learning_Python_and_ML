import os
import csv
from character import Character, Warrior, Mage, Archer

SAVE_FILE = "rpg_save.csv"

def save_game(player: Character) -> None:
    """Serializes the player's core stats to a CSV file."""
    with open(SAVE_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            player.__class__.__name__,
            player.name,
            player.level,
            player.xp,
            player.hp,
            player.base_attack,
            player.base_defense,
        ])
    print("Game saved successfully!")

def load_game() -> Character | None:
    """Deserializes player data from a CSV file to recreate the Character object."""
    if not os.path.exists(SAVE_FILE):
        return None

    try:
        with open(SAVE_FILE, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            data = next(reader)

            cls_name, name, level, xp, hp, base_attack, base_defense = data

            # Instantiate the correct class type
            if cls_name == "Warrior":
                player = Warrior(name)
            elif cls_name == "Mage":
                player = Mage(name)
            elif cls_name == "Archer":
                player = Archer(name)
            else:
                return None

            # Restore previous statistics
            player.level = int(level)
            player.xp = int(xp)
            player.hp = int(hp)
            player.base_attack = int(base_attack)
            player.base_defense = int(base_defense)
            player.xp_to_next_level = int(100 * (1.5 ** (player.level - 1)))

            return player
    except Exception as e:
        print(f"Oops.. something went wrong, unable to open save file. Error: {e}")
        return None