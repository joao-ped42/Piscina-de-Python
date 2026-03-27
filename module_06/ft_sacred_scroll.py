import alchemy
import alchemy.elements


def main() -> None:
    print("\nTesting direct module access:")
    print("alchemy.elements.create_fire(): "
          f"{alchemy.elements.create_fire()}")
    print("alchemy.elements.create_water(): "
          f"{alchemy.elements.create_water()}")
    print("alchemy.elements.create_earth(): "
          f"{alchemy.elements.create_earth()}")
    print("alchemy.elements.create_air(): "
          f"{alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by__init__.py):")
    try:
        print("alchemy.create_fire(): ", end="")
        print(f"{alchemy.create_fire()}")
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_water(): ", end="")
        print(f"{alchemy.create_water()}")
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_earth(): ", end="")
        print(f"{alchemy.create_earth()}")
    except AttributeError:
        print("AttributeError - not exposed")
    try:
        print("alchemy.create_air(): ", end="")
        print(f"{alchemy.create_air()}")
    except AttributeError:
        print("AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if (__name__ == "__main__"):
    print("\n=== Sacred Scroll Mastery ===")
    main()
