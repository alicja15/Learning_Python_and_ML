from typing import Tuple, TYPE_CHECKING
from organism import Organism

if TYPE_CHECKING:
    from world import World

class Animal(Organism):
    """Base class for all moving animals with metabolism (hunger and thirst)."""

    def __init__(self, energy: int, age: int, position: Tuple[int, int], world: "World", 
                 max_hunger: int = 10, max_thirst: int = 10) -> None:
        """Initializes animal stats, setting hunger and thirst to their maximum values."""
        super().__init__(energy, age, position, world)
        self.max_hunger: int = max_hunger
        self.max_thirst: int = max_thirst
        self.hunger: int = max_hunger  
        self.thirst: int = max_thirst  

    def move(self, target: Tuple[int, int]) -> None:
        """Moves the animal one step closer to the target coordinates and consumes 1 energy."""
        x, y = self.position
        tx, ty = target

        dx = 1 if tx > x else (-1 if tx < x else 0)
        dy = 1 if ty > y else (-1 if ty < y else 0)
        new_pos = (x + dx, y + dy)

        if self.world._is_within_bounds(new_pos):
            self.position = new_pos
            self.energy -= 1

    def _check_death_conditions(self) -> bool:
        """Private method: Checks if the animal meets any criteria for death. Returns True if dead."""
        if self.energy <= 0:
            self.decease("lack of energy")
            return True
        if self.hunger <= 0:
            self.decease("starvation")
            return True
        if self.thirst <= 0:
            self.decease("thirst")
            return True
        if self.age >= 30:
            self.decease("old age")
            return True
        return False

    def _determine_priority(self) -> Tuple[bool, bool]:
        """Private method: Evaluates hunger and thirst levels to determine the primary vital need (water or food)."""
        is_hungry: bool = self.hunger <= 6
        is_thirsty: bool = self.thirst <= 6
        priority_water: bool = False
        priority_hunger: bool = False

        if is_hungry or is_thirsty:
            if is_hungry and is_thirsty:
                # Choose whichever stat is closer to zero (higher danger of death)
                if self.thirst <= self.hunger:
                    priority_water = True
                else:
                    priority_hunger = True
            elif is_thirsty:
                priority_water = True
            else:
                priority_hunger = True

        return priority_water, priority_hunger