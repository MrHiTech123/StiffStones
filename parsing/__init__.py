from enum import Enum
from consts import Direction
import re


class CommandClassification(Enum):
    UNKNOWN = -1
    MOVE = 0
    ACTION = 1
    USAGE = 2


def classify_command(command: str) -> CommandClassification:
    """Classifies a command into one of many categories so that it can be later parsed"""
    # If it matches the regex "use .* on .*":
    if re.search('use .* on .*', command):
        return CommandClassification.USAGE
    elif command in tuple(Direction):
        return CommandClassification.MOVE
    else:
        return CommandClassification.ACTION

def parse_usage_command(command: str) -> tuple:
    """Gives the item and target of a usage command"""
    words = command.split()
    return (words[1], words[3])



if __name__ == '__main__':
    print(classify_command('use metal on sword'))
