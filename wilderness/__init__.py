from ui.output import PrintableObject
from wilderness.area import Area
from consts import function




class Wilderness(PrintableObject):
    def __init__(self, width: int = 0, height: int = 0):
        self.width = width
        self.height = height
        self.rooms = [[Area(self) for j in range(height)] for i in range(width)]
    
    def __str__(self) -> str:
        """When printing, print each room out in its row,
        printing newlines between each row"""
        to_return = ''
        for r in range(self.height):
            for c in range(self.width):
                to_return += (str(self.rooms[r][c]) + '   ')
            to_return += '\n'
        return to_return
    
    def __getitem__(self, coords: tuple) -> Area:
        """Causes wilderness[x, y] to return wilderness.rooms[x][y]
        Yes, this is actually how you're supposed to do it."""
        if type(coords) != tuple:
            raise TypeError(f"Expected tuple, got {type(coords)}.\n"
                            f"If you're getting this error, you likely entered the wrong number of arguments to "
                            f"wilderness[x, y].")
        return self.rooms[coords[0]][coords[1]]
    
    def __setitem__(self, coords, value: Area):
        """As above, but allows wilderness[x, y] = my_room
        equivalent to wilderness.rooms[x][y] = my_room"""
        if type(coords) != tuple:
            raise TypeError(f"Expected tuple, got {type(coords)}.\n"
                            f"If you're getting this error, you likely entered the wrong number of arguments to "
                            f"wilderness[x, y].")
        self.rooms[coords[0]][coords[1]] = value
