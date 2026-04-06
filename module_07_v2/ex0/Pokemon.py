from abc import ABC, abstractmethod


class Pokemon(ABC):
    def __init__(self, name: str, type: str, hp: int, speed: int) -> None:
        self.name: str = name
        self.type: str = type
        self.hp: int = hp
        self.speed: int = speed

    @abstractmethod
    def attack(self, attack_name: str) -> str:
        ...

    def describe(self) -> str:
        return (f"{self.name} is a {self.type} type Pokémon")


class Torchic(Pokemon):
    def __init__(self) -> None:
        super().__init__("Torchic", "Fire")
        self.attacks: list[str] = ["Scratch", "Ember", "Peck", "Sand Attack"]

    def attack(self, attack_name: str, target: Pokemon) -> str:
        if (attack_name in self.attacks):
            return (f"Torchic uses {attack_name}")
        return ("Torchic does not have this attack")


class Blaziken(Pokemon):
    def __init__(self) -> None:
        super().__init__("Blaziken", "Fire/Fighting")
        self.attacks: list[str] = ["Slash", "Blaze Kick",
                                   "Fire Blitz", "Brave Bird"]

    def attack(self) -> str:
        return ("Blaziken uses Blaze Kick!")


class Popplio(Pokemon):
    def __init__(self) -> None:
        super().__init__("Popplio", "Water")

    def attack(self) -> str:
        return ("Popplio uses Water Gun!")


class Primarina(Pokemon):
    def __init__(self) -> None:
        super().__init__("Primarina", "Water/Fairy")

    def attack(self) -> str:
        return ("Primarina uses Hydro Punp!")
