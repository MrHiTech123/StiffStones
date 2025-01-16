import recipe.crafting
from consts import function
from ui.output import SlowPrinter, item, feature, key
from os import system


def simple(result: str) -> function:
    """Returns a lambda function that returns the result when given any argument"""
    return lambda x: result


def display_available_recipes(player: "Player"):
    """Shows all crafting and feature recipes that the entered player can do"""
    SlowPrinter.print("Available item interactions (\"with\"):")
    # Iterate through the player's inventory twice
    for item_1 in sorted(player.inventory):
        for item_2 in sorted(player.inventory):
            # If:
            #   There exists a recipe with both items, and:
            #   The items are in alphabetical order (done to prevent repeat symmetrical recipes) and:
            #   The player has enough of the item if they're both the same
            if (
                    (recipe.crafting.two_way_in(item_1, item_2) and item_1 <= item_2 and not
                    (item_1 == item_2 and player.inventory[item_1] < 2))
            ):
                # Print the recipe
                SlowPrinter.print('\t' + item(item_1) + ', ' + item(item_2))
    
    SlowPrinter.print()
    
    SlowPrinter.print("Available feature interactions (\"on\"):")
    # Iterate through the player's inventory and features in the current area
    for item_1 in sorted(player.inventory):
        for feat in player.get_current_area().features:
            # Print the combination if it has a recipe
            if (item_1, feat) in recipe.usage.registry:
                SlowPrinter.print('\t' + item(item_1) + ', ' + feature(feat))
    SlowPrinter.print()


def tutorial(player: "Player"):
    """Shows the player the tutorial"""
    system('clear')
    SlowPrinter.print(
        f"{item('Green')} text indicates items that can be stored in your inventory, such as {item('rocks')} and {item('sticks')}.\n"
        f"{feature('Blue')} text indicates features that can be found in areas, such as {feature('trees')} and {feature('campfires')}.\n"
        f"{key('Yellow')} indicates keys you can press on your keyboard, such as {key('Enter')}.")
    
    SlowPrinter.print('\n\n')
    
    SlowPrinter.print("The following commands can be used once you enter the game:")
    SlowPrinter.print(f"\tuse {item('[item 1]')} with {item('[item 2]')}")
    SlowPrinter.print("\t\tCombines two items from your inventory, usually crafting them into a third output "
                      "item.\n\t\tExample: \"use rock with rock\""
                      "\n\t\tItems can be written in either order. \"use axe_head with stick\" will give the \n\t\t\t"
                      "same result as \"use stick with axe_head\".")
    SlowPrinter.print()
    SlowPrinter.print(f"\tuse {item('[item]')} on {feature('[feature]')}")
    SlowPrinter.print("\t\tUses an item on a feature in the area you're currently in.")
    SlowPrinter.print("\t\tExample: \"use axe on tree\"")
    SlowPrinter.print(
        "\t\tOrder DOES matter for this one. You are using the item on the feature, not the other way around.")
    SlowPrinter.print(
        f"\tRemember: if the second argument is an {item('item')}, the keyword is \"with\". If it's a {feature('feature')}, the keyword is \"on\".")
    SlowPrinter.print()
    SlowPrinter.print("\tmove [direction]")
    SlowPrinter.print("\t\tAllows you to move to an adjacent area. You may move North, South, East, or West.")
    SlowPrinter.print("\t\tExample: \"move north\"")
    SlowPrinter.print(
        "\t\t\"up\", \"down\", \"left\", or \"right\" can also be used instead of the cardinal directions.")
    SlowPrinter.print()
    SlowPrinter.print("\t[command]")
    SlowPrinter.print("\t\tThese are miscellaneous commands that do not take arguments.")
    SlowPrinter.print("\t\tThey are always one word and include:")
    SlowPrinter.print("\t\t\thelp - replays this tutorial")
    SlowPrinter.print("\t\t\texit - ends the program")
    SlowPrinter.print("\t\t\trecipes - gives a list of every recipe you can currently do")
    
    SlowPrinter.print()
    SlowPrinter.print("Cook some meat to win the game!")
    SlowPrinter.print()

# Action "recipe" registry; a command of [key] results in function [value] being run on the player.
registry = {
    'recipes': display_available_recipes,
    'exit': simple('exit'),
    'help': tutorial
}
