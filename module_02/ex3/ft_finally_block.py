def water_plants(plant_list: list[str]) -> None:
    print("Opening watering systems")
    try:
        for plant in plant_list:
            if (plant is None):
                raise ValueError("Error: Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as error:
        print(error)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    plants_right = ["tomato", "lettuce", "carrots"]
    plants_wrong = ["tomato", None, "carrots"]
    print("\nTesting normal watering...")
    water_plants(plants_right)
    print("\nTesting with error...")
    water_plants(plants_wrong)
    print("\nCleanup always happens, even with errors!")


if (__name__ == "__main__"):
    print("=== Garden Watering System ===")
    test_watering_system()
