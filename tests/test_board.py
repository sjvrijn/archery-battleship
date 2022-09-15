from textwrap import dedent

from pytest import raises

from battleship.board import Board
from battleship.ship import ShipOrientation, ShipPartState


def test_str_empty_board():
    b = Board(4)
    assert str(b) == '....\n....\n....\n....'


def test_str_place_hi():
    b = Board()
    b.place_ship(8, 1, 1, ShipOrientation.VERTICAL)
    b.place_ship(8, 1, 6, ShipOrientation.VERTICAL)
    b.place_ship(2, 5, 3, ShipOrientation.HORIZONTAL)
    b.shoot(5, 3)
    b.shoot(5, 4)
    b.place_ship(2, 1, 8, ShipOrientation.VERTICAL)
    b.place_ship(5, 4, 8, ShipOrientation.VERTICAL)
    assert str(b) == dedent(
            '''\
            ..........
            .O....O.O.
            .O....O.O.
            .O....O...
            .O....O.O.
            .O.SS.O.O.
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

def test_invalid_args_small_row():
    b = Board()
    with raises(ValueError):
        b.place_ship(1, -1, 1, ShipOrientation.HORIZONTAL)

def test_invalid_args_small_col():
    b = Board()
    with raises(ValueError):
        b.place_ship(1, 1, -1, ShipOrientation.HORIZONTAL)

def test_invalid_args_large_row():
    b = Board(10)
    with raises(ValueError):
        b.place_ship(1, 11, 1, ShipOrientation.HORIZONTAL)

def test_invalid_args_large_col():
    b = Board(10)
    with raises(ValueError):
        b.place_ship(1, 1, 11, ShipOrientation.HORIZONTAL)

def test_invalid_args_too_long_horizontal():
    b = Board(10)
    with raises(ValueError):
        b.place_ship(10, 1, 1, ShipOrientation.HORIZONTAL)

def test_invalid_args_too_long_vertical():
    b = Board(10)
    with raises(ValueError):
        b.place_ship(10, 1, 1, ShipOrientation.VERTICAL)

def test_shoot_empty():
    b = Board()
    assert b.shoot(0, 0) == ShipPartState.NONE

def test_shoot_ship():
    b = Board()
    b.place_ship(3, 1, 1, ShipOrientation.HORIZONTAL)
    assert b.shoot(1, 1) == ShipPartState.HIT

def test_sink_ship():
    b = Board()
    b.place_ship(3, 1, 1, ShipOrientation.HORIZONTAL)
    b.shoot(1, 1)
    b.shoot(1, 2)
    assert b.shoot(1, 3) == ShipPartState.SUNK

def test_fleet_sunk_single_ship():
    b = Board()
    b.place_ship(3, 1, 1, ShipOrientation.HORIZONTAL)
    b.shoot(1, 1)
    b.shoot(1, 2)
    b.shoot(1, 3)
    assert b.fleet_sunk()

def test_fleet_sunk_multiple_ships():
    ship_rows = (1, 3, 5)
    ship_col = 1
    ship_length = 3

    b = Board()
    for row in ship_rows:
        b.place_ship(ship_length, row, ship_col, ShipOrientation.HORIZONTAL)
    for row in ship_rows:
        assert not b.fleet_sunk()
        for i in range(ship_length):
            b.shoot(row, ship_col+i)

    # fleet should only be sank after all ships are sank
    assert b.fleet_sunk()
