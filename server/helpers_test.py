import pytest
from helpers import parse_board_state

class TestParseBoardState:
    def test_valid_board_state(self):
        board_string = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
        expected = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ]
        
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