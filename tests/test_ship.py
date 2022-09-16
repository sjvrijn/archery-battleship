from pytest import raises

from battleship.ship import Ship, ShipPartState, ShipOrientation


def test_bare_ship():
    length = 5
    s = Ship(length, ShipOrientation.HORIZONTAL)
    assert all(p == ShipPartState.SAFE for p in s.parts)
    assert s.sunk == False

def test_ship_hit():
    length = 5
    s = Ship(length, ShipOrientation.HORIZONTAL)
    s.hit(2)
    assert s.parts[2] == ShipPartState.HIT
    assert sum(p == ShipPartState.SAFE for p in s.parts) == length - 1
    assert sum(p == ShipPartState.HIT for p in s.parts) == 1
    assert s.sunk == False

def test_sink_ship():
    length = 3
    s = Ship(length, ShipOrientation.HORIZONTAL)
    s.hit(0)
    s.hit(1)
    s.hit(2)
    assert s.sunk == True
    assert sum(p == ShipPartState.SUNK for p in s.parts) == length
