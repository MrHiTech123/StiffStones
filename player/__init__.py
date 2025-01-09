import consts.player
from ui.output import PrintableObject

class Player(PrintableObject):
    def __init__(self, wilderness: "Wilderness", coordinates: list[int, int], name: str = "NoName", health: int=consts.player.health, inventory: dict[str: int] = None):
        self.name = name
        self.wilderness = wilderness
        self.coordinates = coordinates
        
        self.health = health
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
    
    def enter(self, area: "Area"):
        return area.be_entered_by(self)
        