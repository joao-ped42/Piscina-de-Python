from ex0.Card import Card
import random


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def ft_len(self, lst: list) -> int:
        ret: int = 0
        for item in lst:
            ret += 1
        return (ret)

    def add_card(self, card: Card) -> None:
        self.cards += [card]

    def is_in_deck(self, card_name: str) -> bool:
        for card in self.cards:
            if (card.name == card_name):
                return (True)
        return (False)

    def remove_card(self, card_name: str) -> bool:
        if (self.is_in_deck(card_name)):
            i: int = 0
            while (i < self.ft_len(self.cards)):
                if (self.cards[i].name == card_name):
                    del (self.cards[i])
                    return (True)
                i += 1
        return (False)

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        card_index: int = random.randrange(self.ft_len(self.cards))
        ret: Card = self.cards[card_index]
        self.remove_card(self.cards[card_index].name)
        type: str = ""
        if (ret.__class__.__name__ == "CreatureCard"):
            type = " (Creature)"
        elif (ret.__class__.__name__ == "SpellCard"):
            type = " (Spell)"
        elif (ret.__class__.__name__ == "ArtifactCard"):
            type = " (Artifact)"
        print(f"\nDrew: Mana Crystal{type}")
        return (ret)

    def get_deck_stats(self) -> dict:
        def count_creature(cards: list[Card]) -> int:
            ret: int = 0
            for card in cards:
                if (card.__class__.__name__ == "CreatureCard"):
                    ret += 1
            return (ret)

        def count_spell(cards: list[Card]) -> int:
            ret: int = 0
            for card in cards:
                if (card.__class__.__name__ == "SpellCard"):
                    ret += 1
            return (ret)

        def count_artifact(cards: list[Card]) -> int:
            ret: int = 0
            for card in cards:
                if (card.__class__.__name__ == "ArtifactCard"):
                    ret += 1
            return (ret)

        def avg_cost(cards: list[Card]) -> float:
            total_cards: int = self.ft_len(cards)
            total_cost: int = 0
            for card in cards:
                total_cost += card.cost
            if (total_cards != 0):
                return (total_cost / total_cards)
            return (0)

        ret: dict = {"total_cards": self.ft_len(self.cards),
                     "creatures": count_creature(self.cards),
                     "spells": count_spell(self.cards),
                     "artifacts": count_artifact(self.cards),
                     "avg_cot": avg_cost(self.cards)}
        return (ret)
