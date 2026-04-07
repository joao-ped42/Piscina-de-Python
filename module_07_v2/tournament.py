from ex2.Strategies import NormalStrategy, AgressiveStrategy
from ex2.Strategies import DefensiveStrategy, BattleStrategy
from ex0 import Pokemon, FlameFactory, AquaFactory
import ex1


def battle(opponents: list[tuple[Pokemon, BattleStrategy]]) -> None:
    size: int = len(opponents)
    i: int = 0
    while (i < size):
        j: int = i + 1
        while (j < size):
            poke1: Pokemon = opponents[i][0]
            strat1: BattleStrategy = opponents[i][1]
            poke2: Pokemon = opponents[j][0]
            strat2: BattleStrategy = opponents[j][1]
            print("\n========================================================")
            print("\n * Battle *")
            print(poke1.describe())
            print("            vs.")
            print(poke2.describe())
            print("         now fight!\n")
            try:
                strat1.act(poke1, poke2)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return
            try:
                strat2.act(poke2, poke1)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return
            print("\n========================================================")
            print("\n\n")
            j += 1
        i += 1


def main() -> None:
    fire_factory: FlameFactory = FlameFactory()
    water_factory: AquaFactory = AquaFactory()
    heal_factory: ex1.HealingPokemonFactory = ex1.HealingPokemonFactory()
    trans_factory: ex1.TransformPokemonFactory = ex1.TransformPokemonFactory()

    torchic: Pokemon = fire_factory.create_base()
    primarina: Pokemon = water_factory.create_evolved()
    bulba: Pokemon = heal_factory.create_base()
    venu: Pokemon = heal_factory.create_evolved()
    zoroark: Pokemon = trans_factory.create_evolved()

    normal: NormalStrategy = NormalStrategy()
    heal: DefensiveStrategy = DefensiveStrategy()
    agressive: AgressiveStrategy = AgressiveStrategy()

    bt: list[list[tuple[Pokemon, BattleStrategy]]] = [[(torchic, normal),
                                                       (bulba, heal)],
                                                      [(torchic, agressive),
                                                       (bulba, heal)],
                                                      [(primarina, normal),
                                                       (venu, heal),
                                                       (zoroark, agressive)]]
    for op in bt:
        try:
            battle(op)
        except Exception as e:
            print(e)


if (__name__ == "__main__"):
    main()
