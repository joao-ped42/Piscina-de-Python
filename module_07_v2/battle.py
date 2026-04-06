from ex0.Pokemon import Pokemon
import ex0


def pokeshowdown(factory: ex0.PokemonFactory) -> None:
    print("\nTesting factory")
    poke = factory.create_base()
    poke_evo = factory.create_evolved()
    print(poke.describe())
    print(poke.attack())
    print(poke_evo.describe())
    print(poke_evo.attack())


def battle(attacker: Pokemon, opponent: Pokemon) -> None:
    print("\nTesting battle")
    print(attacker.describe())
    print("            vs.")
    print(opponent.describe())
    print("           fight!")
    print(attacker.attack())
    print(opponent.attack())


if (__name__ == "__main__"):
    flame: ex0.FlameFactory = ex0.FlameFactory()
    aqua: ex0.AquaFactory = ex0.AquaFactory()
    pokeshowdown(flame)
    pokeshowdown(aqua)
    torchic: Pokemon = flame.create_base()
    popplio: Pokemon = aqua.create_base()
    battle(torchic, popplio)
