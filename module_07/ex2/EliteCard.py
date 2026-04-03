from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex0.Card import Card


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        Card.__init__(self, name, cost, rarity)
        self.current_life: int = 10
        self.damage: int = 5
        self.current_life: int = 10
        self.combat_type: str = "melee"

    def attack(self, target: Card) -> dict:
        ret: dict = {"attacker": self.name,
                     "target": target.name,
                     "damage": self.damage,
                     "still_alive": self.combat_type}
        return (ret)

    def defend(self, incoming_damage: int) -> dict:
        damage_taken: int = incoming_damage - 3
        self.current_life -= damage_taken
        alive: bool = True
        if (self.current_life <= 0):
            self.current_life = 0
            alive = False
        ret: dict = {"attacker": self.name,
                     "damage_taken": damage_taken,
                     "damage_blocked": 3,
                     "still_alive": alive}
        return (ret)
