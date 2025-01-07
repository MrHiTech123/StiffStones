from time import sleep
import sty
import consts


class PrintableObject():
    def __repr__(self) -> str:
        return self.__str__()


def colored(text: str, r: int, g: int, b: int) -> str:
    return sty.fg.rgb_call(r, g, b) + text + sty.rs.fg


def gradient(text: str, r1: int, g1: int, b1: int, r2: int, g2: int, b2: int) -> str:
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


def thing(text: object) -> str:
    """Makes text lime green
    Name is a reference to the API of the Patchouli Minecraft mod, which also uses
    "Thing" to mean, "turn this light green" """
    return colored(text, 0, 255, 0)


def key(text: object):
    """Makes text light blue, indicates that the subject of the text is a control"""
    return colored(text, 255, 255, 0)


class SlowPrinter:
    @staticmethod
    def print(*args: object, sep: str = ' ', end: str = '\n') -> None:
        """Print something (or many things) slowly
        Works like the print function"""
        to_print = sep.join([str(x) for x in args]) + end
        for character in to_print:
            print(character, end='', flush=True)
            if consts.slow_print_at_all:
                sleep(consts.slow_print_delay)
    
    @staticmethod
    def input(__prompt: str) -> str:
        """As SlowPrinter.print, but also takes an input"""
        SlowPrinter.print(__prompt, end='')
        return input()
    
    @staticmethod
    def linput(__prompt: str):
        return SlowPrinter.input(__prompt).lower()


def test_green():
    SlowPrinter.print(
        f"Objects you can interact with will be typed in {thing('Green')}.\n"
        f"Keys you can press will be typed in {key('Blue')}."
        f"If \"Green\" and \"Blue\" are not written in their respective colors,"
        f"something is wrong with your terminal environment.")
