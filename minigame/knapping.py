import recipe
from ui.input import linput
from ui.output import SlowPrinter, key, item
from typing import Collection
from time import time
import consts
from os import system


def knap_one_number(num: int) -> bool:
    print(num)
    start = time()
    input()
    end = time()
    elapsed = end - start
    return abs(elapsed - num) < consts.knapping_threshold


def knapping_process(pattern: Collection[int]) -> bool:
    for num in pattern:
        success = knap_one_number(num)
        if not success:
            return False
    return True


def gameplay(result: str):
    pattern = recipe.knapping.registry[result].pattern
    return knapping_process(pattern)


def run(player) -> bool:
    system('clear')
    # TODO: Tutorial system
    SlowPrinter.print("To knap a stone tool, you must strike the stone precisely.\n"
                      "While knapping, a series of numbers will be printed on the screen.\n"
                      f"After each number, you must press the {key('Enter')} key "
                      "that many seconds after it appears.\n"
                      f"For example, if a \"3\" appears, you must wait 3 seconds and then press {key('Enter')}.\n"
                      f"This represents you hitting the rock precisely.\n"
                      f"After each hit, the next number will appear.")
    
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
    
    SlowPrinter.input(f"Knapping {chosen_item}. Press {item('Enter')} to begin.")
    
    to_return = gameplay(chosen_item)
    
    if to_return:
        SlowPrinter.print(f'Successfully knapped {chosen_item}')
        player.get_item(chosen_item)
    else:
        SlowPrinter.print('Knapping failure')
    
    player.get_item('rock')
    
    return to_return
