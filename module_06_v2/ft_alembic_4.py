import alchemy


if (__name__ == "__main__"):
    print("=== Alembic 4 ===")
    print("Accessing the alchemy module using 'import alchemy'")
    print(f"Testing create_air: {alchemy.create_air()}")
    print(f"Testing the hidden create_earth: {alchemy.create_earth()}")
