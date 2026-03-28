from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str,
                 cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type: str = "damage"
        effect_types: list[str] = ["damage", "heal", "buff", "debuff"]
        for effect in effect_types:
            if (effect in effect_type):
                self.effect_type = effect_type
        self.used: bool = False

    def play(self, game_state: dict) -> dict:
        try:
            if (game_state["mana_used"] >= self.cost):
                ret: dict = {"card_played": self.name,
                             "mana_used": self.cost,
                             "effect": self.effect_type}
            else:
                print(f"{game_state["mana_used"]} mana is insufficient "
                      f"(Cost: {self.cost})")
                return ({None})
        except KeyError:
            print("Couldn't play this card, insufficient info was given")
            return ({None})
        return (ret)

    def resolve_effect(self, targets: list) -> dict:
        pass
