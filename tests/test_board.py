from textwrap import dedent

from battleship.board import Board


def test_str_empty_board():
    b = Board(4)
    assert str(b) == '....\n....\n....\n....'


def test_str_place_hi():
    b = Board()
    b.place_ship(8, 1, 1, False)
    b.place_ship(8, 1, 6, False)
    b.place_ship(2, 5, 3, True)
    b.place_ship(2, 1, 8, False)
    b.place_ship(5, 4, 8, False)
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
