from typing import Tuple, TYPE_CHECKING
from animal import Animal
from plant import Plant

if TYPE_CHECKING:
    from world import World
    from organism import Organism

class Herbivore(Animal):
    """Represents a herbivorous animal that eats plants."""

    def act(self) -> None:
        """Executes the herbivore's turn logic based on survival priorities (water > food > breeding)."""
        self.age += 1
        self.hunger -= 1
        self.thirst -= 1
        self.energy -= 1

        if self._check_death_conditions():
            return

        # Using the inherited priority logic
        priority_water, priority_hunger = self._determine_priority()

        # WATER PRIORITY
        if priority_water:
            water_pos = self.world._find_nearest_water(self.position)
            if water_pos:
                if self.position == water_pos:
                    self.thirst = self.max_thirst
                    self.energy += 2
                    self.world.log(f"[Herbivore] at {self.position} drank water.")
                else:
                    self.move(water_pos)
                return

        # HUNGER PRIORITY
        if priority_hunger:
            nearest_plant = self.world._find_nearest_organism(self.position, Plant)
            if nearest_plant and isinstance(nearest_plant, Plant):
                if self.world._distance(self.position, nearest_plant.position) <= 1:
                    self.move(nearest_plant.position)
                    self.interact(nearest_plant)
                else:
                    self.move(nearest_plant.position)
                return

        # BREED PRIORITY
        if self.energy > 15:
            partner = self.world._find_nearest_organism(self.position, Herbivore)
            if partner and partner != self and partner.energy > 15:
                if self.world._distance(self.position, partner.position) <= 1:
                    self.interact(partner)
                else:
                    self.move(partner.position)
                return

    def interact(self, other: "Organism") -> None:
        """Handles interactions: eats Plants or breeds with other Herbivores."""
        if isinstance(other, Plant):
            self.energy += other.energy
            self.world.log(f"[Herbivore] at {self.position} ate a Plant.")
            other.decease("being eaten by Herbivore")
        elif isinstance(other, Herbivore):
            self.energy -= 7
            other.energy -= 7
            child = Herbivore(energy=10, age=0, position=self.position, world=self.world)
            self.world.add_organism(child)
            self.world.log(f"[Herbivore] bred with partner at {self.position}. New offspring born!")