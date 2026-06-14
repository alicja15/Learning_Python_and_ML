import random
from world import World
from plant import Plant
from herbivore import Herbivore
from carnivore import Carnivore

class Desert(World):
    """Harsh biome with limited water and scarce vegetation."""

    def __init__(self) -> None:
        """Initializes a 6x6 desert with one central oasis and sparse life."""
        super().__init__(width=6, height=6)
        self.water_sources = [(0, 0)]
        
        self.add_organism(Plant(5, 0, (1, 1), self))
        self.add_organism(Herbivore(12, 0, (2, 2), self))
        self.add_organism(Carnivore(20, 0, (5, 5), self))


class Forest(World):
    """Resource-rich biome with plenty of water and vegetation."""

    def __init__(self) -> None:
        """Initializes an 8x8 forest with a river flow and randomly scattered plants."""
        super().__init__(width=8, height=8)
        self.water_sources = [(2, 2), (2, 3), (2, 4)]  # River
        
        for _ in range(6):
            rx = random.randint(0, 7)
            ry = random.randint(0, 7)
            if (rx, ry) not in self.water_sources:
                self.add_organism(Plant(5, 0, (rx, ry), self))

        self.add_organism(Herbivore(15, 0, (1, 1), self))
        self.add_organism(Herbivore(15, 0, (5, 6), self))
        self.add_organism(Carnivore(25, 0, (7, 7), self))