class Character:
    def __init__(
        self,
        name: str,
        health: int = 100,
        strength: int = 10,
        inventory: list = [],
    ) -> None:
        self.name = name
        self.health = health
        self.strength = strength
        self.inventory = inventory
    