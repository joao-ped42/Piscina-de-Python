from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck
from ex0.Card import Card


from random import randrange


def main() -> None:
    print("\nBuilding deck with different card types...")
    deck: Deck = Deck()
    cards: list[Card] = [CreatureCard("Reshiram", 5,
                                      "Legendary", 7, 5),
                         SpellCard("Thunderbolt", 4,
                                   "common", "Deal 3 damage to target"),
                         ArtifactCard("Mana Crystal", 3,
                                      "common", 20,
                                      "Permanent: +1 mana per turn")]
    for card in cards:
        deck.add_card(card)
    print(f"Deck stats: {deck.get_deck_stats()}")

    print("\nDrawing and playing cards:")
    while (deck.get_deck_stats()["total_cards"] > 0):
        card: Card = deck.draw_card()
        game_stats: dict[str, int] = {"mana_used": randrange(2, 6)}
        print(f"Play result: {card.play(game_stats)}")

    print("\nPolymorphism in action:",
          "Same interface, different card behaviors!")


if (__name__ == "__main__"):
    print("=== DataDeck Deck Builder ===")
    main()
