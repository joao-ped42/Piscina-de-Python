from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str,
                 cost: int, rarity: str,
                 durability: int, effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability: int = 2
        self.effect: str = "Makes rain"
        if (durability > 0):
            self.durability = durability
        if (not ((effect == "") or (not effect))):
            self.effect = effect
        self.active: bool = False
        self.used: bool = False

    def play(self, game_state: dict) -> dict:
        try:
            if (game_state["mana_used"] >= self.cost):
                ret: dict = {"card_played": self.name,
                             "mana_used": self.cost,
                             "effect": self.effect}
            else:
                print(f"{game_state["mana_used"]} mana is insufficient "
                      f"(Cost: {self.cost})")
                return ({})
        except KeyError:
            print("Couldn't play this card, insufficient info was given")
            return ({None})
        return (ret)

    def activate_ability(self) -> dict:
        if (self.used is False):
            self.used = True
            self.active = True
            ret: dict = {"active": self.active,
                         "used": self.used,
                         "effect": self.effect}
        else:
            print("You can only use an Artifact Card once")
            return ({None})
        return (ret)
