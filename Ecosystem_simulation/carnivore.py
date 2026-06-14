from typing import Tuple, TYPE_CHECKING
from animal import Animal
from herbivore import Herbivore

if TYPE_CHECKING:
    from world import World
    from organism import Organism

class Carnivore(Animal):
    """Represents a predatory animal that hunts Herbivores."""

    def act(self) -> None:
        """Executes the carnivore's turn logic. Loses energy faster than herbivores."""
        self.age += 1
        self.hunger -= 1
        self.thirst -= 1
        self.energy -= 2  

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
                    self.world.log(f"[Carnivore] at {self.position} drank water.")
                else:
                    self.move(water_pos)
                return

        # HUNGER PRIORITY
        if priority_hunger:
            target = self.world._find_nearest_organism(self.position, Herbivore)
            if target:
                if self.world._distance(self.position, target.position) <= 1:
                    self.move(target.position)
                    self.interact(target)
                else:
                    self.move(target.position)
                return

        # BREED PRIORITY
        if self.energy > 15:
            partner = self.world._find_nearest_organism(self.position, Carnivore)
            if partner and partner != self and partner.energy > 15:
                if self.world._distance(self.position, partner.position) <= 1:
                    self.interact(partner)
                else:
                    self.move(partner.position)
                return

    def interact(self, other: "Organism") -> None:
        """Handles interactions: attacks Herbivores or breeds with other Carnivores."""
        if isinstance(other, Herbivore):
            self.hunger = self.max_hunger
            self.energy += 12
            self.world.log(f"[Carnivore] at {self.position} attacked and ate Herbivore.")
            other.decease("attacked by Carnivore")
        elif isinstance(other, Carnivore):
            self.energy -= 8
            other.energy -= 8
            child = Carnivore(energy=12, age=0, position=self.position, world=self.world)
            self.world.add_organism(child)
            self.world.log(f"[Carnivore] bred with partner at {self.position}. New predator born!")