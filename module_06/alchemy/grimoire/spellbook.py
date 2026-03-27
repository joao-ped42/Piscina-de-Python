def record_spell(spell_name: str, ingredients: str) -> str:
    try:
        from .validator import validate_ingredients
    except Exception:
        return ("Couldn't import validate_ingridients()")
    validation = validate_ingredients(ingredients)
    result = validation.split(" - ")[1]
    if (result == "VALID"):
        return (f"Spell recorded: {spell_name} ({validation})")
    return (f"Spell rejected: {spell_name} ({validation})")
