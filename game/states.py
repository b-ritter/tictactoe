from enum import Enum

class GameStates(Enum):
    PLAY = 1
    INVALID_INPUT = 2
    INVALID_MOVE = 3
    WIN = 4
    TIE = 5
    EXIT = 6
    HELP = 7
    QUIT = 8