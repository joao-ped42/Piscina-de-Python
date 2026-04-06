from alchemy.grimoire.dark_validation import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    return (["bats", "frogs", "arsenic", "eyeball"])


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    validation: str = validate_ingredients(ingredients)
    if (validation == "VALID"):
        return (f"Spell recorded: {spell_name} ({ingredients} - {validation})")
    return (f"Spell rejected: {spell_name} ({ingredients} - {validation})")
