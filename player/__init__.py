import consts.player
import parsing
import recipe
from ui.output import PrintableObject, SlowPrinter

class Player(PrintableObject):
    def __init__(self, wilderness: "Wilderness", coordinates: list[int, int], name: str = "NoName", health: int=consts.player.health, inventory: dict[str: int] = None):
        self.name = name
        self.wilderness = wilderness
        self.coordinates = coordinates
        
        self.health = health
        if inventory == None:
            inventory = {}
        self.inventory = inventory
        
        self.enter(wilderness[1, 1])
        
    def display_inventory(self):
        to_return = 'Inventory:\n'
        for item, amount in self.inventory.items():
            to_return += f'\t{item}\t{amount}\n'
        return to_return
    def __str__(self):
        to_return = ''
        to_return += self.name + '\n'
        to_return += self.display_inventory()
        return to_return
    
    def get_item(self, item: str, amount: int = 1) -> None:
        if item not in self.inventory:
            self.inventory[item] = 0
        self.inventory[item] += amount
    
    def spend_item(self, item: str, amount: int = 1) -> bool:
        if item not in self.inventory:
            return False
        if self.inventory[item] < amount:
            return False
        self.inventory[item] -= amount
        return True
    
    def enter(self, area: "Area"):
        return area.be_entered_by(self)
    
    def move(self, direction: consts.Direction):
        coordinate_adjust = consts.coordinate_adjusts[direction]
        for i in range(2):
            self.coordinates[i] += coordinate_adjust[i]
        self.enter(self.wilderness[self.coordinates])
    
    def do_usage_command(self, args):
        return
    def do_item_combine_command(self, *items):
        SlowPrinter.print(f"Combining {items[0]} with {items[1]}")
        gots = self.spend_item(items[0]), self.spend_item(items[1])
        if not all(gots):
            self.get_item(items[0])
            self.get_item(items[1])
            SlowPrinter.print("Error: Insufficient materials")
            SlowPrinter.print(self.display_inventory())
            return
        result = recipe.crafting.get(self, *items)
        if result == None:
            SlowPrinter.print(f"Error: {items[0]} cannot be combined with {items[1]}")
        
        if isinstance(result, str):
            self.get_item(result)
        return
    def do_move_command(self, direction: consts.Direction):
        SlowPrinter.print(f"Moving {direction.value}")
        self.move(direction)
    def do_unknown_command(self, command):
        SlowPrinter.print("Error: Unknown command")
        return
    def do_command(self, command):
        parsed_command = parsing.parse_command(command)
        command_type = parsed_command[0]
        command_args = parsed_command[1:]
        match command_type:
            case parsing.CommandClassification.USAGE:
                return self.do_usage_command(*command_args)
            case parsing.CommandClassification.ITEM_COMBINE:
                return self.do_item_combine_command(*command_args)
            case parsing.CommandClassification.MOVE:
                return self.do_move_command(*command_args)
            case _:
                return self.do_unknown_command(command)
                