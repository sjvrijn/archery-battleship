from pytest import raises

from battleship.board import Board
from battleship.game import step_direction, select_next_direction, select_next_valid_shot_and_direction


def test_next_directions():
    assert select_next_direction((5,0)) == (0,1)
    assert select_next_direction((0,5)) == (-1,0)
    assert select_next_direction((-5,0)) == (0,-1)

def test_next_direction_west_south_invalid():
    with raises(ValueError):
        select_next_direction((0,-5))

def test_next_shots():
    b = Board()
    assert step_direction((1,0)) == (2,0)
    assert step_direction((0,1)) == (0,2)
    assert step_direction((-1,0)) == (-2,0)
    assert step_direction((0,-1)) == (0,-2)

def test_next_shot_in_corners():
    b = Board(10)
    assert select_next_valid_shot_and_direction(b, (9,0), (1,0)) == ((9,1), (0,1))
    assert select_next_valid_shot_and_direction(b, (9,9), (1,0)) == ((8,9), (-1,0))
    assert select_next_valid_shot_and_direction(b, (0,9), (0,1)) == ((0,8), (0,-1))


def test_next_shot_error_in_corner():
    b = Board(10)
    with raises(ValueError):
        assert select_next_valid_shot_and_direction(b, (0,0), (-1,0))
