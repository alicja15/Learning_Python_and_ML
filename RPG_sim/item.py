class Item:
    """Represents an equippable item that modifies a character's stats."""
    
    def __init__(self, name: str, item_type: str, stat_bonus: int) -> None:
        """Initializes a new item."""
        self.name: str = name
        self.item_type: str = item_type  # Expected: "attack" or "defense"
        self.stat_bonus: int = stat_bonus

    def __str__(self) -> str:
        """Returns a string representation of the item."""
        return f"{self.name} (+{self.stat_bonus} {self.item_type})"