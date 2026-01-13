# All constants
EMPTY = '.'
PAWN = 'p'
KING = 'k'
QUEEN = 'q'
ROOK = 'r'
BISHOP = 'b'
KNIGHT = 'n'
WHITE = 'wh'
BLACK = 'bl'
BOARD_SIZE = 8
WHITE_LAST_RANK_INDEX = 7
BLACK_LAST_RANK_INDEX = 0
WHITE_PAWN_START_INDEX = 6
BLACK_PAWN_START_INDEX = 1
PROMOTION_LIST = ['R', 'N', 'B', 'Q']
STARTING_FEN_STRING = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
STARTING_BOARD = [
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
]
COORD_MAP = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}