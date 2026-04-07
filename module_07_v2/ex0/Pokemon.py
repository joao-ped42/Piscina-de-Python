from abc import ABC, abstractmethod


class Pokemon(ABC):
    def __init__(self, name: str, type: str) -> None:
        self.name: str = name
        self.type: str = type

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return (f"{self.name} is a {self.type} type Pokémon")


class Torchic(Pokemon):
    def __init__(self) -> None:
        super().__init__("Torchic", "Fire")

    def attack(self) -> str:
        return ("Torchic uses Ember!")


class Blaziken(Pokemon):
    def __init__(self) -> None:
        super().__init__("Blaziken", "Fire/Fighting")

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
