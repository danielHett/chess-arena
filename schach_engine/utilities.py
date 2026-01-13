from schach_engine import constants
    
def who_is_on_the_sqaure(board, point):
    """
    Answers the question, who is on the square? 

    arguments:
    board (array) -- A 2D array representing a chess board.
    point (tuple) -- A pair of integers representing a square on a chess board.  

    return:
    Can return a white piece, a black piece, or nothing. 
    """

    # Point can't exceed the bounds of the board. 
    if (is_bad_coordinate(point)):
        raise IndexError('point out of range')

    r, c = point
    sqaure = board[r][c]

    # Just assume anything that isn't alpha is empty. 
    if not sqaure.isalpha():
        return constants.EMPTY
    
    return constants.WHITE if sqaure.isupper() else constants.BLACK

def what_is_on_the_sqaure(board, point):
    """
    Answers the question, what is on the square? 

    arguments:
    board (array) -- A 2D array representing a chess board.
    point (tuple) -- A pair of integers representing a square on a chess board.  

    return:
    the constant value for the corresponding piece. 
    """
    # Point can't exceed the bounds of the board. 
    if (is_bad_coordinate(point)):
        raise IndexError('point out of range')

    r, c = point
    sqaure = board[r][c]

    if not sqaure.isalpha():
        return constants.EMPTY
    
    return sqaure.lower()

def is_matching_coordinates(a, b):
    return a[0] == b[0] and a[1] == b[1]

def next_player(player):
    return constants.WHITE if player == constants.BLACK else constants.BLACK

def end_sqaure(color):
    return constants.WHITE_LAST_RANK_INDEX if color == constants.WHITE else constants.BLACK_LAST_RANK_INDEX

def is_bad_coordinate(point):
    r, c = point
    return (r >= constants.BOARD_SIZE or r < 0) or (c >= constants.BOARD_SIZE or c < 0)

def is_in_start_state(game_id, games):
    return game_id in games and 'pass_black' in games[game_id]

def assert_game_exists(game_id, games, request):
    return False

def string_to_coord(s):
    return (s.split(',')[0], s.split(',')[1])

def coord_to_string(c):
    return str(c[0]) + ',' + str(c[1])

def calc_movement(move):
    start_point, end_point, _ = move
    start_x, start_y = start_point
    end_x, end_y = end_point
    
    return (end_x - start_x, end_y - start_y)

def print_board(b):
    for row in reversed(b):
        s = ''
        for tile in row:
            s += tile
        print(s)

