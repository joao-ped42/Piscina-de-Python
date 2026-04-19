from collections.abc import Callable
from functools import wraps
from time import perf_counter
from typing import Any


def power_validator(min_power: int) -> Callable:
    def dec_factory(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str:
            if (args[2] >= min_power):
                return (func(*args, **kwargs))
            return ("Insuficient power for this spell")
        return (wrapper)
    return (dec_factory)


def retry_spell(max_attempts: int) -> Callable:
    def dec_factory(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> str | None:
            for retry in range(1, max_attempts + 1):
                try:
                    return (func(*args, **kwargs))
                except Exception:
                    if (retry < max_attempts):
                        print(f"Spell failed, retrying... (attempt {retry}/"
                              f"{max_attempts})")
                    else:
                        print(f"Spell casting failed after {max_attempts}",
                              "attempts")
                        return ("Waaaaaaagh spelled!")
            return (None)
        return (wrapper)
    return (dec_factory)


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if (len(name) < 3):
            return (False)
        for char in name:
            if (not (char.isalpha() or char.isspace())):
                return (False)
        return (True)

    @retry_spell(3)
    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (f"Successfully cast {spell_name} with {power} power")


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        print(f"Casting {func.__name__}")
        start: float = perf_counter()
        ret: Any = func(*args, **kwargs)
        end: float = perf_counter()
        print(f"Spell completed in {(end - start):.3f} seconds")
        if (ret is not None):
            print(f"Result: {ret}")
    return (wrapper)


@spell_timer
def Fireball() -> str:
    return ("Fireball cast!")


def main() -> None:
    print("Testing spell timer...")
    Fireball()

    print("\nTesting retrying spell...")
    guild: MageGuild = MageGuild()
    print(guild.cast_spell("Lightning", "15"))

    print("\nTesting MageGuild")
    print(guild.validate_mage_name("Quasimodo"))
    print(guild.validate_mage_name("6767"))
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Lightning", 1))


if (__name__ == "__main__"):
    main()
