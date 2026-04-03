from ex2.EliteCard import EliteCard


def main() -> None:
    print("\nEliteCard capabilities:")
    elite_capabilities: dict = {"Card": ["play",
                                         "get_card_info",
                                         "is_playable"],
                                "Combatable": ["attack",
                                               "defend",
                                               "get_combat_stats"],
                                "Magical": ["cast_spell",
                                            "channel_mana",
                                            "get_magic_stats"]}
    for cap in elite_capabilities:
        print(f"-{cap}: {elite_capabilities[cap]}")

    print("\nPlaying Arcane Warrior (Elite Card):")

    print("\nCombat phase:")
    arcane_warrior: EliteCard = EliteCard("Arcane Warrior", 3, "Common")
    enemy: EliteCard = EliteCard("Enemy", 1, "Very Common")
    enemy2: EliteCard = EliteCard("Enemy2", 1, "Very Common")
    print(f"Attack result: {arcane_warrior.attack(enemy)}")
    print(f"Defense result: {arcane_warrior.defend(5)}")

    print("\nMagic phase:")


if (__name__ == "__main__"):
    print("\n=== DataDeck Ability System ===")
    main()
