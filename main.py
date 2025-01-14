from ui.output import SlowPrinter, test_effects, tutorial
from wilderness import Wilderness
from player import Player
import consts


def main_game():
    wilderness = Wilderness(consts.wilderness.width, consts.wilderness.height)
    name = SlowPrinter.input("Enter your name:\n")
    player = Player(wilderness, [consts.wilderness.width // 2, consts.wilderness.height // 2], name)
    
    while True:
        command = player.command_prompt()
        if command == 'exit':
            return


def main_menu():
    while True:
        option = SlowPrinter.input("Type 1 to play.\n"
                                   "Type 2 for a tutorial.\n"
                                   "Type 3 to confirm that your terminal is set up properly.\n")
        if option == '2':
            tutorial()
        elif option == '3':
            test_effects()
        elif option == '1':
            break
    
    main_game()


if __name__ == '__main__':
    main_menu()
