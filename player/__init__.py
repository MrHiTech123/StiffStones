import consts.player
from ui.output import PrintableObject

class Player(PrintableObject):
    def __init__(self, name: str, health=consts.player.health, inventory = None):
        self.name = name
        
        if inventory == None:
            inventory = {}
        self.inventory = inventory
    
    def __str__(self):
        to_return = ''
        to_return += self.name + '\n'
        to_return += 'Inventory:\n'
        for item, amount in self.inventory.items():
            to_return += f'\t{item}\t{amount}\n'
        return to_return
    
    def get_item(self, item: str, amount: int) -> None:
        if item not in self.inventory:
            self.inventory[item] = 0
        self.inventory[item] += amount
    
    def spend_item(self, item: str, amount: int) -> bool:
        if item not in self.inventory:
            return False
        if self.inventory[item] < amount:
            return False
        self.inventory[item] -= amount
        return True