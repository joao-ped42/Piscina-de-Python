class GardenError(Exception):
    """Basic Error"""
    pass


class PlantError(GardenError):
    """Plant Error"""
    pass


class WaterError(GardenError):
    """Water Error"""
    pass


class GardenManager:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.plants: dict[str] = {}
        self.water_level: int = 10

    class GardenAux:
        @staticmethod
        def ft_is_space(word: str) -> bool:
            for a in word:
                if (a not in "\t\n\v\f\r "):
                    return (False)
            return (True)

    def add_plant(self, plant_name: str, water_level: int) -> None:
        if ((not plant_name) or (self.GardenAux.ft_is_space(plant_name))):
            raise PlantError("Plant name cannot be empty!")
        self.plants[plant_name] = water_level
        print(f"Added {plant_name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        for plant in self.plants:
            if (self.water_level == 0):
                raise GardenError("Not enough water in tank")
            if (not plant):
                raise WaterError(f"Cannot water {plant} - Invalid plant!")
            self.water_level -= 1
            self.plants[plant] += 1
            print(f"Watering {plant} - success")

    def check_health(self) -> None:
        for plant in self.plants:
            if (self.plants[plant] > 10):
                raise PlantError(f"Error checking {plant}:"
                                 f" Water level {self.plants[plant]}"
                                 f" is too high (max 10)")
            print(f"{plant}: healthy (water {self.plants[plant]})")

    def check_water_tank(self) -> None:
        if (self.water_level < 10):
            raise GardenError("Not enough water in tank")
        print("Water tank is ok")


def test_garden_management() -> None:
    m1 = GardenManager("Roger")
    plants_to_add: list[str] = ["tomato", "lettuce", ""]
    print("\nAdding plants to garden...")
    i: int = 5
    for plant in plants_to_add:
        try:
            m1.add_plant(plant, i)
            i = i * 5
        except PlantError as error:
            print(f"Error adding plants: {error}")
    print("\nWatering plants...")
    try:
        m1.water_plants()
    except GardenError as error:
        print(f"Error watering plants: {error}")
    finally:
        print("Closing watering system (cleanup)")
    print("\nChecking plant health...")
    try:
        m1.check_health()
    except PlantError as error:
        print(error)
    print("\nTesting error recovery..")
    try:
        m1.check_water_tank()
    except GardenError as error:
        print(f"Caught GardenError: {error}")
        while (m1.water_level != 10):
            m1.water_level += 1
        print("System recovered and continuing...")
    print("\nGarden management system test complete!")


if (__name__ == "__main__"):
    print("=== Garden Management System ===")
    test_garden_management()
