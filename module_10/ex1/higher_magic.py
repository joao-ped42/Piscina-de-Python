from collections.abc import Callable


def spell(target: str, power: int) -> str:
    return (f"{target} suffered {power} damage")


def heal(target: str, power: int) -> str:
    return (f"Heal restores {target} for {power} HP")


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def strcat(str1: str, str2: str) -> str: