from enum import Enum
from consts import Direction
import re


class CommandClassifications(Enum):
    UNKNOWN = -1
    MOVE = 0
    ACTION = 1
    USAGE = 2


def classify_command(command: str) -> CommandClassifications:
    """Classifies a command into one of many categories so that it can be later parsed"""
    # If it matches the regex "use .* on .*":
    if re.search('use .* on .*', command):
        return CommandClassifications.USAGE
    elif command in tuple(Direction):
        return CommandClassifications.MOVE
    else:
        return CommandClassifications.ACTION

def parse_usage_command(command: str) -> tuple:
    """Gives the item and target of a usage command"""
    words = command.split()
    return (words[1], words[3])



if __name__ == '__main__':
    print(classify_command('use metal on sword'))
