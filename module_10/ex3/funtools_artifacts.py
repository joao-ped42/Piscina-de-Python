from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul
from collections.abc import Callable
from typing import Any


def enchant(power: int, element: str, target: str) -> str:
    return (f"Enchanted {target} with {element} (level {power})")


def spell_reducer(spells: list[int], operation: str) -> int:
    ret: int = 0
    match operation:
        case "add":
            ret = reduce(add, spells)
        case "multiply":
            ret = reduce(mul, spells)
        case "max":
            ret = reduce(max, spells)
        case "min":
            ret = reduce(min, spells)
        case _:
            print("Unsupported operation")
    return (ret)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    fixed: Callable = partial(base_enchantment, power=50)
    r: dict[str, Callable] = {"fortune": fixed(element="Fortune",
                                               target="Pickaxe"),
                              "fire_touch": fixed(element="Fire Touch",
                                                  target="Sword"),
                              "silk_touch": fixed(element="Silk Touch",
                                                  target="Shovel")}
    return (r)


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if (n <= 0):
        return (0)
    elif (n == 1):
        return (1)
    return (memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2))


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatching(argument: Any) -> str:
        return (f"{type(argument)} is unknown.")

    @dispatching.register(int)
    def _(argument: int) -> str:
        return (f"{argument} damage")

    @dispatching.register(str)
    def _(argument: str) -> str:
        return (f"{argument}")

    @dispatching.register(list)
    def _(argument: list) -> str:
        return (f"{len(argument)} spells")

    return (dispatching)


def main() -> None:
    print("\nTesting spell reducer...")
    numbers: list[int] = [40, 10, 30, 20]
    print("Sum:", spell_reducer(numbers, "add"))
    print("Multiply", spell_reducer(numbers, "multiply"))
    print("Max:", spell_reducer(numbers, "max"))

    print("\nTesting partial enchanter...")
    enchants: dict[str, Callable] = partial_enchanter(enchant)
    for enc in enchants.values():
        print(enc)

    print("\nTesting memoized fibonacci...")
    positions: list[int] = [0, 1, 10, 15]
    for index in positions:
        print(f"Fib({index}): {memoized_fibonacci(index)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    tests: dict[str, int | str | list] = {"Damage spell": 42,
                                          "Enchantment": "fireball",
                                          "Multi-cast": ["1", "3", "5"]}
    for key, value in tests.items():
        print(f"{key}: {dispatcher(value)}")
    print(dispatcher({"naruto": 1}))


if (__name__ == "__main__"):
    main()
