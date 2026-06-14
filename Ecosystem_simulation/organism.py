from abc import ABC, abstractmethod
from typing import Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from world import World

class Organism(ABC):
    """Abstract base class representing any living organism in the simulation."""

    def __init__(self, energy: int, age: int, position: Tuple[int, int], world: "World") -> None:
        """Initializes core organism attributes."""
        self.energy: int = energy
        self.age: int = age
        self.position: Tuple[int, int] = position
        self.world: "World" = world
        self.is_alive: bool = True

    @abstractmethod
    def act(self) -> None:
        """Abstract method defining the organism's behavior during a simulation tick."""
        pass

    @abstractmethod
    def interact(self, other: "Organism") -> None:
        """Abstract method defining interactions with another organism."""
        pass

    def decease(self, reason: str) -> None:
        """Handles the death of the organism, removes it from the world, and logs the event."""
        self.is_alive = False
        self.world.remove_organism(self)
        self.world.log(f"[{type(self).__name__}] at {self.position} died of {reason}.")