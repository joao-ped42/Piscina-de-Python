from ex1.Pokemon import Bulbasaur, Venusaur, Zorua, Zoroark
import ex1


def main() -> None:
    print("Testing Pokemon with Healing Capability")
    print()

    heal_factory: ex1.HealingPokemonFactory = ex1.HealingPokemonFactory()
    bulba: Bulbasaur = heal_factory.create_base()
    venu: Venusaur = heal_factory.create_evolved()
    print(bulba.describe())
    print(bulba.attack())
    print(bulba.heal(bulba))
    print()
    print(venu.describe())
    print(venu.attack())
    print(venu.heal(bulba))
    print()

    print("Testing Pokemon with Transform Capability")
    print()

    trans_factory: ex1.TransformPokemonFactory = ex1.TransformPokemonFactory()
    zorua: Zorua = trans_factory.create_base()
    zoroark: Zoroark = trans_factory.create_evolved()
    print(zorua.describe())
    print(zorua.attack())
    print(zorua.transform(bulba))
    print(zorua.attack())
    print(zorua.revert())
    print()
    print(zoroark.describe())
    print(zoroark.attack())
    print(zoroark.transform(venu))
    print(zoroark.attack())
    print(zoroark.revert())


if (__name__ == "__main__"):
    main()
