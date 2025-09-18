BOARD_SIZE = 8

def parse_board_state(state_string):
    """
    Given a state string (see Forsyth-Edwards notation), this function returns a structure with corresponding 
    fields. 

    arguments:
    state_string (string) -- The Forsyth-Edwards string outlining the state of the game. 

    return:
    a dictionary with the corresponding fields. 
    """
    board = [['.' for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)] 

    # Iterate through the board. 'i' tracks the state_string and 'j' the board. 
    i = 0
    while len(state_string) > 0: 
        # If not a number, it's a piece. Add it to the board.    
        if not str.isdigit(state_string[0]):
            board[int(i / BOARD_SIZE)][i % BOARD_SIZE] = state_string[0]
            state_string = state_string[1:]
            i += 1
            continue

        # If it is a digit, we need to parse the whole number. 
        n = ''
        while str.isdigit(state_string[0]):
            n += state_string[0]
            state_string = state_string[1:]
        i += int(n)
        
    return board

def parse_state_string(state_string):
    """
    Given a state string (see Forsyth-Edwards notation), this function returns a structure with corresponding 
    fields. 

    Here's a link to Forsyth-Edwards Notation: https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation

    arguments:
    state_string (string) -- The Forsyth-Edwards string outlining the state of the game. 

    return:
    a dictionary with the corresponding fields. 
    """
    teile = state_string.split()

    # Sanity check. If there are more than two, then something is wrong. 
    if len(teile) != 2:
        raise ValueError()
    
    state = {
        'board': parse_board_state(teile[0]),
        'player': teile[1]
    }

    return state