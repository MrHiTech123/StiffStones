from enum import Enum

import consts
import recipe.actions
from consts import Direction
import re


# Enum for the different ways to classify a command
class CommandClassification(Enum):
    UNKNOWN = -1
    MOVE = 0
    ACTION = 1
    USAGE = 2
    ITEM_COMBINE = 3


def classify_command(command: str) -> CommandClassification:
    """Classifies a command into one of many categories so that it can be later parsed"""
    # re.match(str) -> if it matches the entered regex:
    if command in recipe.actions.registry:
        return CommandClassification.ACTION
    elif re.match('use \\S+ on \\S+', command):
        return CommandClassification.USAGE
    elif re.match('use \\S+ with \\S+', command):
        return CommandClassification.ITEM_COMBINE
    elif re.match('move \\S+', command):
        return CommandClassification.MOVE
    else:
        return CommandClassification.UNKNOWN


def parse_usage_command(command: str) -> tuple:
    """Gives the item and target of a usage command.
    Each parse_whatever_command function also returns its
    classification as the first element of the tuple, for later reference."""
    words = command.split()
    return CommandClassification.USAGE, words[1], words[3]


def parse_item_combine_command(command: str) -> tuple:
    """Returns the two items being combined by an item combine command"""
    words = command.split()
    return CommandClassification.ITEM_COMBINE, words[1], words[3]


def parse_move_command(command: str) -> tuple:
    """Returns a movement classification and the direction in which to move, unless
    it's not a real direction, in which case just consider it an unknown command."""
    words = command.split()
    if words[1] in consts.direction_from_string:
        return CommandClassification.MOVE, consts.direction_from_string[words[1]]
    else:
        return (CommandClassification.UNKNOWN,)


def parse_action_command(command: str) -> tuple:
    """Returns a classification of action. No more needs to be returned since the
    do_command function can later take the whole command as an argument."""
    return (CommandClassification.ACTION,)


def parse_unknown_command(command: str) -> tuple:
    """Returns a classification of unknown. No more needs to be returned since the
    do_command function can later take the whole command as an argument."""
    return (CommandClassification.UNKNOWN,)


def parse_command(command: str) -> tuple:
    """Parses a command, returning a tuple representing that command in a format recognizable to the player."""
    command_type = classify_command(command)
    match command_type:
        case CommandClassification.USAGE:
            return parse_usage_command(command)
        case CommandClassification.ITEM_COMBINE:
            return parse_item_combine_command(command)
        case CommandClassification.MOVE:
            return parse_move_command(command)
        case CommandClassification.ACTION:
            return parse_action_command(command)
        case _:
            return parse_unknown_command(command)


if __name__ == '__main__':
    print(classify_command('use metal on sword'))
