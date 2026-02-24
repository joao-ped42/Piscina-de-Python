import sys


def main(argv: list[str]) -> None:
    if (len(argv) == 1):
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")
        return
    try:
        score_list: list[int] = [int(n) for n in argv[1:]]
        print(f"Scores processed: {score_list}")
        print(f"Total players: {len(score_list)}")
        print(f"Total score: {sum(score_list)}")
        print(f"Average score: {sum(score_list) / len(score_list)}")
        print(f"High score: {max(score_list)}")
        print(f"Low score: {min(score_list)}")
        print(f"Score range: {max(score_list) - min(score_list)}\n")
    except ValueError:
        print("This program only accepts numbers as entries.")


if (__name__ == "__main__"):
    print("=== Player Score Analytics ===")
    main(sys.argv)
