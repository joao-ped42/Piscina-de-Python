class Plant:
    def __init__(self, name: str, height: int, plant_age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.plant_age: int = plant_age

    def grow(self) -> None:
        self.height = self.height + 1

    def age(self) -> None:
        self.plant_age = self.plant_age + 1

    def get_info(self) -> str:
        return (f"{self.name}: {self.height}cm, {self.plant_age} days old")


if (__name__ == "__main__"):
    rose: Plant = Plant("Rose", 25, 30)
    print("=== Day 1 ===")
    print(rose.get_info())
    for i in range(6):
        rose.grow()
        rose.age()
    print("=== Day 7 ===")
    print(rose.get_info())
    print("Growth this week: +6cm")
