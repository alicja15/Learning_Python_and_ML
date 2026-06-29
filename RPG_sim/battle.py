import time
from character import Character
from enemy import Enemy

def battle_turn(player: Character, enemy: Enemy) -> bool:
    """Manages the turn-based combat sequence between a player and an enemy."""
    round_num = 1
    print(f"\nAn enemy enters: {enemy.name}")

    while player.is_alive() and enemy.is_alive():
        print(f"\n--- Turn {round_num} ---")
        print(f"Player: {player.hp}/{player.max_hp} HP | Enemy: {enemy.hp}/{enemy.max_hp} HP")

        print("Choose an action:")
        print("1. Regular attack")
        print("2. Special attack")
        choice = input("> ")

        if choice == "1":
            player.regular_attack(enemy)
        elif choice == "2":
            player.special_ability(enemy)
        else:
            print(f"{player.name} doesn't know what to do!! Your turn has passed.")

        time.sleep(1)

        # Enemy's turn
        if enemy.is_alive():
            enemy.enemy_ai_turn(player)
            time.sleep(1)

        round_num += 1

    if player.is_alive():
        print(f"\n{enemy.name} has been slain!")
        player.gain_xp(enemy.xp_reward)
        return True
    else:
        print("\nYou have been slain...")
        return False