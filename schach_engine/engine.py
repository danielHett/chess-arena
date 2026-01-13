"""
this file provides a function that takes both a game state and a piece on the board and gives back an array of all 
possible next states. this can be used to both: 
    (1) evaluate if a move is legal (useful for the game engine). 
    (2) generate a game tree. 
"""
from schach_engine import constants
from copy import deepcopy
from schach_engine.utilities import who_is_on_the_sqaure, what_is_on_the_sqaure, next_player, end_sqaure

def copy_state(state, f, t, piece=None):
    # Make a deep copy. Updating values in the state won't change the original object. 
    state = deepcopy(state)

    r_1, c_1 = f
    r_2, c_2 = t

    state['board'][r_2][c_2] = state['board'][r_1][c_1] if piece is None else piece
    state['board'][r_1][c_1] = constants.EMPTY

    state['active_player'] = next_player(state['active_player'])

    state['en_passant_sqaure'] = None

    return state

def next_states_pawn(state, point):
    # Do a sanity check. Is the piece a pawn?
    color = who_is_on_the_sqaure(state['board'], point)
    if (color == constants.EMPTY or what_is_on_the_sqaure(state['board'], point) != constants.PAWN):
        raise ValueError('FATAL: next_states_pawn was passed something that was not a pawn!')
    
    # We keep all of the next possible states here. 
    next_states = []

    # Need the coordinates and direction
    r, c = point
    dir = 1 if color == constants.WHITE else -1
    next_r = r + (dir * 1)
    über_next_r = r + (dir * 2)

    # if the pawn is [white and placed on row 1] or [black and placed on row 6]
    if ((color == constants.WHITE and r == 1) or (color == constants.BLACK and r == 6)):
        # check first if the next spot is empty. if so, we have a possible state. 
        if (state['board'][next_r][c] == constants.EMPTY and state['board'][über_next_r][c] == constants.EMPTY):
            new_state = copy_state(state, (r, c), (über_next_r, c ))
            new_state['en_passant_sqaure'] = (next_r, c)  # have to update the en_passant_sqaure. 
            next_states.append(new_state)
    
    # moving forward. make sure we aren't already at an end state. 
    if (r == constants.WHITE_LAST_RANK_INDEX and r == constants.BLACK_LAST_RANK_INDEX):
        raise ValueError('FATAL: next_states_pawn was passed a state with a pawn on an end sqaure!')
    
    # if the next sqaure is open, we can move there. 
    if (state['board'][next_r][c] == constants.EMPTY):
        # are we at the end sqaure? then give back all promotion states. 
        if next_r == end_sqaure(color):
            [next_states.append(copy_state(state, (r, c), (next_r, c), piece if color == constants.WHITE else piece.lower())) for piece in constants.PROMOTION_LIST]
        # otherwise just move forward. 
        else:
            next_states.append(copy_state(state, (r, c), (next_r, c)))

    # check the diagonals. we already checked we weren't on the last rank, so we don't check again. 
    # TODO: this can be cleaner. 
    diag_points_in_bound = []
    if c - 1 >= 0:
        diag_points_in_bound.append((r + (dir * 1), c - 1))
    if c + 1 <= 7:
        diag_points_in_bound.append((r + (dir * 1), c + 1)) 
    
    for next_point in diag_points_in_bound:
        # first, can we attack the sqaure? must be an enemy piece that isn't a king.
        is_enemy_on_point = who_is_on_the_sqaure(state['board'], next_point) == color and what_is_on_the_sqaure(state['board'], next_point) != constants.KING
        # or the point is en passant. 
        is_en_passant = state['en_passant_sqaure'] == next_point
        
        if is_enemy_on_point or is_en_passant:
            next_r, next_c = next_point
            temp_states = []

            # promote the pawn. 
            if next_r == end_sqaure(color):
                [temp_states.append(copy_state(state, point, next_point, piece if color == constants.WHITE else piece.lower())) for piece in constants.PROMOTION_LIST]
            else:
                temp_states.append(copy_state(state, point, next_point))
            
            # if it was en_passant, we also need to take the enemy pawn. 
            if is_en_passant:
                # opponent moves in the opposite direction. 
                opponent_dir = dir * -1
                for temp_state in temp_states:
                    # next_r + opponent_dir * 1 gives us the row coordinate for the opponent piece, so we can remove it. 
                    temp_state['board'][next_r + (opponent_dir * 1)][next_c] = constants.EMPTY
            
            next_states.extend(temp_states)

    return next_states

