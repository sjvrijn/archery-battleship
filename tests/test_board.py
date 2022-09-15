from textwrap import dedent

from pytest import raises

from battleship.board import Board
from battleship.ship import ShipOrientation


def test_str_empty_board():
    b = Board(4)
    assert str(b) == '....\n....\n....\n....'


def test_str_place_hi():
    b = Board()
    b.place_ship(8, 1, 1, ShipOrientation.VERTICAL)
    b.place_ship(8, 1, 6, ShipOrientation.VERTICAL)
    b.place_ship(2, 5, 3, ShipOrientation.HORIZONTAL)
    b.place_ship(2, 1, 8, ShipOrientation.VERTICAL)
    b.place_ship(5, 4, 8, ShipOrientation.VERTICAL)
    assert str(b) == dedent(
            '''\
            ..........
            .O....O.O.
            .O....O.O.
            .O....O...
            .O....O.O.
            .O.OO.O.O.
            .O....O.O.
            .O....O.O.
            .O....O.O.
            ..........'''
        )

def test_invalid_crossing_ships():
    b = Board()
    b.place_ship(4, 2, 1, ShipOrientation.HORIZONTAL)
    with raises(ValueError):
        b.place_ship(4, 1, 2, ShipOrientation.VERTICAL)

def test_invalid_parallel_ships_horizontal():
    b = Board()
    b.place_ship(4, 2, 1, ShipOrientation.HORIZONTAL)
    with raises(ValueError):
        b.place_ship(4, 3, 1, ShipOrientation.HORIZONTAL)

def test_invalid_parallel_ships_vertical():
    b = Board()
    b.place_ship(4, 2, 1, ShipOrientation.VERTICAL)
    with raises(ValueError):
        b.place_ship(4, 2, 2, ShipOrientation.VERTICAL)

def test_invalid_on_edge_ships():
    b = Board()
    b.place_ship(4, 2, 1, ShipOrientation.HORIZONTAL)
    with raises(ValueError):
        b.place_ship(4, 1, 5, ShipOrientation.VERTICAL)
