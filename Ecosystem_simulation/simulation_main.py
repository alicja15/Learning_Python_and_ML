import time
from biomes import Forest, Desert
from world import World

def run_simulation() -> None:
    """Handles user setup and executes the core simulation loop for a chosen biome."""
    print("Choose simulation biome:")
    print("1. Forest - Lots of resources")
    print("2. Desert - Harsh environment")
    biome_choice: str = input().strip()
    
    print("How many turns should the simulation have? Please enter a positive integer:")
    try:
        ticks_num: int = int(input())
    except ValueError:
        print("Invalid input. Defaulting to 10 turns.")
        ticks_num = 10

    world: World = Forest() if biome_choice == "1" else Desert()
    
    if biome_choice == "1":
        print("\n--- Starting Forest biome simulation ---")
    else:
        print("\n--- Starting Desert biome simulation ---")

    for tick_num in range(1, ticks_num + 1):
        world.log(f"\n==================== TURN {tick_num} ====================")
        world.tick()
        world.print_statistics()
        time.sleep(1)

if __name__ == "__main__":
    run_simulation()