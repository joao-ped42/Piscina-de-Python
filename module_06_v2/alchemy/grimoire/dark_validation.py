from alchemy.grimoire.dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    for ingredient in dark_spell_allowed_ingredients():
        if (ingredient in ingredients.lower()):
            return ("VALID")
    return ("INVALID")
