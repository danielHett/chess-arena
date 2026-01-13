import pytest
from copy import deepcopy
from schach_engine import constants
from schach_engine.state_utilities import parse_board_state, parse_en_passant_point, read_fen_string

class TestParseBoardState:
    def test_valid_board_state(self):
        board_string = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
        expected = deepcopy(constants.STARTING_BOARD)
        
        print(parse_board_state(board_string))
        assert parse_board_state(board_string) == expected
    
    def test_valid_board_state_mid_game(self):
        board_string = 'rnbqkbnr/pp1ppppp/8/2p5/6Q1/4P3/PPPP1PPP/RNB1KBNR'
        expected = [
            ['R', 'N', 'B', '.', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', '.', 'P', 'P', 'P'],
            ['.', '.', '.', '.', 'P', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', 'Q', '.'],
            ['.', '.', 'p', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['p', 'p', '.', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ]
        
        print(parse_board_state(board_string))
        assert parse_board_state(board_string) == expected
    
    def test_invalid_board_state_too_many_rows(self):
        board_string = 'rnbqkbnr/pppppppp/8/8/8/8/8/PPPPPPPP/RNBQKBNR'
        with pytest.raises(ValueError):
            parse_board_state(board_string)

    def test_invalid_board_state_too_few_rows(self):
        board_string = 'rnbqkbnr/pppppppp/8/8/8/PPPPPPPP/RNBQKBNR'
        with pytest.raises(ValueError):
            parse_board_state(board_string)

    # TODO: This test will fail until some logic is written to check for this.
    def test_invalid_board_state_too_many_sqaures(self):
        board_string = 'rnbqkbnr/pppppppp/8/8/8/7/PPPPPPPP/RNBQKBNR'
        with pytest.raises(ValueError):
            parse_board_state(board_string)

        board_string = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPPP/RNBQKBNR'
        with pytest.raises(ValueError):
            parse_board_state(board_string)
    
    # TODO: This test will fail until some logic is written to check for this.
    def test_invalid_board_state_too_few_sqaures(self):
        # Has a row with only 7 sqaures. 
        board_string = 'rnbqkbnr/pp1ppppp/8/2p5/6Q1/3P3/PPPP1PPP/RNB1KBNR'
        with pytest.raises(ValueError):
            parse_board_state(board_string)

        # Has a row with only 7 sqaures. 
        board_string = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPP/RNBQKBNR'
        with pytest.raises(ValueError):
            parse_board_state(board_string)

class TestParseEnPassantPoint:
    def test_empty(self):
        assert parse_en_passant_point('-') is None

    def test_valid(self):
        assert parse_en_passant_point('e3') == (2, 4)

    def test_invalid_invalid_letter(self):
        with pytest.raises(ValueError):
            parse_en_passant_point('i1')
        with pytest.raises(ValueError):
            parse_en_passant_point('E1')
    
    def test_invalid_invalid_number(self):
        with pytest.raises(ValueError):
            parse_en_passant_point('i0')
        with pytest.raises(ValueError):
            parse_en_passant_point('i9')

class TestReadFenString:
    def test_read_valid_fen_string(self):
        s = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'
        expected = {
            'board': deepcopy(constants.STARTING_BOARD),
            'active_player': constants.WHITE, 
            'castling': 'KQkq', 
            'en_passant_point': None
        }

        assert read_fen_string(s) == expected

    def test_read_invalid_fen_string(self):
        s = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR daniel KQkq - 0 1'

        with pytest.raises(ValueError):
            read_fen_string(s)