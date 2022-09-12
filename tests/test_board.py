from textwrap import dedent

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
