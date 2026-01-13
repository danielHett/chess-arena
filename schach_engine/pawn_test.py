from schach_engine.engine import next_states_pawn
from schach_engine.state_utilities import read_fen_string, write_fen_string

def to_states(strings):
    return [read_fen_string(s) for s in strings]

def is_matching(alpha, beta):
    return set([write_fen_string(a) for a in alpha]) == set([write_fen_string(b) for b in beta])

class TestNextStatesPawn:
    def test_one_forward(self):
        starting_state = read_fen_string('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1')
        expected_next_states = to_states(['rnbqkbnr/ppppppp1/7p/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'])

        print("HI", next_states_pawn(starting_state, (1, 7)))
        assert is_matching(expected_next_states, next_states_pawn(starting_state, (1, 7)))