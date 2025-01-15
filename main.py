from ui.output import SlowPrinter, test_effects
from wilderness import Wilderness
from player import Player
from recipe.actions import tutorial
import consts



def main_game():
    # Make new variables
    wilderness = Wilderness(consts.wilderness.width, consts.wilderness.height)
    name = SlowPrinter.input("Enter your name:\n")
    player = Player(wilderness, [consts.wilderness.width // 2, consts.wilderness.height // 2], name)
    
    while True:
        # Keep the player in the command loop until they exit.
        command = player.command_prompt()
        if command == 'exit':
            return


def main_menu():
    while True:
        option = SlowPrinter.input("Type 1 to play.\n"
                                   "Type 2 for a tutorial.\n"
                                   "Type 3 to confirm that your terminal is set up properly.\n")
        if option == '2':
            tutorial(None)
        elif option == '3':
            test_effects()
        elif option == '1':
            break
    
    main_game()


if __name__ == '__main__':
    main_menu()
