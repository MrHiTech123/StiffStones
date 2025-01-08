from player import Player
from wilderness import Wilderness
from wilderness.area import Area, ClearingArea
import consts

if __name__ == '__main__':
    wilderness = Wilderness(2, 2)
    wilderness[1, 1] = ClearingArea(wilderness)
    player = Player('MrHiTech', consts.player.health)
    print(player)
    
    wilderness[1, 1].enter(player)
    
    print(player)
    

