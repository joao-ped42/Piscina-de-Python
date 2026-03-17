class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = 0
        if (height >= 0):
            self.height: int = height
        self.age: int = age

    def __str__(self) -> str:
        return (f"{self.name}")

    def get_info(self) -> str:
        return (f"{self.name}: {self.height}cm")

    def grow(self) -> None:
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color: str = color

    def get_info(self) -> None:
        return (f"{self.name}: {self.height}cm, "
                f"{self.color} flowers (blooming)")


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int,
                 color: str, prize_points: int) -> None:
        super().__init__(name, height, age, color)
        self.prize_points: int = prize_points

    def get_info(self) -> None:
        return (f"{self.name}: {self.height}cm, "
                f"{self.color} flowers (blooming), "
                f"Prize Points: {self.prize_points}")


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner: str = owner
        self.plants: list[Plant] = []
        self.plant_types: dict = {"plant": 0,
                                  "floweringplant": 0,
                                  "prizeflower": 0}

    @classmethod
    def found_garden(cls, owner_name: str):
        return (cls(owner_name))


class GardenManager:
    def __init__(self, manager_name: str) -> None:
        self.manager_name: str = manager_name
        self.gardens_managed: list[Garden] = []
        self.total_growth: int = 0

    def create_garden_network(self, new_garden: Garden) -> None:
        self.gardens_managed.append(new_garden)

    @staticmethod
    def add_plants(garden: Garden, new_plant: Plant) -> None:
        garden.plants.append(new_plant)
        print(f"Added {new_plant.name} to {garden.owner} garden")
        if (new_plant.__class__ is Plant):
            garden.plant_types["plant"] += 1
        elif (new_plant.__class__ is FloweringPlant):
            garden.plant_types["floweringplant"] += 1
        else:
            garden.plant_types["prizeflower"] += 1

    class GardenStats:
        @staticmethod
        def grow_all(manager: "GardenManager",
                     plants: list[Plant]) -> None:
            print(f"\n{manager.manager_name} is helping all plants grow...")
            for plant in plants:
                plant.grow()
                manager.total_growth += 1

        @staticmethod
        def get_points(types: dict) -> int:
            total_points: int = 0
            for plant in types:
                quantity: int = types[plant]
                if (plant == "plant"):
                    total_points = total_points + (quantity * 10)
                elif (plant == "floweringplant"):
                    total_points = total_points + (quantity * 20)
                else:
                    total_points = total_points + (quantity * 40)
            return (total_points)

        @staticmethod
        def lst_len(lst: list) -> int:
            i: int = 0
            for obj in lst:
                i += 1
            return (i)

        @staticmethod
        def height_validation(plant: Plant) -> bool:
            if (plant.height < 0):
                return (False)
            return (True)

    def report(self, reported: Garden) -> None:
        print(f"\n=== {reported.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in reported.plants:
            print(f"{plant.get_info()}")
        print(f"\nPlants added: "
              f"{self.GardenStats.lst_len(reported.plants)}, "
              f"Total growth: {self.total_growth}cm")
        print(f"Plant Types: {reported.plant_types["plant"]} regular, "
              f"{reported.plant_types["floweringplant"]} flowering, "
              f"{reported.plant_types["prizeflower"]} prize flowers")


def main() -> None:
    manager = GardenManager("Roger")
    alice_plants: list[Plant] = [Plant("Oak Tree", 100, 30),
                                 FloweringPlant("Rose", 25, 100, "red"),
                                 PrizeFlower("Sunflower", 50, 30, "yellow", 1)]
    bob_plants: list[Plant] = [Plant("Oak Tree", 120, 50),
                               Plant("Olive Tree", 150, 80),
                               Plant("Apple Tree", 135, 90)]
    alice_garden: Garden = Garden("Alice")
    bob_garden: Garden = Garden.found_garden("Bob")
    manager.create_garden_network(alice_garden)
    manager.create_garden_network(bob_garden)
    for plant in alice_plants:
        manager.add_plants(alice_garden, plant)
    for plant in bob_plants:
        manager.add_plants(bob_garden, plant)
    manager.GardenStats.grow_all(manager, alice_garden.plants)
    manager.report(alice_garden)
    print(f"\nHeight validation test: "
          f"{manager.GardenStats.height_validation(Plant("teste", -1, 1))}")
    print(f"Garden scores - Alice: "
          f"{manager.GardenStats.get_points(alice_garden.plant_types)} "
          f"Bob: "
          f"{manager.GardenStats.get_points(bob_garden.plant_types)}")
    print(f"Total gardens managed: "
          f"{manager.GardenStats.lst_len(manager.gardens_managed)}")


if (__name__ == "__main__"):
    print("===  Garden Management System Demo  ===\n")
    main()
