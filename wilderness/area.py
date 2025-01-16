import consts
from player import Player
from ui.output import PrintableObject, SlowPrinter, item, feature
from random import randint, choice
from typing import Type


def prune_empty_keys(to_be_pruned: dict[any: int]) -> dict[any: int]:
    """Removes any items from a dict that have a value of 0"""
    to_return = to_be_pruned.copy()
    for k, v in to_be_pruned.items():
        if v <= 0:
            to_return.pop(k)
    return to_return


class Area(PrintableObject):
    def __init__(self, wilderness: 'Wilderness', name: str = "unnamed", inventory: dict[str: int] = None,
                 features: dict[str] = None):
        self.name = name
        
        if inventory == None:
            inventory = {}
        if features == None:
            features = {}
        self.inventory = prune_empty_keys(inventory)
        self.features = prune_empty_keys(features)
    
    def north(self, player: Player):
        """Returns what happens when player moves north from this area"""
        return True
    
    def east(self, player: Player):
        """Returns what happens when player moves east from this area"""
        return True
    
    def south(self, player: Player):
        """Returns what happens when player moves south from this area"""
        return True
    
    def west(self, player: Player):
        """Returns what happens when player moves west from this area"""
        return True
    
    def leave(self, player: Player, direction: consts.Direction):
        """Returns what happens when player leaves the area"""
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
        """Displays the Area's inventory"""
        to_return = ''
        for item_type, amount in self.inventory.items():
            to_return += f'\t{item(item_type)}\t{amount}\n'
        return to_return
    
    def display_features(self):
        """Displays the Area's features"""
        to_return = ''
        for feature_type, amount in self.features.items():
            to_return += f"\t{feature(feature_type)}\t{amount}\n"
        return to_return
    
    def be_entered_by(self, player: Player):
        """What happens when player enters the Area"""
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
        """Returns what happens if the player interacts with the area; not currently used."""
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
        super().__init__(wilderness, 'Clearing', ClearingArea.random_inventory(), ClearingArea.random_features())
    
    def be_entered_by(self, player: Player):
        SlowPrinter.print("You enter a grassy clearing.")
        super().be_entered_by(player)
    
    @staticmethod
    def random_inventory():
        return {
            'rock': choice((0, 1, 1, 1)),
            'stick': choice((0, 1, 1, 1))
        }
    
    @staticmethod
    def random_features():
        return {
            "rabbit": choice((0, 0, 1)),
            "tall_grass": randint(0, 2),
            "tree": randint(0, 1)
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
            'stick': randint(1, 5)
        }
    
    @staticmethod
    def random_features():
        return {
            'tree': randint(4, 8)
        }


class RockyArea(Area):
    def __init__(self, wilderness: "Wilderness"):
        super().__init__(wilderness, 'Rocky', RockyArea.random_inventory())
    
    def be_entered_by(self, player: Player):
        SlowPrinter.print("You find yourself on a flat plane of stone that pokes through the surrounding dirt")
        super().be_entered_by(player)
    
    @staticmethod
    def random_inventory():
        return {
            'rock': randint(2, 5)
        }

# How likely each area type is to exist
area_weights = {
    ClearingArea: 3,
    ForestArea: 1,
    RockyArea: 1
}

# Create the list that is used to select random area types
area_types = []
for area, count in area_weights.items():
    for i in range(count):
        area_types.append(area)


def rand_area_type() -> Type:
    """Returns a random area type"""
    return choice(area_types)
