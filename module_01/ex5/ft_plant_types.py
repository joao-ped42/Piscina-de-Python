class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def get_info(self) -> str:
        return (f"\n{self.name} (Flower): {self.height}cm, "
                f"{self.age} days, {self.color} color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully")


class Tree(Plant):
    def __init__(self, name: str, height: int,
                 age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def get_info(self) -> str:
        return (f"\n{self.name} (Tree): {self.height}cm, "
                f"{self.age} days, {self.trunk_diameter} diameter")

    def produce_shade(self) -> None:
        shade: int = int(((self.height / 100) ** 2) * 3.14)
        print(f"{self.name} provides {shade} square meters of shade")


class Vegetable(Plant):
    def __init__(self, name: str, height: str, age: str,
                 harvest_season: str, nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value

    def get_info(self) -> str:
        return (f"\n{self.name} (Tree): {self.height}cm, "
                f"{self.age} days, {self.harvest_season}")

    def get_nutritional(self) -> str:
        return (f"{self.name} is rich in {self.nutritional_value}")


if (__name__ == "__main__"):
    print("=== Garden Plant Types ===")
    rose = Flower("Rose", 25, 30, "red")
    oak = Tree("Oak", 500, 1825, 50)
    tomato = Vegetable("Tomato", 80, 90, "summer harvest", "vitamin C")
    print(rose.get_info())
    rose.bloom()
    print(oak.get_info())
    oak.produce_shade()
    print(tomato.get_info())
    print(tomato.get_nutritional())
