from ex0 import PokemonFactory
from ex1.Pokemon import Bulbasaur, Venusaur, Zorua, Zoroark


class HealingPokemonFactory(PokemonFactory):
    def create_base(self) -> Bulbasaur:
        return (Bulbasaur())

    def create_evolved(self) -> Venusaur:
        return (Venusaur())


class TransformPokemonFactory(PokemonFactory):
    def create_base(self) -> Zorua:
        return (Zorua())

    def create_evolved(self) -> Zoroark:
        return (Zoroark())
