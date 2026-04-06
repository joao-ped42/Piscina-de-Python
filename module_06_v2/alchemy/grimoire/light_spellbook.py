def light_spell_allowed_ingredients() -> list[str]:
    return (["earth", "air", "fire", "water"])


def light_spell_record(spell_name: str, ingredients: str) -> str:
    try:
        from alchemy.grimoire.light_validation import validate_ingredients
    except ImportError:
        print("Failed to access grimorie")
    if (validate_ingredients(ingredients) == "VALID"):
        return (f"{spell_name} Recorded")
    return (f"{spell_name} Rejected")
