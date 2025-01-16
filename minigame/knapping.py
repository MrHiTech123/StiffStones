import recipe
from ui.input import linput
from ui.output import SlowPrinter, key, item, clear
from typing import Collection
from time import time
import consts


def knap_one_number(num: int) -> bool:
    """Knap one number in the pattern, returns whether the player succeeded for that number."""
    print(num)
    start = time()
    input()
    end = time()
    elapsed = end - start
    if abs(elapsed - num) < consts.knapping_threshold:
        return True
    else:
        if (elapsed > num):
            SlowPrinter.print("You hit too late!")
        else:
            SlowPrinter.print("You hit too early!")
        return False


def knapping_process(pattern: Collection[int]) -> bool:
    """Knap each number in succession"""
    for num in pattern:
        success = knap_one_number(num)
        if not success:
            return False
    return True


def gameplay(result: str) -> bool:
    """Get the pattern and then run the knapping minigame for it"""
    pattern = recipe.knapping.registry[result].pattern
    return knapping_process(pattern)


def run(player: "Player") -> bool:
    """Runs the knapping minigame, returns whether the player succeeded"""
    clear()
    SlowPrinter.print("Welcome to the knapping menu.")
    needs_help = SlowPrinter.linput(
        f"Type \"help\" for a knapping tutorial. Type \"exit\" to exit. Otherwise, press {key('Enter')} to continue.\n")
    
    if needs_help == 'help':
        SlowPrinter.print("To knap a stone tool, you must strike the stone precisely.\n"
                          "While knapping, a series of numbers will be printed on the screen.\n"
                          f"After each number, you must press the {key('Enter')} key "
                          "that many seconds after it appears.\n"
                          f"For example, if a \"3\" appears, you must wait 3 seconds and then press {key('Enter')}.\n"
                          f"This represents you hitting the rock precisely.\n"
                          f"After each hit, the next number will appear.")
    elif needs_help == "exit":
        player.get_item('rock', 2)
        return False
    
    # Select item
    SlowPrinter.print("What item would you like to knap? You may choose from:")
    for item_name in recipe.knapping.registry:
        SlowPrinter.print('\t' + item(item_name))
    SlowPrinter.print("Or type \"exit\" to exit")
    
    while True:
        chosen_item = linput()
        if chosen_item == 'exit':
            player.get_item('rock', 2)
            return False
        if chosen_item in recipe.knapping.registry:
            break
        SlowPrinter.print("Invalid item. Please try again.")
    
    # Do the minigame
    SlowPrinter.input(f"Knapping {item(chosen_item)}. Press {key('Enter')} to begin.")
    
    to_return = gameplay(chosen_item)
    
    # If they knapped successfully, give them the item.
    if to_return:
        SlowPrinter.print(f'Successfully knapped {item(chosen_item)}')
        player.get_item(chosen_item)
    else:
        SlowPrinter.print('Knapping failure')
    
    # The recipe calls for two rocks, since you're banging
    # one against the other and also that's how crafting recipes work in this.
    # However, the second rock is a catalyst, so give it back at the end.
    player.get_item('rock')
    
    return to_return
