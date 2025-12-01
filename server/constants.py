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
WHITE_LAST_RANK_INDEX = 0
BLACK_LAST_RANK_INDEX = 7
WHITE_PAWN_START_INDEX = 6
BLACK_PAWN_START_INDEX = 1
PROMOTION_LIST = ['R', 'N', 'B', 'Q']
STARTING_FEN_STRING = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
STARTING_BOARD = [
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', ''],
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']
]