class SecurePlant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.__height: int = 0
        self.__age: int = 0
        if (height >= 0):
            self.__height = height
        if (age >= 0):
            self.__age = age
        print(f"Plant created: {name}")

    def get_height(self) -> str:
        return (f"{self.__height}cm")

    def get_age(self) -> str:
        return (f"{self.__age} days")

    def set_height(self, newH: int) -> None:
        if (newH >= 0):
            self.__height = newH
            print(f"Height updated: {newH}cm [OK]")
        else:
            print(f"\nInvalid operation attempted: height {newH}cm [REJECTED]")
            print("Security: Negative height rejected\n")

    def set_age(self, newA: int) -> None:
        if (newA >= 0):
            self.__age = newA
            print(f"Age updated: {newA} days [OK]")
        else:
            print(f"Invalid operation attempted: age {newA}cm [REJECTED]")
            print("Security: Negative age rejected")


if (__name__ == "__main__"):
    r: SecurePlant = SecurePlant("Rose", 67, 911)
    r.set_height(25)
    r.set_age(30)
    r.set_height(-5)
    print(f"Current plant: {r.name} ({r.get_height()}cm, {r.get_age()} days)")
