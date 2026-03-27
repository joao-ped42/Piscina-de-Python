def validate_ingredients(ingredients: str) -> str:
    valids: list[str] = ["fire", "water", "earth", "air"]
    for element in valids:
        if element in ingredients:
            return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
