import minigame
from consts import function


def get(player: "Player", item_1: str, item_2: str) -> str | bool | None:
    if (item_1, item_2) in registry:
        return registry[(item_1, item_2)](player)
    elif (item_2, item_1) in registry:
        return registry[(item_2, item_1)](player)
    return None

def two_way_in(item_1: str, item_2: str) -> bool:
    """Returns a boolean of whether there exists a recipe of the arguments in the registry"""
    return (item_1, item_2) in registry or (item_2, item_1) in registry

def simple(result: str) -> function:
    """Returns a function that returns result when passed any argument"""
    return lambda x: result

registry = {
    ("grass", "stick"): simple("firestarter"),
    ("rock", "rock"): minigame.knapping.run,
    ("stick", "axe_head"): simple("axe"),
    ("stick", "knife_head"): simple("knife"),
    ("stick", "spear_head"): simple("spear"),
    ("firestarter", "wood"): minigame.firestarter.run
}