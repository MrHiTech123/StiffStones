from typing import NamedTuple, Collection
from ui.output import SlowPrinter


# Oh that's right I forgot I used a NamedTuple here.
# That would probably make my other code considerably cleaner.
# Oops
class KnappingRecipe(NamedTuple):
    result: str
    # Used in the Knapping minigame to result in the item
    pattern: Collection[int]


# List of knapping recipes
recipes = [
    KnappingRecipe('spear_head', (6, 3, 2, 1)),
    KnappingRecipe('axe_head', (5, 5, 3, 3)),
    KnappingRecipe('knife_head', (2, 2, 2, 2))
]

registry = {}

# Make the registry from scratch
for recipe in recipes:
    registry[recipe.result] = recipe


# I honestly have no idea what is even happening here.
# I'm honestly not convinced it's actually used becuase how would that even work?
# There's a string being passed to a list index?

def get(result: str) -> tuple[int]:
    if result in recipes:
        return recipes[result]
    else:
        SlowPrinter.print(f"Error: No knapping recipe for {result}")
