from abc import ABC
from ex0.Card import Card


class Combatable(ABC):
    def attack(self, target: Card) -> dict:
        pass

    def defend(self, incoming_damage: int) -> dict:
        pass

    def get_combat_stats(self) -> dict:
        pass
