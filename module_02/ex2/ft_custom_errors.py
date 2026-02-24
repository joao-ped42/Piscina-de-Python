class GardenError(Exception):
    """Basic Error"""
    pass


class PlantError(GardenError):
    """Plant Error"""
    pass


class WaterError(GardenError):
    """Water Error"""
    pass


def error_test(condition: str) -> None:
    if (condition == "wilting"):
        raise PlantError("The tomato plant is wilting!")
    else:
        raise WaterError("Not enough water in the tank!")


def error_showcase() -> None:
    print("=== Custom Garden Errors Demo ===")
    try:
        print("\nTesting PlantError...")
        error_test("wilting")
    except PlantError as error:
        print(f"Caught PlantError: {error}")
    try:
        print("\nTesting WaterError...")
        error_test("water")
    except WaterError as error:
        print(f"Caught WaterError: {error}")
    print("\nTesting catching all garden errors...")
    try:
        error_test("wilting")
    except GardenError as error:
        print(f"Caught a garden error: {error}")
    try:
        error_test("water")
    except GardenError as error:
        print(f"Caught a garden error: {error}")
    print("\nAll custom error types work correctly!")


if (__name__ == "__main__"):
    error_showcase()
