from enum import StrEnum
import consts.player, consts.escape_code, consts.wilderness

# This isn't a Python keyword for some reason
function = type(lambda: None)


# Enum for direction
class Direction(StrEnum):
    NORTH = 'north'
    EAST = 'east'
    SOUTH = 'south'
    WEST = 'west'


# Given a string, gives back the direction enum value corresponding to it.
direction_from_string: dict[str: Direction] = {
    'north': Direction.NORTH,
    'east': Direction.EAST,
    'south': Direction.SOUTH,
    'west': Direction.WEST,
    'up': Direction.NORTH,
    'right': Direction.EAST,
    'down': Direction.SOUTH,
    'left': Direction.WEST,
}

# Tells you how your coordinates are adjusted if you move in a given direction
coordinate_adjusts = {
    Direction.NORTH: (-1, 0),
    Direction.WEST: (0, -1),
    Direction.SOUTH: (1, 0),
    Direction.EAST: (0, 1)
}
# Convert campfire heat values out of 255, to degrees Celsius.
heat_conversion = 5 / 2

# Set to false for debug purposes
slow_print_at_all = False
# How long the slow print delay is the first time a string is printed
slow_print_delay = 0.03
# How long the print delay is for a string that has already been printed
quick_print_delay = 0.01
# How quickly you can press enter in succession before you're considered to be cheating.
cheating_threshold = 0.05

# How many seconds you're considered to be knapping accurately
knapping_threshold = 1
