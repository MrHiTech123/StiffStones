import recipe.crafting
from ui.output import tutorial, SlowPrinter, item, feature


def simple(result: str):
    return lambda x: result

def display_available_recipes(player: "Player"):
    """Shows all crafting and feature """
    SlowPrinter.print("Available item interactions:")
    for item_1 in player.inventory:
        for item_2 in player.inventory:
            if (
                    (recipe.crafting.two_way_in(item_1, item_2) and not 
                    (item_1 == item_2 and player.inventory[item_1] < 2))
            ):
                SlowPrinter.print('\t' + item(item_1) + ', ' + item(item_2))
    SlowPrinter.print()
    
    SlowPrinter.print("Available feature interactions:")
    for item_1 in player.inventory:
        for feat in player.get_current_area().features:
            if (item_1, feat) in recipe.usage.recipes:
                SlowPrinter.print('\t' + item(item_1) + ', ' + feature(feat))
    SlowPrinter.print()
            

actions = {
    'recipes': display_available_recipes,
    'exit': simple('exit'),
    'help': tutorial
}