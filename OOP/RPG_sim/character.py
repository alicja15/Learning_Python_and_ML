from abc import ABC, abstractmethod
import random
from item import Item

class Character(ABC):
    """Abstract base class for all characters in the game."""
    
    def __init__(self, name: str, hp: int, attack_power: int, defense: int) -> None:
        """Initializes character with base stats and empty inventory."""
        self.name: str = name
        self.max_hp: int = hp
        self.hp: int = hp
        self.base_attack: int = attack_power
        self.base_defense: int = defense
        self.inventory: list[Item] = []
        self.level: int = 1
        self.xp: int = 0
        self.xp_to_next_level: int = 100

    def _calculate_attack(self) -> int:
        """Private method calculating total attack power including item bonuses."""
        bonus = sum(item.stat_bonus for item in self.inventory if item.item_type == "attack")
        return self.base_attack + bonus

    def _calculate_defense(self) -> int:
        """Private method calculating total defense including item bonuses."""
        bonus = sum(item.stat_bonus for item in self.inventory if item.item_type == "defense")
        return self.base_defense + bonus

    def is_alive(self) -> bool:
        """Checks if the character is still alive."""
        return self.hp > 0

    def take_damage(self, damage: int, ignore_defense: bool = False) -> int:
        """Calculates and applies damage to the character, handling dodge and defense logic."""
        if random.random() < 0.15:
            print(f"{self.name} successfully dodged an attack!")
            return 0
            
        defense_val = 0 if ignore_defense else self._calculate_defense()
        actual_damage = max(1, damage - defense_val)
        self.hp = max(0, self.hp - actual_damage)
        
        print(f"{self.name} received {actual_damage} dmg! (HP left: {self.hp}/{self.max_hp})")
        return actual_damage

    @abstractmethod
    def regular_attack(self, target: 'Character') -> None:
        """Abstract method for a basic attack."""
        pass

    @abstractmethod
    def special_ability(self, target: 'Character') -> None:
        """Abstract method for a special ability."""
        pass

    def add_item(self, item: Item) -> None:
        """Adds an item to the character's inventory."""
        self.inventory.append(item)
        print(f"{self.name} picked up an item: {item}")

    def gain_xp(self, amount: int) -> None:
        """Increases character experience and triggers a level up if the threshold is met."""
        self.xp += amount
        print(f"{self.name} gained {amount} XP")
        if self.xp >= self.xp_to_next_level:
            self._level_up()
    
    def _level_up(self) -> None:
        """Private method that levels up the character and scales their stats."""
        self.level += 1
        self.xp = 0
        self.xp_to_next_level = int(self.xp_to_next_level * 1.25)
        self.max_hp += 20
        self.base_attack += 5
        self.base_defense += 2
        self.hp = self.max_hp
        print(f"{self.name} just leveled up to level {self.level}!")


class Warrior(Character):
    """Warrior character class, specializing in melee combat."""
    
    def __init__(self, name: str) -> None:
        """Initializes the Warrior with predefined base stats."""
        super().__init__(name, hp=120, attack_power=18, defense=8)

    def regular_attack(self, target: Character) -> None:
        """Performs a regular attack with a 12% critical hit chance."""
        print(f"Warrior {self.name} attacks!")
        is_crit = random.random() < 0.12 
        damage = self._calculate_attack()
        
        if is_crit:
            damage = int(damage * 1.5)
            print("Critical hit!")
            
        target.take_damage(damage)

    def special_ability(self, target: Character) -> None:
        """Uses a piercing blade skill that completely ignores the enemy's defense."""
        print(f"Warrior {self.name} uses his piercing blade skill and ignores the enemy's defense!")
        damage = self._calculate_attack()
        target.take_damage(damage, ignore_defense=True)


class Mage(Character):
    """Mage character class, specializing in magic and mana usage."""
    
    def __init__(self, name: str) -> None:
        """Initializes the Mage with predefined base stats and mana."""
        super().__init__(name, hp=80, attack_power=25, defense=3)
        self.mana: int = 50

    def regular_attack(self, target: Character) -> None:
        """Fires a standard magic projectile."""
        print(f"Mage {self.name} fires a projectile!")
        target.take_damage(self._calculate_attack())

    def special_ability(self, target: Character) -> None:
        """Casts Fireball for double damage, consuming mana."""
        if self.mana >= 20:
            self.mana -= 20
            print(f"{self.name} uses Fireball!")
            target.take_damage(self._calculate_attack() * 2)
        else:
            print(f"Not enough mana! {self.name} fires a regular projectile instead.")
            self.regular_attack(target)


class Archer(Character):
    """Archer character class, specializing in ranged, multi-hit attacks."""
    
    def __init__(self, name: str) -> None:
        """Initializes the Archer with predefined base stats."""
        super().__init__(name, hp=95, attack_power=20, defense=5)

    def regular_attack(self, target: Character) -> None:
        """Shoots an arrow with an 18% critical hit chance."""
        print(f"Archer {self.name} shoots an arrow!")
        is_crit = random.random() < 0.18
        damage = self._calculate_attack()
        
        if is_crit:
            damage *= 2
            print("Bullseye! Critical damage applied.")
            
        target.take_damage(damage)

    def special_ability(self, target: Character) -> None:
        """Uses Rain of Arrows to attack multiple times in succession."""
        print(f"{self.name} uses Rain of Arrows!")
        self.regular_attack(target)
        
        if target.is_alive() and random.random() > 0.10: # 10% miss chance
            self.regular_attack(target) 
            
        if target.is_alive() and random.random() > 0.25: # 25% miss chance
            self.regular_attack(target)