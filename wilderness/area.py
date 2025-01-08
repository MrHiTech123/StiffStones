from player import Player
from ui.output import PrintableObject
from random import randint


class Area(PrintableObject):
    def __init__(self, wilderness: 'Wilderness', f_name: str = "unnamed", f_inventory: dict[str: int] = None):
        self.name = f_name
        
        if f_inventory == None:
            f_inventory = {}
        self.inventory = f_inventory
    
    def north(self, player: Player):
        return True
    
    def east(self, player: Player):
        return True
    
    def south(self, player: Player):
        return True
    
    def west(self, player: Player):
        return True
    
    def enter(self, player: Player):
        for item, amount in self.inventory.items():
            player.get_item(item, amount)
        return True
    
    def interact(self, player: Player):
        return None
    
    def __str__(self):
        return f'Room {self.name}'
    
    def display(self):
        return self.name

class ClearingArea(Area):
    def __init__(self, wilderness: 'Wilderness'):
        super().__init__(wilderness, 'Clearing', ClearingArea.random_inventory())
    
    @staticmethod
    def random_inventory():
        return {
            'rock': randint(1, 4),
            'stick': randint(1, 3)
        }
        