import minigame


def get(player, item_1, item_2):
    if (item_1, item_2) in recipes:
        return recipes[(item_1, item_2)](player)
    elif (item_2, item_1) in recipes:
        return recipes[(item_2, item_1)](player)
    return None

def simple(result: str):
    return lambda x: result

recipes = {
    ("rock", "rock"): minigame.knapping.run,
    ("stick", "stick"): simple("firestarter")
}