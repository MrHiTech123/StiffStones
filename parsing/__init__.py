from enum import Enum

import consts
from consts import Direction
import re


class CommandClassification(Enum):
    UNKNOWN = -1
    MOVE = 0
    ACTION = 1
    USAGE = 2
    ITEM_COMBINE = 3


def classify_command(command: str) -> CommandClassification:
    """Classifies a command into one of many categories so that it can be later parsed"""
    # If it matches the regex "use \S* on \S+":
    if command in consts.actions:
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
    """Gives the item and target of a usage command"""
    words = command.split()
    return CommandClassification.USAGE, words[1], words[3]

def parse_item_combine_command(command: str) -> tuple:
    words = command.split()
    return CommandClassification.ITEM_COMBINE, words[1], words[3]

def parse_move_command(command: str) -> tuple:
    words = command.split()
    if words[1] in consts.direction_from_string:
        return CommandClassification.MOVE, consts.direction_from_string[words[1]]
    else:
        return CommandClassification.UNKNOWN, command

def parse_unknown_command(command: str) -> tuple:
    return (CommandClassification.UNKNOWN, )

def parse_command(command: str) -> tuple:
    command_type = classify_command(command)
    match command_type:
        case CommandClassification.USAGE:
            return parse_usage_command(command)
        case CommandClassification.ITEM_COMBINE:
            return parse_item_combine_command(command)
        case CommandClassification.MOVE:
            return parse_move_command(command)
        case _:
            return parse_unknown_command(command)
    
    

if __name__ == '__main__':
    print(classify_command('use metal on sword'))
