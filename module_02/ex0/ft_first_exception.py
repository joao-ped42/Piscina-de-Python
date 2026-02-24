def check_temperature(temp_str: str):
    print(f"\nTesting temperature: {temp_str}")
    try:
        temp_int = int(temp_str)
        if (0 <= temp_int <= 40):
            print(f"Temperature {temp_int}°C is perfect for plants!")
            return (temp_int)
        if (temp_int < 0):
            print(f"Error: {temp_int}°C is too cold for plants (min 0°C)")
        else:
            print(f"Error: {temp_int}°C is too hot for plants")
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")
    print("\nAll tests completed - program didn't crash")


if (__name__ == "__main__"):
    test_temperature_input()
