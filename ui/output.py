from os import system
from time import sleep
import sty
import consts


class PrintableObject():
    def __repr__(self) -> str:
        return self.__str__()


def colored(text: object, r: int, g: int, b: int) -> str:
    """Prints text, colored rgb"""
    return sty.fg.rgb_call(r, g, b) + str(text) + sty.rs.fg


def gradient(text: str, r1: int, g1: int, b1: int, r2: int, g2: int, b2: int) -> str:
    """Prints text in a gradient. The starting color is (r1, g1, b1), and the ending color is (r2, g2, b2)."""
    to_return = ''
    # Get the step size
    size = len(text)
    
    # Get the step size for each color
    r_step = (r2 - r1) / size
    g_step = (g2 - g1) / size
    b_step = (b2 - b1) / size
    
    # Initialize the colors
    r = r1
    g = g1
    b = b1
    for character in text:
        # Add the escape code for the next color, and then add the character that will be that color
        to_return += sty.fg.rgb_call(int(r), int(g), int(b)) + character
        
        # Increment the colors for next character
        r += r_step
        g += g_step
        b += b_step
    # Reset the color at the end of the loop
    to_return += sty.rs.fg
    
    return to_return


def item(text: object) -> str:
    """Makes text light green indicates that the subject of the text is a feature."""
    return colored(text, 0, 255, 0)

def feature(text: object) -> str:
    """Makes text light blue, indicates that the subject of the text is a feature."""
    return colored(text, 0, 227, 255)

def key(text: object):
    """Makes text yellow, indicates that the subject of the text is a control"""
    return colored(text, 255, 255, 0)


class SlowPrinter:
    __printed_strings__: set[str] = set()
    @staticmethod
    def print(*args: object, sep: str = ' ', end: str = '\n') -> None:
        """Print something (or many things) slowly
        Works like the print function"""
        # Check if it's in the set. If it is, print it normally.
        to_print = sep.join([str(x) for x in args]) + end
        
        # If it's been slow-printed before, just print it normally the second time.
        if to_print in SlowPrinter.__printed_strings__:
            delay = consts.quick_print_delay
        else:
            # Add the string to printed_strings so that it knows not to slow-print it again.
            SlowPrinter.__printed_strings__.add(to_print)
            delay = consts.slow_print_delay
            
        
        for character in to_print:
            print(character, end='', flush=True)
            if consts.slow_print_at_all:
                sleep(delay)
            
    
    @staticmethod
    def input(__prompt: str) -> str:
        """As SlowPrinter.print, but also takes an input"""
        SlowPrinter.print(__prompt, end='')
        return input()
    
    @staticmethod
    def linput(__prompt: str):
        """As SlowPrinter.input, but returns the lowercase version"""
        return SlowPrinter.input(__prompt).lower()



def test_effects():
    """Confirms to the user that their terminal is set up properly"""
    system('clear')
    SlowPrinter.print(item('This text should be printed in Green.'))
    SlowPrinter.print(feature("This text should be printed in Light Blue."))
    SlowPrinter.print(key('This text should be printed in Yellow.'))
    
    SlowPrinter.print('This sentence should be overwritten.')
    sleep(1)
    print(consts.escape_code.start_prev_line, end='')
    SlowPrinter.print("If any of that didn't happen, your terminal environment is not set up properly for this game.")


def tutorial():
    system('clear')
    SlowPrinter.print(f"{item('Green')} text indicates items that can be stored in your inventory, such as {item('rocks')} and {item('sticks')}.\n"
                      f"{feature('Blue')} text indicates features that can be found in areas, such as {feature('trees')} and {feature('campfires')}.\n"
                      f"{key('Yellow')} indicates keys you can press on your keyboard, such as {key('Enter')}.")
    
    SlowPrinter.print('\n\n\n\n')
    
    SlowPrinter.print("The following commands can be used once you enter the game:")
    SlowPrinter.print(f"\tuse {item('[item 1]')} with {item('[item 2]')}")
    SlowPrinter.print("\t\tCombines two items from your inventory, usually crafting them into a third output "
                      "item.\n\t\tExample: use rock with rock"
                      "\n\t\tItems can be written in either order. \"use axe_head with stick\" will give the "
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
    
    