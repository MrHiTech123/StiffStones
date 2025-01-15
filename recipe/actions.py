import recipe.crafting
from ui.output import SlowPrinter, item, feature, key
from os import system


def simple(result: str):
    return lambda x: result

def display_available_recipes(player: "Player"):
    """Shows all crafting and feature """
    SlowPrinter.print("Available item interactions (\"with\"):")
    for item_1 in sorted(player.inventory):
        for item_2 in sorted(player.inventory):
            if (
                    (recipe.crafting.two_way_in(item_1, item_2) and item_1 <= item_2 and not 
                    (item_1 == item_2 and player.inventory[item_1] < 2))
            ):
                SlowPrinter.print('\t' + item(item_1) + ', ' + item(item_2))
    SlowPrinter.print()
    
    SlowPrinter.print("Available feature interactions (\"on\"):")
    for item_1 in player.inventory:
        for feat in player.get_current_area().features:
            if (item_1, feat) in recipe.usage.recipes:
                SlowPrinter.print('\t' + item(item_1) + ', ' + feature(feat))
    SlowPrinter.print()

def tutorial(player: "Player"):
    system('clear')
    SlowPrinter.print(f"{item('Green')} text indicates items that can be stored in your inventory, such as {item('rocks')} and {item('sticks')}.\n"
                      f"{feature('Blue')} text indicates features that can be found in areas, such as {feature('trees')} and {feature('campfires')}.\n"
                      f"{key('Yellow')} indicates keys you can press on your keyboard, such as {key('Enter')}.")
    
    SlowPrinter.print('\n\n\n\n')
    
    SlowPrinter.print("The following commands can be used once you enter the game:")
    SlowPrinter.print(f"\tuse {item('[item 1]')} with {item('[item 2]')}")
    SlowPrinter.print("\t\tCombines two items from your inventory, usually crafting them into a third output "
                      "item.\n\t\tExample: use rock with rock"
                      "\n\t\tItems can be written in either order. \"use axe_head with stick\" will give the \n\t\t"
                      "same result as \"use stick with axe_head\".")
    SlowPrinter.print()
    SlowPrinter.print(f"\tuse {item('[item]')} on {feature('[feature]')}")
    SlowPrinter.print("\t\tUses an item on a feature in the area you're currently in.")
    SlowPrinter.print("\t\tExample: \"use axe on tree\"")
    SlowPrinter.print("\t\tOrder DOES matter for this one. You are using the item on the feature, not the other way around.")
    SlowPrinter.print(f"\tRemember: if the second argument is an {item('item')}, the keyword is \"with\". If it's a {feature('feature')}, the keyword is \"on\".")
    SlowPrinter.print()
    SlowPrinter.print("\tmove [direction]")
    SlowPrinter.print("\t\tAllows you to move to an adjacent area. You may move North, South, East, or West.")
    SlowPrinter.print("\t\tExample: \"move north\"")
    SlowPrinter.print("\t\t\"up\", \"down\", \"left\", or \"right\" can also be used instead of the cardinal directions.")
    SlowPrinter.print()
    SlowPrinter.print("\t[command]")
    SlowPrinter.print("\t\tThese are miscellaneous commands that do not follow an explicit pattern.")
    SlowPrinter.print("\t\tThey are always one word and include:")
    SlowPrinter.print("\t\t\thelp - replays this tutorial")
    SlowPrinter.print("\t\t\texit - ends the program")
    SlowPrinter.print("\t\t\trecipes - gives a list of every recipe you can currently do")

actions = {
    'recipes': display_available_recipes,
    'exit': simple('exit'),
    'help': tutorial
}