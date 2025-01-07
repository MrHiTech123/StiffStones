from enum import Enum
from consts import Direction
import re



class CommandClassifications(Enum):
    UNKNOWN = -1
    MOVE = 0
    ACTION = 1
    USAGE = 2
    

class CommandClassifier:
    @staticmethod
    def classify(command: str) -> CommandClassifications:
        if re.search('use .* on .*', ''):
            return CommandClassifications.USAGE
        elif command in tuple(Direction):
            return CommandClassifications.MOVE
        else:
            return CommandClassifications.ACTION

if __name__ == '__main__':
    print('wes' in tuple(Direction))