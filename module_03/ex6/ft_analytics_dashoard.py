def list_comprehension(players: list[dict[str, str |
                                          int | list[str] | bool]]) -> None:
    print("\n=== List Comprehension Examples ===")
    try:
        high_scores: list[str] = [player["name"]
                                  for player in players
                                  if player["score"] > 2000]
        print(f"High scorers (>2000): {high_scores}")
    except Exception:
        print("An error has occurred to the high scorers")
    try:
        scores_doubled: list[int] = [(player["score"] * 2)
                                     for player in players]
        print(f"Scores doubled: {scores_doubled}")
    except Exception:
        print("An error has occurred doubling the scores")
    try:
        active_players: list[str] = [player["name"]
                                     for player in players
                                     if player["active"] is True]
        print(f"Active players: {active_players}")
    except Exception:
        print("An error has occurred getting active players")


def dict_comprehension(players: list[dict[str, str |
                                          int | list[str] | bool]]) -> None:
    print("\n=== Dict Comprehension Examples ===")
    try:
        active_scores: dict[str, int] = {player["name"]: player["score"]
                                         for player in players}
        print(f"Player scores {active_scores}")
    except Exception:
        print("An error has occurred getting active players scores")
    try:
        score_categories: dict[str, int] = {"high": 0, "medium": 0, "low": 0}
        for player in players:
            if (player["score"] >= 2000):
                score_categories["high"] += 1
            elif (1000 <= player["score"] < 2000):
                score_categories["medium"] += 1
            else:
                score_categories["low"] += 1
        print(f"Score categories: {score_categories}")
    except Exception:
        print("An error has occurred getting active players scores")
    try:
        achievment_counter: dict[str, int] = {player["name"]:
                                              len(player["achievements"])
                                              for player in players
                                              if player["active"] is True}
        print(f"Achievement counts: {achievment_counter}")
    except Exception:
        print("An error has occurred counting achievements")


def set_comprehension(players: list[dict[str, str |
                                         int | list[str] | bool]]) -> None:
    print("\n=== Set Comprehension Examples ===")
    try:
        unique_players: set[str] = {player["name"]
                                    for player in players}
        print(f"Unique players: {unique_players}")
    except Exception:
        print("An error has occurred getting unique players")
    try:
        achievement_total = {achievement
                             for player in players
                             for achievement in player["achievements"]}
        unique_achiev = {achievement
                         for achievement in achievement_total
                         if (sum(achievement in player["achievements"]
                                 for player in players) == 1)}
        print(f"Unique Achievements: {unique_achiev}")
    except Exception:
        print("An error has occurred getting unique achievements")
    try:
        active_regions: set[str] = {player["region"]
                                    for player in players
                                    if player["active"] is True}
        print(f"Active regions: {active_regions}")
    except Exception:
        print("An error has occurred getting unique regions")
    print("\n=== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(achievement_total)}")
    total_score: int = 0
    for player in players:
        total_score += player["score"]
    print(f"Average score: {total_score / len(players):.1f}")
    max_score: int = max([player["score"]
                          for player in players])
    best_performer = [(player['name'], player['score'],
                      len(player['achievements']))
                      for player in players
                      if player['score'] == max_score]
    print(
        f"Top performer: {best_performer[0][0]} "
        f"({best_performer[0][1]} points, "
        f"{best_performer[0][2]} achievements)"
    )


def main() -> None:
    players: list[dict[str, str | int | list[str] | bool]]
    players = [{"name": "alice",
                "score": 2300,
                "achievements": ['first_blood',
                                 'level_master',
                                 'treasure_seeker',
                                 'boss_slayer',
                                 'combo_king'],
                "region": "east",
                "active": True},
               {"name": "bob",
                "score": 1800,
                "achievements": ['first_blood',
                                 'speed_runner',
                                 'explorer'],
                "region": "north",
                "active": True},
               {"name": "charlie",
                "score": 2150,
                "achievements": ['first_blood',
                                 'level_master',
                                 'treasure_seeker',
                                 'pixel_perfect',
                                 'combo_king',
                                 'first_kill',
                                 'level_10'],
                "region": "central",
                "active": True},
               {"name": "diana",
                "score": 2050,
                "achievements": ['first_blood',
                                 'treasure_seeker',
                                 'pixel_perfect',
                                 'level_master'
                                 'speed_runner'],
                "region": "north",
                "active": False},
               {"name": "eve",
                "score": 1500,
                "achievements": ['first_blood',
                                 'treasure_seeker',
                                 'pixel_perfect'],
                "region": "south",
                "active": False},
               {"name": "frank",
                "score": 900,
                "achievements": ['first_blood',
                                 'explorer'],
                "region": "central",
                "active": False},]
    list_comprehension(players)
    dict_comprehension(players)
    set_comprehension(players)


if (__name__ == "__main__"):
    print("=== Game Analytics Dashboard ===")
    main()
