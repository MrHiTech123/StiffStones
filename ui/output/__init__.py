from time import sleep


class PrintableObject():
    def __repr__(self) -> str:
        return self.__str__()


class SlowPrinter:
    @staticmethod
    def print(*args: object, sep: str = ' ', end: str = '\n') -> None:
        """Print something (or many things) slowly
        Works like the print function"""
        to_print = sep.join([str(x) for x in args]) + end
        for character in to_print:
            print(character, end='', flush=True)
            sleep(0.02)
    
    @staticmethod
    def input(__prompt: str) -> str:
        """As SlowPrinter.print, but also takes an input"""
        SlowPrinter.print(__prompt, end='')
        return input()


if __name__ == '__main__':
    SlowPrinter.print(1, 3, 'hello', end='\n')
    name = SlowPrinter.input('Hello, enter your name: ')
    
    SlowPrinter.print("Hello,", name)
