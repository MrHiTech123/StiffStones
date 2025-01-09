from ui.output import SlowPrinter
from player import Player
from wilderness import Wilderness
from wilderness.area import Area, ClearingArea
import consts
import minigame

if __name__ == '__main__':
    
    # ui.output.test_effects()
    
    wilderness = Wilderness(consts.wilderness.width, consts.wilderness.height)
    wilderness[1, 1] = ClearingArea(wilderness)
    player = Player(wilderness, [1, 1], 'MrHiTech', consts.player.health)
    SlowPrinter.print(player)
    
    wilderness[1, 1].be_entered_by(player)
    
    SlowPrinter.print(player)
    

