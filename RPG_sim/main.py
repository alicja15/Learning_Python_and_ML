from character import Warrior
from enemy import Goblin
from battle import battle_turn
from save_system import save_game, load_game

def main() -> None:
    """Main execution block of the RPG game."""
    print("Welcome to the Python RPG!")
    
    # Attempt to load a saved game
    player = load_game()
    
    if player is None:
        print("Starting a new adventure...")
        player_name = input("Enter your hero's name: ")
        player = Warrior(player_name) 
    else:
        print(f"Welcome back, {player.name} (Level {player.level})!")

    # Example Battle
    enemy = Goblin()
    victory = battle_turn(player, enemy)

    # Save game conditionally upon surviving
    if victory:
        print("Saving your progress...")
        save_game(player)

if __name__ == "__main__":
    main()