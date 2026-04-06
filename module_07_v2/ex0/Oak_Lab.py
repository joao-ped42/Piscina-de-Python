from abc import ABC, abstractmethod
from ex0.Pokemon import Pokemon, Torchic, Blaziken, Popplio, Primarina


class PokemonFactory(ABC):
    @abstractmethod
    def create_base(self) -> Pokemon:
        ...

    @abstractmethod
    def create_evolved(self) -> Pokemon:
        ...


class FlameFactory(PokemonFactory):
    def create_base(self) -> Pokemon:
        return (Torchic())

    def create_evolved(self) -> Pokemon:
        return (Blaziken())


class AquaFactory(PokemonFactory):
    def create_base(self) -> Pokemon:
        return (Popplio())

    def create_evolved(self) -> Pokemon:
        return (Primarina())
