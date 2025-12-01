"""
A helpful tool: https://www.redhotpawn.com/chess/chess-fen-viewer.php
"""

from next_states import next_states_pawn
from helpers import parse_fen_string, print_board

state = parse_fen_string('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
print(next_states_pawn(state, (1,0)))

state = parse_fen_string('rnbqkbnr/ppppp1pp/5p2/8/1P6/3P4/P1P1PPPP/RNBQKBNR b KQkq b3 0 1')
print('PRINTING STATES: \n')
for s in next_states_pawn(state, (1,0)):
    print_board(s['board'])
    print('\n')

state = parse_fen_string('rnb1kbnr/pp1pp1pp/2p2p2/1q6/1P6/3P4/P1P1PPPP/RNBQKBNR w KQkq - 0 1')
print('PRINTING STATES: \n')
for s in next_states_pawn(state, (3,1)):
    print_board(s['board'])
    print('\n')

state = parse_fen_string('rnb1kbnr/pp1pp1pp/2p2p2/8/1P1q4/8/P1PPPPPP/RNBQKBNR w KQkq - 0 1')
print('PRINTING STATES: \n')
for s in next_states_pawn(state, (1,3)):
    print_board(s['board'])
    print('\n')