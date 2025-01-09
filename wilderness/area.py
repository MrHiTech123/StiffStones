from player import Player
from ui.output import PrintableObject, SlowPrinter
from random import randint


class Area(PrintableObject):
    def __init__(self, wilderness: 'Wilderness', name: str = "unnamed", inventory: dict[str: int] = None, features: set[str] = None):
        self.name = name
        
        if inventory == None:
            inventory = {}
        if features == None:
            features = set()
        self.inventory = inventory
        self.features = features
    
    def north(self, player: Player):
        return True
    
    def east(self, player: Player):
        return True
    
    def south(self, player: Player):
        return True
    
    def west(self, player: Player):
        return True
    
    def be_entered_by(self, player: Player):
        if self.inventory:
            SlowPrinter.print("This area contains the following items, which you pick up:")
            for item, amount in self.inventory.items():
                SlowPrinter.print(f"\t{item}\t{amount}")
                player.get_item(item, amount)
        self.inventory.clear()
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

class ForestArea(Area):
    def __init__(self, wilderness: 'Wilderness'):
        super().__init__(wilderness, 'Forest', ForestArea.random_inventory())
    
    @staticmethod
    def random_inventory():
        return {
            'stick': randint(1, 10)
        }
    
    