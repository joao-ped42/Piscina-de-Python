import sys


def main(argv: list[str]) -> None:
    argv_len: int = len(argv)
    i: int = 1

    if (argv_len == 1):
        print("No arguments provided!")
        print(f"Program name: {argv[0]}")
        print(f"Total arguments: {len(argv)}\n")
        return
    print(f"Program name: {argv[0]}")
    print(f"Arguments received: {argv_len - 1}")
    while (i <= (argv_len - 1)):
        print(f"Argument {i}: {argv[i]}")
        i += 1
    print(f"Total arguments: {len(argv)}\n")


if (__name__ == "__main__"):
    print("=== Command Quest ===")
    main(sys.argv)
