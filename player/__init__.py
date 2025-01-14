import consts.player
import parsing
import recipe
from os import system
from ui.output import PrintableObject, SlowPrinter


class Player(PrintableObject):
    def __init__(self, wilderness: "Wilderness", coordinates: list[int, int], name: str = "NoName",
                 health: int = consts.player.health, inventory: dict[str: int] = None):
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
        to_return += f"Coords: {self.coordinates}\n"
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
        if self.inventory[item] <= 0:
            self.inventory.pop(item)
        return True
    
    def enter(self, area: "Area"):
        return area.be_entered_by(self)
    
    def move(self, direction: consts.Direction):
        coordinate_adjust = consts.coordinate_adjusts[direction]
        for i in range(2):
            self.coordinates[i] += coordinate_adjust[i]
        
        if self.coordinates[0] >= self.wilderness.width:
            SlowPrinter.print("Cannot go further South")
            self.coordinates[0] = self.wilderness.width - 1
        elif self.coordinates[0] < 0:
            SlowPrinter.print("Cannot go further North")
            self.coordinates[0] = 0
        if self.coordinates[1] >= self.wilderness.height:
            SlowPrinter.print("Cannot go further East")
            self.coordinates[1] = self.wilderness.height - 1
        elif self.coordinates[1] < 0:
            SlowPrinter.print("Cannot go further West")
            self.coordinates[1] = 0
        
        self.enter(self.wilderness[self.coordinates])
    
    def do_action_command(self, action):
        if action not in consts.actions:
            return None
        return consts.actions[action](self)
    
    def do_usage_command(self, item, feature):
        SlowPrinter.print(f"Using {item} on {feature}")
        area = self.wilderness[self.coordinates]
        if item not in self.inventory:
            SlowPrinter.print("Error: Insufficient materials")
            return
        if feature not in area.features:
            SlowPrinter.print(f"Error: Area does not have {feature}")
            return
        result = recipe.usage.get(self, item, feature)
        if result == None:
            SlowPrinter.print(f"Error: {item} cannot be used on {feature}")
        if isinstance(result, str):
            SlowPrinter.print(f"Recieved {result}")
            self.get_item(result)
    
    def do_item_combine_command(self, *items):
        initial_inventory = self.inventory.copy()
        SlowPrinter.print(f"Using {items[0]} with {items[1]}")
        gots = self.spend_item(items[0]), self.spend_item(items[1])
        if not all(gots):
            SlowPrinter.print("Error: Insufficient materials")
            self.inventory = initial_inventory
            return
        result = recipe.crafting.get(self, *items)
        if result == None:
            SlowPrinter.print(f"Error: {items[0]} cannot be used with {items[1]}")
            self.inventory = initial_inventory
            return
        if isinstance(result, str):
            SlowPrinter.print(f"Recieved {result}")
            self.get_item(result)
    
    def do_move_command(self, direction: consts.Direction):
        SlowPrinter.print(f"Moving {direction.value}")
        if self.wilderness[self.coordinates].move(self, direction):
            self.move(direction)
    
    def do_unknown_command(self, command):
        SlowPrinter.print(f"Error: Unknown command \"{command}\"")
        return
    
    def do_command(self, command):
        parsed_command = parsing.parse_command(command)
        command_type = parsed_command[0]
        command_args = parsed_command[1:]
        match command_type:
            case parsing.CommandClassification.ACTION:
                return self.do_action_command(command)
            case parsing.CommandClassification.USAGE:
                return self.do_usage_command(*command_args)
            case parsing.CommandClassification.ITEM_COMBINE:
                return self.do_item_combine_command(*command_args)
            case parsing.CommandClassification.MOVE:
                return self.do_move_command(*command_args)
            case _:
                return self.do_unknown_command(command)
    
    def command_prompt(self):
        SlowPrinter.print(self.name)
        SlowPrinter.print(self.display_inventory())
        
        command = SlowPrinter.linput("Enter command:\n")
        return self.do_command(command)
