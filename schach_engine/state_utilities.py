from schach_engine import constants

def parse_board_state(state_string):
    """
    This is used for parsing the board part of a chess state encoded using Forsyth-Edwards notation. 
    
    :param state_string: A string describing the state of the board. Consult the documentation for Forsyth-Edwards notation 
    to see how this should look. 
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
            # This should stop us from accessing out-of-bounds. 
            if j >= 8:
                raise ValueError('More than 8 tiles in row ' + str(i) + '.')
            
            if str.isdigit(c):
                # TODO: Check that the number isn't bogus. 
                j += int(c)
            else:
                board[i][j] = c
                j += 1
        
        if j != 8:
            raise ValueError('Number of tiles (' + str(j) + ') in row ' + str(i) + ' is not equal to 8.')
        
    return board

# TODO: Needs more checking. 
def parse_en_passant_point(point_string):
    """
    This is used for parsing the en-passant part of a chess state encoded using Forsyth-Edwards notation. 
    
    :param point_string: A string describing en-passant sqaure. Consult the documentation for Forsyth-Edwards notation 
    to see how this should look. 
    """
    if point_string == '-':
        return None
    elif len(point_string) == 2 and point_string[0] in constants.COORD_MAP:
        # FEN coordinates are 1-indexed but we are indexing from 0, hence we subtract 1. 
        # We also need to translate the letter to an integer. 
        return (int(point_string[1]) - 1, constants.COORD_MAP[point_string[0]])
    else:
        raise ValueError('ERROR: Something is wrong with the en-passant sqaure.')
    
def read_fen_string(state_string):
    """
    Given a state string (see Forsyth-Edwards notation), this function returns a structure with corresponding 
    fields. Here's a link to Forsyth-Edwards Notation: https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation. 

    :param state_string: A string encoding the state of the chess game using Forsyth-Edwards notation. 
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
 
    en_passant_point = parse_en_passant_point(parts[3])

    # board, active_player, castling, and en_passant_loc
    return { 'board': board, 'active_player': active_player, 'castling': castling, 'en_passant_point': en_passant_point }

# TODO: Finish and test this. 
def write_fen_string(state):
    """
    At some point we may need to take a state and write it back to the string encoding. 
    
    :param state: the (already parsed) state of the chess game. 
    """
    fen_str = ''
    for row in state['board']:
        empty_sqaure_count = 0
        row_str = ''
        for square in row:
            if square == constants.EMPTY:
                empty_sqaure_count += 1
            else:
                row_str += ('' if empty_sqaure_count == 0 else str(empty_sqaure_count)) + square
                empty_sqaure_count = 0
        fen_str = row_str + fen_str
    
    print(fen_str)