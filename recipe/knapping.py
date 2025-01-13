from typing import NamedTuple, Collection
from ui.output import SlowPrinter


class KnappingRecipe(NamedTuple):
    result: str
    # Used in the Knapping minigame to result in the item
    pattern: Collection[int]

recipes = [
    KnappingRecipe('spear_head', (6, 3, 2, 1)),
    KnappingRecipe('axe_head', (5, 5, 3, 3)),
    KnappingRecipe('knife_head', (2, 2, 2, 2))
]

registry = {}

for recipe in recipes:
    registry[recipe.result] = recipe

def get(result: str):
    if result in recipes:
        return recipes[result]
    else:
        SlowPrinter.print(f"Error: No knapping recipe for {result}")