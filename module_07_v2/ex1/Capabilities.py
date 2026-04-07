from abc import abstractmethod
from ex0.Pokemon import Pokemon


class HealCapability:
    @abstractmethod
    def heal(self, target: Pokemon) -> str:
        ...


class TransformCapability:
    @abstractmethod
    def transform(self, target: Pokemon) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...
