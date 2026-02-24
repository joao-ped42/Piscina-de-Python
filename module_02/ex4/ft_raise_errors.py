def check_plant(plant_name: str, water_level: int, sunlight_hours: int):
    if (not plant_name):
        raise ValueError("Plant name cannot be empty!")
    if (water_level > 10):
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if (water_level < 1):
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if (sunlight_hours > 12):
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too high (max 12)"
        )
    if (sunlight_hours < 2):
        raise ValueError(
            f"Sunlight hours {sunlight_hours} is too low (min 12)"
        )
    print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks() -> None:
    print("\nTesting good values...")
    check_plant("tomato", 8, 8)
    print("\nTesting empty plant name...")
    try:
        check_plant("", 8, 8)
    except ValueError as error:
        print(f"Error: {error}")
    print("\nTesting bad water level...")
    try:
        check_plant("tomato", 15, 8)
    except ValueError as error:
        print(f"Error: {error}")
    print("\nTesting bad sunlight hours...")
    try:
        check_plant("Tomato", 8, 0)
    except ValueError as error:
        print(f"Error: {error}")
    print("\nAll error raising tests completed!")


if (__name__ == "__main__"):
    print("=== Garden Plant Health Checker")
    test_plant_checks()
