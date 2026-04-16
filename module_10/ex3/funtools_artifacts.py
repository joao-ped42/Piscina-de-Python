from functools import reduce, partial
from operator import add, mul
from collections.abc import Callable


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
    r: dict[str, Callable] = {"fortune": fixed("Fortune", "Pickaxe"),
                              "fire_touch": fixed("Fire Touch", "Sword"),
                              "silk_touch": fixed("Silk Touch", "Shovel")}
    return (r)


def main() -> None:
    print("\nTesting spell reducer...")
    numbers: list[int] = [40, 10, 30, 20]
    print("Sum:", spell_reducer(numbers, "add"))
    print("Multiply", spell_reducer(numbers, "multiply"))
    print("Max:", spell_reducer(numbers, "max"))

    print("\nTesting partial enchanter...")
    partial_enchanter(enchant)


if (__name__ == "__main__"):
    main()