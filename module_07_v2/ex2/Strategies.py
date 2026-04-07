from abc import ABC, abstractmethod
from ex0 import Pokemon
from ex1 import HealCapability, TransformCapability
from typing import cast


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, poke: Pokemon) -> bool:
        ...

    @abstractmethod
    def act(self, pokemon: Pokemon, target: Pokemon) -> None:
        ...


class NormalStrategy(BattleStrategy):
    def is_valid(self, poke: Pokemon) -> bool:
        return (True)

    def act(self, pokemon: Pokemon, target: Pokemon) -> None:
        target
        print(pokemon.attack())


class AgressiveStrategy(BattleStrategy):
    def is_valid(self, poke: Pokemon) -> bool:
        if (isinstance(poke, TransformCapability)):
            return (True)
        return (False)

    def act(self, pokemon: Pokemon, target: Pokemon) -> None:
        if (self.is_valid(pokemon)):
            poke_copy = cast(TransformCapability, pokemon)
            print(poke_copy.transform(target))
            print(pokemon.attack())
            print(poke_copy.revert())
        else:
            raise ValueError(f"Invalid Pokemon {pokemon.name} "
                             "for this agressive strategy")


class DefensiveStrategy(BattleStrategy):
    def is_valid(self, poke: Pokemon) -> bool:
        if (isinstance(poke, HealCapability)):
            return (True)
        return (False)

    def act(self, pokemon: Pokemon, target: Pokemon) -> None:
        if (self.is_valid(pokemon)):
            poke_copy = cast(HealCapability, pokemon)
            print(pokemon.attack())
            print(poke_copy.heal(pokemon))
        else:
            raise ValueError(f"Invalid Pokemon {pokemon.name} "
                             "for this defensive strategy")
