from ui.output import SlowPrinter, test_effects
from wilderness import Wilderness
from player import Player
import consts

def main_game():
    wilderness = Wilderness(consts.wilderness.width, consts.wilderness.height)
    player = Player(wilderness, health=consts.player.health)
    
    while True:
        player.command_prompt()
        
    
    
    

def main_menu():
    
    while True:
        option = SlowPrinter.input("Type 1 to play.\nType 2 to confirm that your terminal is set up properly.")
        if option == '2':
            test_effects()
        elif option == '1':
            break
        
    
    
    main_game()
    
    
    