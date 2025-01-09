from enum import StrEnum
import consts.player, consts.escape_code, consts.wilderness

function = type(lambda: None)


class Direction(StrEnum):
    NORTH = 'north'
    EAST = 'east'
    SOUTH = 'south'
    WEST = 'west'

coordinate_adjusts = {
    Direction.NORTH: (-1, 0),
    Direction.WEST: (0, -1),
    Direction.SOUTH: (1, 0),
    Direction.EAST: (0, 1)
}
heat_conversion = 5/2

slow_print_at_all = True
slow_print_delay = 0.03
quick_print_delay = 0.01
cheating_threshold = 0.05

knapping_threshold = 1