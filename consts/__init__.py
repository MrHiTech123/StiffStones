from enum import StrEnum

function = type(lambda: None)


class Direction(StrEnum):
    NORTH = 'north'
    EAST = 'east'
    SOUTH = 'south'
    WEST = 'west'
