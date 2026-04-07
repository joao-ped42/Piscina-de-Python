from ex1.Capabilities import HealCapability, TransformCapability
from ex0 import Pokemon


class Bulbasaur(Pokemon, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bulbasaur", "Grass/Poison")

    def attack(self) -> str:
        return ("Bulbasaur uses Vine Whip!")

    def heal(self, target: Pokemon) -> str:
        if (target.name == self.name):
            return ("Bulbasaur uses Synthesis!")
        return (f"Bulbasaur healed {target.name} for a small amount")


class Venusaur(Pokemon, HealCapability):
    def __init__(self) -> None:
        super().__init__("Venusaur", "Grass/Poison")

    def attack(self) -> str:
        return ("Venusaur uses Petal Blizzard!")

    def heal(self, target: Pokemon) -> str:
        if (target.name == self.name):
            return ("Venusaur uses Synthesis!")
        return (f"Venusaur healed {target.name} for a small amount")


class Zorua(Pokemon, TransformCapability):
    def __init__(self):
        super().__init__("Zorua", "Dark")
        self.transformed: bool = False

    def attack(self) -> str:
        if (self.transformed):
            return ("Zorua performs a boosted strike!")
        return ("Zorua uses Bite!")

    def transform(self, target: Pokemon) -> str:
        self.transformed = True
        return ("Zorua hifts into a sharper form!")

    def revert(self):
        self.transformed = False
        return ("Zorua returns to normal")


class Zoroark(Pokemon, TransformCapability):
    def __init__(self):
        super().__init__("Zoroark", "Dark")
        self.transformed: bool = False

    def attack(self) -> str:
        if (self.transformed):
            return ("Zoroark unleashes a devastating mega strike!")
        return ("Zoroark uses Bite!")

    def transform(self, target: Pokemon) -> str:
        self.transformed = True
        return ("Zoroark mega evolved!")

    def revert(self):
        self.transformed = False
        return ("Zoroark stabilizes its form")
