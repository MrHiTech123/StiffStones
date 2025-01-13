from ui.output import SlowPrinter
from player import Player
from wilderness import Wilderness
from wilderness.area import Area, ClearingArea, ForestArea
import consts
import minigame

if __name__ == '__main__':
    
    
    # ui.output.test_effects()
    
    wilderness = Wilderness(consts.wilderness.width, consts.wilderness.height)
    wilderness[1, 1] = ClearingArea(wilderness)
    wilderness[1, 2] = ForestArea(wilderness)
    player = Player(wilderness, [1, 1], 'MrHiTech', consts.player.health)

    SlowPrinter.print(player)
    
    player.do_command("move east")
    player.do_command("use rock with rock")
    SlowPrinter.print(player)
    

