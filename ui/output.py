from time import sleep
from termcolor import termcolor


class PrintableObject():
    def __repr__(self) -> str:
        return self.__str__()


def thing(text: object) -> str:
    """Makes text lime green
    Name is a reference to the API of the Patchouli Minecraft mod, which also uses
    "Thing" to mean, "turn this light green" """
    return termcolor.colored(text, 'light_green')


class SlowPrinter:
    @staticmethod
    def print(*args: object, sep: str = ' ', end: str = '\n') -> None:
        """Print something (or many things) slowly
        Works like the print function"""
        to_print = sep.join([str(x) for x in args]) + end
        for character in to_print:
            print(character, end='', flush=True)
            sleep(0.03)
    
    @staticmethod
    def input(__prompt: str) -> str:
        """As SlowPrinter.print, but also takes an input"""
        SlowPrinter.print(__prompt, end='')
        return input()
