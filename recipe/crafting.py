import minigame
from consts import function
from typing import NamedTuple


class CraftingRecipe(NamedTuple):
    result: str
    result_function: function


def get_recipe(item_1: str, item_2: str) -> CraftingRecipe | None:
    if (item_1, item_2) in registry:
        return registry[(item_1, item_2)]
    elif (item_2, item_1) in registry:
        return registry[(item_2, item_1)]
    return None


def two_way_in(item_1: str, item_2: str) -> bool:
    """Returns a boolean of whether there exists a recipe of the arguments in the registry"""
    return get_recipe(item_1, item_2) != None


def get(player: "Player", item_1: str, item_2: str) -> str | bool | None:
    """Returns a """
    recipe = get_recipe(item_1, item_2)
    if recipe == None:
        return None
    return recipe.result_function(player)


def simple_function(result: str) -> function:
    """Returns a function that returns result when passed any argument"""
    return lambda x: result


def simple(result: str):
    return CraftingRecipe(result, simple_function(result))


registry = {
    ("grass", "stick"): simple("firestarter"),
    ("rock", "rock"): CraftingRecipe("knapping", minigame.knapping.run),
    ("stick", "axe_head"): simple("axe"),
    ("stick", "knife_head"): simple("knife"),
    ("stick", "spear_head"): simple("spear"),
    ("firestarter", "wood"): CraftingRecipe("campfire", minigame.firestarter.run)
}
