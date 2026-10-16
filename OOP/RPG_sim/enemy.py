from character import Character
import random

class Enemy(Character):
    """Base class representing hostile entities in the game."""
    
    def __init__(self, name: str, hp: int, attack_power: int, defense: int, xp_reward: int) -> None:
        """Initializes enemy stats and the XP reward for defeating them."""
        super().__init__(name, hp, attack_power, defense)
        self.xp_reward: int = xp_reward

    def enemy_ai_turn(self, target: Character) -> None:
        """Decides the enemy's action randomly (30% chance for special ability)."""
        if random.random() < 0.3:
            self.special_ability(target)
        else:
            self.regular_attack(target)


class Goblin(Enemy):
    """A weak, early-game enemy."""
    
    def __init__(self, name: str = "Green Goblin") -> None:
        super().__init__(name, hp=50, attack_power=12, defense=2, xp_reward=40)

    def regular_attack(self, target: Character) -> None:
        """Standard blade attack."""
        print(f"{self.name} attacks with its blade!")
        target.take_damage(self._calculate_attack())

    def special_ability(self, target: Character) -> None:
        """Throws rocks for slightly increased damage."""
        print(f"{self.name} throws rocks at {target.name}!")
        target.take_damage(self._calculate_attack() + 5)


class Witch(Enemy):
    """A magic-wielding mid-tier enemy."""
    
    def __init__(self, name: str = "Wicked Witch", hp: int = 70, attack_power: int = 16, defense: int = 2, xp_reward: int = 65) -> None:
        super().__init__(name, hp, attack_power, defense, xp_reward)

    def regular_attack(self, target: Character) -> None:
        """Casts a basic spell."""
        print(f"{self.name} murmurs a spell...")
        target.take_damage(self._calculate_attack())

    def special_ability(self, target: Character) -> None:
        """Drinks an empowering potion to increase spell damage."""
        print(f"{self.name} drinks an empowering potion before casting a spell!")
        target.take_damage(self._calculate_attack() + 10)


class Dragon(Enemy):
    """A powerful, late-game enemy boss."""
    
    def __init__(self, name: str = "Legendary Dragon") -> None:
        super().__init__(name, hp=150, attack_power=22, defense=10, xp_reward=150)

    def regular_attack(self, target: Character) -> None:
        """Standard physical tail attack."""
        print(f"{self.name} uses its tail to attack!")
        target.take_damage(self._calculate_attack())

    def special_ability(self, target: Character) -> None:
        """Breathes fire for massive damage."""
        print(f"{self.name} breathes fire!")
        target.take_damage(self._calculate_attack() + 15)