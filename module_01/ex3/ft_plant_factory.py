class Plant:
    def __init__(self, name: str, height: int, plant_age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.plant_age: int = plant_age
        print(f"Creaed: {name} ({height}cm, {plant_age} days)")


if (__name__ == "__main__"):
    print("===  Plant Factory Output ===")
    plants: list[Plant] = [Plant("Rose", 25, 30),
                           Plant("Oak", 200, 365),
                           Plant("Cactus", 5, 90),
                           Plant("Sunflower", 80, 45),
                           Plant("Fern", 15, 120)]
    plant_num = 0
    for plant in plants:
        plant_num += 1
    print(f"\nTotal plants created: {plant_num}")
