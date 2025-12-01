"""
this file provides a function that takes both a game state and a piece on the board and gives back an array of all 
possible next states. this can be used to both: 
    (1) evaluate if a move is legal (useful for the game engine). 
    (2) generate a game tree. 
"""
import constants
from copy import deepcopy
from helpers import who_is_on_the_sqaure, what_is_on_the_sqaure, next_player, end_sqaure

def copy_state(state, f, t, piece=None):
    # Make a deep copy. Updating values in the state won't change the original object. 
    state = deepcopy(state)

    r_1, c_1 = f
    r_2, c_2 = t

    state['board'][r_2][c_2] = state['board'][r_1][c_1] if piece is None else piece
    state['board'][r_1][c_1] = constants.EMPTY

    state['active_player'] = next_player(state['active_player'])

    state['en_passant_point'] = None

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
            new_state['en_passant_point'] = (next_r, c)  # have to update the en_passant_point. 
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

    return next_states

