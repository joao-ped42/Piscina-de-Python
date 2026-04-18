from collections.abc import Callable
from typing import Any


def fireball(target) -> str:
    return (f"Fireball hits {target}")


def basic_heal(target: str) -> str:
    return (f"Heals {target}")


def dragon_flame(power: int, target: str) -> str:
    return (f"Dragon Flame hits {target} with {power} power")


def hydro_pump(power: int, target: str) -> str:
    return (f"Hydro Pump hits {target} with {power} power")


def spin_dash(power: int, target: str) -> str:
    return (f"Spin Dash hits {target} with {power} power")


def valid_target(target: str) -> bool:
    return (target == "Trump")


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def new_spell(*args: tuple[Any]) -> str:
        ret: str = spell1(*args) + ", " + spell2(*args)
        return (ret)
    return (new_spell)


def power_amplifier(base_spell: Callable, multiplier: int,) -> Callable:
    def power_amplified(base_power: int, *args: tuple[Any]) -> str:
        new_power: int = base_power * multiplier
        ret: str = base_spell(new_power, *args)
        return (ret)
    return (power_amplified)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def apply_cond(target: str, *args: tuple[Any]) -> str:
        if (condition(target)):
            return (spell(*args, target))
        return ("Spell fizzled")
    return (apply_cond)


def spell_sequence(spells: list[Callable]) -> Callable:
    def speller() -> None:
        for spell in spells:
            print(spell(9999, "Trump"))
    return (speller)


def main() -> None:
    print("\nTesting spell combiner...")
    spells_combined: Callable = spell_combiner(basic_heal,
                                               fireball)
    print(spells_combined("Dragon"))

    print("\nTesting power amplifier...")
    amplified_spell: Callable = power_amplifier(dragon_flame, 3)
    print(amplified_spell(50, "Sonic"))

    print("\nTesting conditional caster...")
    cond_dragon: Callable = conditional_caster(valid_target,
                                               dragon_flame)
    print(cond_dragon("Trump", 9999))
    print(cond_dragon("Erika", 9999))

    print("\nTesting spell sequence...")
    spells: list[Callable] = [dragon_flame,
                              hydro_pump,
                              spin_dash]
    caster: Callable = spell_sequence(spells)
    caster()


if (__name__ == "__main__"):
    main()
