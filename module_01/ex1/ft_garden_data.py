class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age


if (__name__ == "__main__"):
    print("=== Garden Plant Registry ===")
    plants: list[Plant] = [Plant("Rose", 25, 30),
                           Plant("Sunflower", 80, 45),
                           Plant("Cactus", 15, 120)]
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
