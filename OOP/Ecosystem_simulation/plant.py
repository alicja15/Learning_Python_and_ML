import random
from typing import Tuple, TYPE_CHECKING
from organism import Organism

if TYPE_CHECKING:
    from world import World

class Plant(Organism):
    """Represents a stationary plant that generates energy from photosynthesis and spreads."""

    def act(self) -> None:
        """Increases age and energy passively. Has a chance to reproduce on adjacent tiles."""
        self.age += 1
        self.energy += 1  # Passive energy from photosynthesis

        # Chance to reproduce
        if self.energy > 12 and random.random() < 0.10:
            x, y = self.position
            new_pos: Tuple[int, int] = (x + random.choice([-1, 0, 1]), y + random.choice([-1, 0, 1]))
            if self.world._is_within_bounds(new_pos) and not self.world._is_water(new_pos):
                child = Plant(energy=4, age=0, position=new_pos, world=self.world)
                self.world.add_organism(child)

    def interact(self, other: "Organism") -> None:
        """Plants do not actively initiate interactions."""
        pass