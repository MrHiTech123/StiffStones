from typing import NamedTuple, Collection


class KnappingRecipe(NamedTuple):
    result: str
    # Used in the Knapping minigame to result in the item
    pattern: Collection[int]

recipes = [
    KnappingRecipe('spear_head', (6, 3, 2, 1)),
    KnappingRecipe('axe_head', (5, 5, 3, 3)),
    KnappingRecipe('knife_head', (1, 1, 1, 1))
]

registry = {}

for recipe in recipes:
    registry[recipe.result] = recipe
    
