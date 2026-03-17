import typing
import time


def is_prime(num: int) -> bool:
    if (num == 1):
        return False
    for i in range(2, int(num / 2) + 1):
        if num % i == 0:
            return False
    return True


def primes() -> typing.Generator[int, None, None]:
    ret: int = 2
    while True:
        if (is_prime(ret)):
            yield ret
        ret += 1


def fibonacci() -> typing.Generator[int, None, None]:
    yield (0)
    yield (1)
    prev: int = 1
    prev_prev: int = 0
    ret: int
    while True:
        ret = prev_prev + prev
        yield ret
        prev_prev = prev
        prev = ret


def event(players: list[dict[str, int | str]],
          event: dict[str, int],
          quantity: int) -> typing.Generator[str, None, None]:
    events: list[str] = ["killed monster", "found treasure", "leveled up",
                         "died", "resurrected", "got an item",
                         "went to jail", "was set free", "killed someone",
                         "went away", "found a witch"]
    for i in range(quantity):
        ret: str = (f"Event {i}: Player {players[i % 4]['name']} "
                    f"(level: {players[int(i % 4)]['level']}) "
                    f"{events[i % 11]}")
        if (events[i % 9] == "leveled up"):
            players[i % 4]['level'] += 1
            event["level"] += 1
        elif (events[i % 9] == "found treasure"):
            event["treasure"] += 1
        yield ret


def main() -> None:
    print("=== Game Data Stream Processor ===")
    quantity: int = 67
    players: list[dict[str, int | str]] = [{"name": "alice", "level": 5},
                                           {"name": "bob", "level": 12},
                                           {"name": "charlie", "level": 7},
                                           {"name": "diana", "level": 80}]
    event_count: dict[str, int] = {"treasure": 0, "level": 0}
    event_gen = event(players, event_count, 1000)
    print(f"\nProcessing {quantity} game events...\n")
    start_time: float = time.time()
    for i in range(quantity):
        print(next(event_gen))
    finish_time: float = time.time()
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {quantity}")
    high_level: int = 0
    for dic in players:
        if (dic["level"] >= 10):
            high_level += dic["level"]
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {event_count['treasure']}")
    print(f"Level-up events: {event_count['level']}")
    print("\nMemory usage: Constant (streaming)")
    print(f"Processing time: {(finish_time - start_time):.3f}")
    print("\n=== Generator Demonstration ===")
    limit_prime: int = 5
    limit_f: int = 10
    prime: list[str] = []
    fibb: list[str] = []
    prime_gen: typing.Generator = primes()
    f_gen: typing.Generator = fibonacci()
    print(f"Fibonacci sequence: (first {limit_f}): ", end="")
    for i in range(0, limit_f):
        fibb.append(str(next(f_gen)))
    print(", ".join(fibb))
    print(f"Prime numbers (first {limit_prime}): ", end="")
    for i in range(0, limit_prime):
        prime.append(str(next(prime_gen)))
    print(", ".join(prime))


if (__name__ == "__main__"):
    print("=== Game Data Stream Processor ===")
    main()
