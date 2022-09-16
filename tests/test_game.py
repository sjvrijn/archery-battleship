from pytest import raises

from battleship.board import Board
from battleship.game import select_next_shot, select_next_direction


def test_next_directions():
    assert select_next_direction((5,0)) == (0,1)
    assert select_next_direction((0,5)) == (-1,0)
    assert select_next_direction((-5,0)) == (0,-1)

def test_next_direction_west_south_invalid():
    with raises(ValueError):
        select_next_direction((0,-5))

def test_next_shots():
    b = Board()
    assert select_next_shot(b, (4,4), (1,0)) == ((5,4), (2,0))
    assert select_next_shot(b, (4,4), (0,1)) == ((4,5), (0,2))
    assert select_next_shot(b, (4,4), (-1,0)) == ((3,4), (-2,0))
    assert select_next_shot(b, (4,4), (0,-1)) == ((4,3), (0,-2))

def test_next_shot_in_corners():
    b = Board(10)
    # assert select_next_shot(b, (9,0), (1,0)) == ((9,1), (0,2))
    assert select_next_shot(b, (9,9), (1,0)) == ((8,9), (-2,0))
    assert select_next_shot(b, (0,9), (0,1)) == ((0,8), (0,-2))


def test_next_shot_error_in_corner():
    b = Board(10)
    with raises(ValueError):
        assert select_next_shot(b, (0,0), (-1,0))
