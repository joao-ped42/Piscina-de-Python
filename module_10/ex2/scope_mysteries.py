from collections.abc import Callable


def mage_counter() -> Callable:
    total_calls: int = 0

    def counter() -> int:
        nonlocal total_calls
        total_calls += 1
        return (total_calls)
    return (counter)


def spell_accumulator(initial_power: int) -> Callable:
    def accumulate(add_power: int) -> int:
        nonlocal initial_power
        initial_power += add_power
        return (initial_power)
    return (accumulate)


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(tool: str) -> str:
        nonlocal enchantment_type
        tool = enchantment_type + ' ' + tool
        return (tool)
    return (enchant)


def memory_vault() -> dict[str, Callable]:
    warehouse: dict[str, int] = {}

    def store(key: str, value: int) -> None:
        nonlocal warehouse
        print(f"Store '{key}' = {value}")
        warehouse.update({key: value})

    def recall(key: str) -> int | str:
        try:
            return (warehouse[key])
        except KeyError:
            return ("Memory not found")

    return ({"store": store, "recall": recall})


def main() -> None:
    print("Testing mage counter...")
    counter_a: Callable = mage_counter()
    counter_b: Callable = mage_counter()
    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting mage counter...")
    power_acc: Callable = spell_accumulator(100)
    print(f"Base 100: add 20: {power_acc(20)}")
    print(f"Base 100: add 30: {power_acc(30)}")

    print("\nTesting enchantment_factory...")
    frozen: Callable = enchantment_factory("Frozen")
    flaming: Callable = enchantment_factory("Flaming")
    print(frozen("Sword"))
    print(flaming("Shield"))

    print("\nTesting memory vault...")
    manage: dict[str, Callable] = memory_vault()
    manage["store"]("secret", 42)
    print("Recall 'secret':", manage["recall"]("secret"))
    print("Recall 'unknown':", manage["recall"]("unknown"))


if (__name__ == "__main__"):
    main()
