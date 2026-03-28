from ex0.Card import Card


class CreatureCard(Card):
    def __init__(self, name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack: int = 0
        if (attack > 0):
            self.attack = attack
        else:
            self.attack = 3
        self.health: int = 0
        if (health > 0):
            self.health = health
        else:
            self.health = 5

    def play(self, game_state: dict) -> dict:
        try:
            if (game_state["mana_used"] >= self.cost):
                ret: dict = {"card_played": self.name,
                             "mana_used": self.cost,
                             "effect": game_state["effect"]}
            else:
                print(f"{game_state["mana_used"]} mana is insufficient "
                      f"(Cost: {self.cost})")
                return ({})
        except KeyError:
            print("Couldn't play this card, insufficient info was given")
            return ({None})
        return (ret)

    def get_card_info(self) -> dict:
        print("CreatureCard Info:")
        ret: dict = {"name": self.name,
                     "cost": self.cost,
                     "rarity": self.rarity,
                     "type": "Creature",
                     "attack": self.attack,
                     "health": self.health}
        return (ret)

    def attack_target(self, target: "CreatureCard") -> dict:
        resolved: bool = False
        if (self.attack > target.health):
            resolved = True
        ret: dict = {"attacker": self.name,
                     "target": target.name,
                     "damage_dealt": self.attack,
                     "combat_resolved": resolved}
        return (ret)
