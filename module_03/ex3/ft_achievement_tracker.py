def unlock_achievment(player: set[str], achievment_list: set[str],
                      achievment: str) -> None:
    if (achievment in achievment_list):
        player.add(achievment)
    else:
        print("There isn't any achievment with that name")


def unlock_all(player1: set[str], player2: set[str], player3: set[str],
               achiev: list[str]) -> None:
    unlock_achievment(player1, achiev, "first_kill")
    unlock_achievment(player2, achiev, "first_kill")
    unlock_achievment(player1, achiev, "level_10")
    unlock_achievment(player2, achiev, "level_10")
    unlock_achievment(player3, achiev, "level_10")
    unlock_achievment(player1, achiev, "treasure_hunter")
    unlock_achievment(player3, achiev, "treasure_hunter")
    unlock_achievment(player2, achiev, "boss_slayer")
    unlock_achievment(player3, achiev, "boss_slayer")
    unlock_achievment(player1, achiev, "speed_demon")
    unlock_achievment(player3, achiev, "speed_demon")
    unlock_achievment(player2, achiev, "collector")
    unlock_achievment(player3, achiev, "perfectionist")


def count_achievments(achievment: str, players: list[set[str]]) -> int:
    count: int = 0
    for player in players:
        if (achievment in player):
            count += 1
    return (count)


def main() -> None:
    achievments: set[str] = {'boss_slayer', 'collector', 'first_kill',
                             'level_10', 'perfectionist', 'speed_demon',
                             'treasure_hunter'}
    alice_achievments: set[str] = set()
    bob_achievments: set[str] = set()
    charlie_achievments: set[str] = set()
    players: list[set[str]] = []
    players.append(alice_achievments)
    players.append(bob_achievments)
    players.append(charlie_achievments)
    unlock_all(alice_achievments, bob_achievments, charlie_achievments,
               achievments)
    print(f"Player alice achievments: {alice_achievments}")
    print(f"Player bob achievments: {bob_achievments}")
    print(f"Player charlie achievments: {charlie_achievments}")
    print("\n=== Achievement Analytics ===")
    print("All unique achievments:", achievments)
    print(f"Total unique achievments: {len(achievments)}")
    print(f"\nCommon to all players: "
          f"{alice_achievments & bob_achievments & charlie_achievments}")
    all: set[str] = alice_achievments.union(
        bob_achievments).union(charlie_achievments)
    a_b: set[str] = alice_achievments.intersection(bob_achievments)
    ac: set[str] = alice_achievments.intersection(charlie_achievments)
    bc: set[str] = bob_achievments.intersection(charlie_achievments)
    abc: set[str] = a_b.intersection(charlie_achievments)
    comuns: set[str] = a_b.union(ac).union(bc).union(abc)
    rare: set[str] = all.difference(comuns)
    print(f"Rare achievements (1 player): {rare}")
    print(f"\nAlice vs Bob common: "
          f"{alice_achievments.intersection(bob_achievments)}")
    print(f"Alice unique: "
          f"{alice_achievments - bob_achievments}")
    print(f"Bob unique: "
          f"{bob_achievments - alice_achievments}")


if (__name__ == "__main__"):
    print("=== Achievement Tracker System ===")
    main()
