from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\nTesting Abstract Base Class Design:")
    card1: CreatureCard = CreatureCard("Reshiram", 5, "Legendary", 7, 5)
    print(card1.get_card_info())

    print("\nPlaying Fire Dragon with 6 mana available:")
    print(f"Playable: {card1.is_playable(6)}")
    print("Play result: "
          f"{card1.play({"mana_used": 6,
                         "effect": "Creature summoned to battlefield"})}")

    print("\nReshiram attacks Zekrom:")
    card2: CreatureCard = CreatureCard("Zekrom", 5, "Legendary", 10, 3)
    print(f"Attack result: {card1.attack_target(card2)}")

    print("\nTesting insufficient mana (3 available):")
    print(f"Playable: {card1.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if (__name__ == "__main__"):
    print("\n=== DataDeck Card Foundation ===")
    main()
