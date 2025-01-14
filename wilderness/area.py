import consts
from player import Player
from ui.output import PrintableObject, SlowPrinter, item, feature
from random import randint, choice


class Area(PrintableObject):
    def __init__(self, wilderness: 'Wilderness', name: str = "unnamed", inventory: dict[str: int] = None,
                 features: dict[str] = None):
        self.name = name
        
        if inventory == None:
            inventory = {}
        if features == None:
            features = {}
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
    
    def move(self, player: Player, direction: consts.Direction):
        match direction:
            case consts.Direction.NORTH:
                return self.north(player)
            case consts.Direction.EAST:
                return self.east(player)
            case consts.Direction.SOUTH:
                return self.south(player)
            case consts.Direction.WEST:
                return self.west(player)
    
    def display_inventory(self):
        to_return = ''
        for item_type, amount in self.inventory.items():
            to_return += f'\t{item(item_type)}\t{amount}\n'
        return to_return
    
    def display_features(self):
        to_return = ''
        for feature_type, amount in self.features.items():
            to_return += f"\t{feature(feature_type)}\t{amount}\n"
        return to_return
        
    
    def be_entered_by(self, player: Player):
        if self.inventory:
            SlowPrinter.print("This area contains the following items, which you pick up:")
            SlowPrinter.print(self.display_inventory())
            for item, amount in self.inventory.items():
                player.get_item(item, amount)
        self.inventory.clear()
        if self.features:
            SlowPrinter.print("The area also contains the following features with which you can interact:")
            SlowPrinter.print(self.display_features())
        
        return True
    
    def interact(self, player: Player):
        return None
    
    def __str__(self):
        return f'{self.name} Area'
    
    def display(self):
        return self.name
    
    def add_feature(self, feature):
        """Adds a feature to an area"""
        if feature in self.features:
            self.features[feature] += 1
        else:
            self.features[feature] = 1
    
    def remove_feature(self, feature):
        """Removes a feature from an area"""
        if feature not in self.features:
            return False
        self.features[feature] -= 1
        if self.features[feature] <= 0:
            self.features.pop(feature)
        return True


class ClearingArea(Area):
    def __init__(self, wilderness: 'Wilderness'):
        super().__init__(wilderness, 'Clearing', ClearingArea.random_inventory())
    
    def be_entered_by(self, player: Player):
        SlowPrinter.print("You enter a grassy clearing.")
        super().be_entered_by(player)
    
    @staticmethod
    def random_inventory():
        return {
            'rock': randint(1, 4),
            'stick': randint(1, 3)
        }


class ForestArea(Area):
    def __init__(self, wilderness: 'Wilderness'):
        super().__init__(wilderness, 'Forest', ForestArea.random_inventory(), ForestArea.random_features())
    
    def be_entered_by(self, player: Player):
        SlowPrinter.print("You enter a forest.")
        super().be_entered_by(player)
    
    @staticmethod
    def random_inventory():
        return {
            'stick': randint(1, 10)
        }
    
    @staticmethod
    def random_features():
        return {
            'tree': randint(1, 4)
        }


room_types = [ClearingArea, ForestArea]


def rand_area_type():
    return choice(room_types)
