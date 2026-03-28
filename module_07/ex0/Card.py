from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self.name: str = name
        self.cost: int = cost
        self.rarity: str = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        ...

    def get_card_info(self) -> dict:
        print("\nCard Info:")
        ret: dict = {"name": self.name,
                     "cost": self.cost,
                     "rarity": self.rarity}
        return (ret)

    def is_playable(self, avaliable_mana: int) -> bool:
        if (avaliable_mana >= self.cost):
            return (True)
        return (False)
