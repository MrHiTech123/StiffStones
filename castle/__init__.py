from ui.output import PrintableObject
from consts import function


class Room(PrintableObject):
    def __init__(self,
                 f_name: str = "unnamed",
                 f_north: function = lambda: True,
                 f_south: function = lambda: True,
                 f_east: function = lambda: True,
                 f_west: function = lambda: True,
                 f_interact: function = lambda: None):
        self.name = f_name
        self.north = f_north
        self.south = f_south
        self.east = f_east
        self.west = f_west
        self.interact = f_interact
    
    def __str__(self):
        return f'Room {self.name}'
    
    def display(self):
        return self.name


class Castle(PrintableObject):
    def __init__(self, width: int = 0, height: int = 0):
        self.width = width
        self.height = height
        self.rooms = [[Room() for j in range(height)] for i in range(width)]
    
    def __str__(self) -> str:
        """When printing, print each room out in its row,
        printing newlines between each row"""
        to_return = ''
        for r in range(self.height):
            for c in range(self.width):
                to_return += (str(self.rooms[r][c]) + '   ')
            to_return += '\n'
        return to_return
    
    def __getitem__(self, coords: tuple) -> Room:
        """Causes castle[x, y] to return castle.rooms[x][y]
        Yes, this is actually how you're supposed to do it."""
        if type(coords) != tuple:
            raise TypeError(f"Expected tuple, got {type(coords)}.\n"
                            f"If you're getting this error, you likely entered the wrong number of arguments to "
                            f"castle[x, y].")
        return self.rooms[coords[0]][coords[1]]
    
    def __setitem__(self, coords, value: Room):
        """As above, but allows castle[x, y] = my_room
        equivalent to castle.rooms[x][y] = my_room"""
        if type(coords) != tuple:
            raise TypeError(f"Expected tuple, got {type(coords)}.\n"
                            f"If you're getting this error, you likely entered the wrong number of arguments to "
                            f"castle[x, y].")
        self.rooms[coords[0]][coords[1]] = value
