import constants

def parse_board_state(state_string):
    """
    Guess what this does. 
    """
    board = [[constants.EMPTY for _ in range(constants.BOARD_SIZE)] for _ in range(constants.BOARD_SIZE)] 

    # Get the rows. If there are not exactly eight rows, something is seriously wrong. 
    rows = state_string.split('/')
    if len(rows) != 8:
        raise ValueError()
    
    # Iterate through every row. 
    for i in range(8):
        # Iterate throgh every tile. 
        j = 0
        for c in rows[7 - i]:
            if str.isdigit(c):
                # TODO: Check that the number isn't bogus. 
                j += int(c)
            else:
                board[i][j] = c
                j += 1
    return board

def parse_fen_string(state_string):
    """
    Given a state string (see Forsyth-Edwards notation), this function returns a structure with corresponding 
    fields. 

    Here's a link to Forsyth-Edwards Notation: https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation

    Here is an example string: rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1

    arguments:
    state_string (string) -- The Forsyth-Edwards string outlining the state of the game. 

    return:
    a dictionary with the corresponding fields. 
    """
    parts = state_string.split()

    # Sanity check. If there are more than four, then something is wrong. 
    if len(parts) != 6:
        raise ValueError()
    
    board = parse_board_state(parts[0])
    
    if parts[1] == 'b':
        active_player = constants.BLACK
    elif parts[1] == 'w':
        active_player = constants.WHITE
    else:
        raise ValueError('active_player must be white or black')
    
    # TODO: do something with this? check if it is valid?
    castling = parts[2]

    # TODO: check this is valid. 
    en_passant_point = None
    if parts[3] == '-':
        en_passant_point = '-'
    elif len(parts[3]) == 2 and parts[3][0] in constants.COORD_MAP:
        en_passant_point = (int(parts[3][1]) - 1, constants.COORD_MAP[parts[3][0]])
    else:
        raise ValueError('something is wrong with the en passant point')

    # board, active_player, castling, and en_passant_loc
    return { 'board': board, 'active_player': active_player, 'castling': castling, 'en_passant_point': en_passant_point }

def write_state_to_fen(state):
    fen_str = ''
    for row in state['board']:
        empty_sqaure_count = 0
        for square in row:
            if square == constants.EMPTY:
                empty_sqaure_count += 1
            else:
                fen_str = ('' if empty_sqaure_count == 0 else str(empty_sqaure_count)) + fen_str
                empty_sqaure_count = 0
    

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