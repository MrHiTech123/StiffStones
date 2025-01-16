import consts.player
import parsing
import recipe
from os import system
from ui.output import PrintableObject, SlowPrinter, item


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
        
        self.enter(wilderness[self.coordinates])
    
    def display_inventory(self):
        """Returns a string that displays the player's inventory."""
        to_return = 'Inventory:\n'
        for item_type, amount in self.inventory.items():
            to_return += f'\t{item(item_type)}\t{amount}\n'
        return to_return
    
    def __str__(self):
        to_return = ''
        to_return += self.name + '\n'
        to_return += f"Coords: {self.coordinates}\n"
        to_return += self.display_inventory()
        return to_return
    
    def get_current_area(self) -> "Area":
        """Gets the area of wilderness in which the player currently is"""
        return self.wilderness[self.coordinates]
    
    def get_item(self, item: str, amount: int = 1) -> None:
        """Puts one or more of an item in the player's inventory"""
        if item not in self.inventory:
            self.inventory[item] = 0
        self.inventory[item] += amount
    
    def spend_item(self, item: str, amount: int = 1) -> bool:
        """Removes one or more item in the player's inventory.
        Returns True if the item was successfully removed, and False
        if the player did not have the item, or did not have enough of it, prior to the removal.
        If the function returns False, the player's inventory stays how it was."""
        if item not in self.inventory:
            return False
        if self.inventory[item] < amount:
            return False
        self.inventory[item] -= amount
        if self.inventory[item] <= 0:
            self.inventory.pop(item)
        return True
    
    def enter(self, area: "Area"):
        """Enter an Area"""
        return area.be_entered_by(self)
    
    def move(self, direction: consts.Direction):
        """Move one space in one of the four cardinal directions"""
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
        
        self.enter(self.get_current_area())
    
    def do_action_command(self, action):
        """Do an "action" command"""
        if action not in recipe.actions.registry:
            return None
        return recipe.actions.registry[action](self)
    
    def do_usage_command(self, item, feature):
        """Do a command where an item is used on a feature"""
        SlowPrinter.print(f"Using {item} on {feature}")
        area = self.get_current_area()
        if item not in self.inventory:
            SlowPrinter.print("Error: Insufficient materials")
            return
        if feature not in area.features:
            SlowPrinter.print(f"Error: Area does not have {feature}")
            return
        result = recipe.usage.get(self, item, feature)
        # If there is no valid recipe
        if result == None:
            SlowPrinter.print(f"Error: {item} cannot be used on {feature}")
        # If the result is a string, add it to the player's inventory.
        # This is so done because some recipes have internal
        # reward item handlers and return booleans indicating their success.
        if isinstance(result, str):
            SlowPrinter.print(f"Recieved {result}")
            self.get_item(result)
    
    def do_item_combine_command(self, *items):
        """Do a command where two items are used on one another"""
        initial_inventory = self.inventory.copy()
        SlowPrinter.print(f"Using {items[0]} with {items[1]}")
        gots = self.spend_item(items[0]), self.spend_item(items[1])
        if not all(gots):
            SlowPrinter.print("Error: Insufficient materials")
            self.inventory = initial_inventory
            return
        result = recipe.crafting.get(self, *items)
        # If there is no valid recipe
        if result == None:
            SlowPrinter.print(f"Error: {items[0]} cannot be used with {items[1]}")
            self.inventory = initial_inventory
            return
        # If the result is a string, add it to the player's inventory.
        # This is so done because some recipes have internal
        # reward item handlers and return booleans indicating their success.
        if isinstance(result, str):
            SlowPrinter.print(f"Recieved {result}")
            self.get_item(result)
    
    def do_move_command(self, direction: consts.Direction):
        """Do a move command"""
        SlowPrinter.print(f"Moving {direction.value}")
        # Check if the current area allows the player to leave
        if self.get_current_area().leave(self, direction):
            self.move(direction)
    
    def do_unknown_command(self, command):
        """Tells the player that their command is unknown"""
        SlowPrinter.print(f"Error: Unknown command \"{command}\"")
        return
    
    def do_command(self, command):
        """Does a command"""
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
        """Shows some HUD information and prompts the player for a command"""
        SlowPrinter.print(self.name)
        SlowPrinter.print(self.display_inventory())
        SlowPrinter.print(self.get_current_area())
        SlowPrinter.print(self.get_current_area().display_features())
        
        command = SlowPrinter.linput("Enter command:\n")
        return self.do_command(command)
    
    def win_condition(self):
        """Determines if the player has won"""
        return 'cooked_meat' in self.inventory
    