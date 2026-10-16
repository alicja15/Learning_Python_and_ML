import math
from typing import List, Tuple, Type, Optional
from organism import Organism
from plant import Plant
from herbivore import Herbivore
from carnivore import Carnivore

class World:
    """Manages the simulation grid, timeline ticks, logging, and organism lists."""

    def __init__(self, width: int = 6, height: int = 6) -> None:
        """Initializes the world grid dimensions, organism queues, and log file."""
        self.width: int = width
        self.height: int = height
        self.organisms: List[Organism] = []
        self.water_sources: List[Tuple[int, int]] = []
        self.log_file: str = "simulation_events.txt"
        
        with open(self.log_file, "w", encoding="utf-8") as file:
            file.write("=== SIMULATION START ===\n")

    def log(self, message: str) -> None:
        """Prints a message to the console and appends it to the log file."""
        print(message)
        with open(self.log_file, "a", encoding="utf-8") as file:
            file.write(message + "\n")

    def tick(self) -> None:
        """Advances the simulation by one turn, allowing each organism to take an action."""
        for organism in list(self.organisms):
            if organism.is_alive:
                organism.act()

    def remove_organism(self, organism: Organism) -> None:
        """Removes a dead organism from the simulation tracking list."""
        if organism in self.organisms:
            self.organisms.remove(organism)

    def add_organism(self, organism: Organism) -> None:
        """Adds a new organism to the simulation tracking list."""
        self.organisms.append(organism)

    def print_statistics(self) -> None:
        """Counts and prints the current population of each species."""
        plants = sum(1 for o in self.organisms if isinstance(o, Plant))
        herbivores = sum(1 for o in self.organisms if isinstance(o, Herbivore))
        carnivores = sum(1 for o in self.organisms if isinstance(o, Carnivore))
        print(f"Current organisms alive: Plants: {plants}, Herbivores: {herbivores}, Carnivores: {carnivores}")

    # PRIVATE READ-ONLY / UTILITY METHODS
    def _is_water(self, pos: Tuple[int, int]) -> bool:
        """Private method: Checks if the specified position is a water tile."""
        return pos in self.water_sources

    def _is_within_bounds(self, pos: Tuple[int, int]) -> bool:
        """Private method: Checks if the specified position is within the grid boundaries."""
        return 0 <= pos[0] < self.width and 0 <= pos[1] < self.height

    def _distance(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> float:
        """Private method: Calculates the Euclidean distance between two points."""
        return math.hypot(pos1[0] - pos2[0], pos1[1] - pos2[1])

    def _find_nearest_water(self, pos: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        """Private method: Finds the closest water source coordinates relative to a position."""
        if not self.water_sources:
            return None
        return min(self.water_sources, key=lambda w_pos: self._distance(pos, w_pos))

    def _find_nearest_organism(self, pos: Tuple[int, int], organism_type: Type[Organism]) -> Optional[Organism]:
        """Private method: Finds the closest living organism of a specific type."""
        valid_targets = [org for org in self.organisms if isinstance(org, organism_type) and org.is_alive]
        if not valid_targets:
            return None
        return min(valid_targets, key=lambda org: self._distance(pos, org.position))