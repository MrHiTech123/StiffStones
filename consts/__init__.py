from enum import StrEnum

function = type(lambda: None)


class Direction(StrEnum):
    NORTH = 'north'
    EAST = 'east'
    SOUTH = 'south'
    WEST = 'west'

heat_conversion = 5/2

slow_print_at_all = True
slow_print_delay = 0.03
cheating_threshold = 0.05
