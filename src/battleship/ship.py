"""Class for a (Battle)Ship"""


from enum import IntEnum


class ShipPartState(IntEnum):
    NONE = 0
    SAFE = 1
    HIT = 2


class ShipOrientation(IntEnum):
    HORIZONTAL = 0
    VERTICAL = 1


class Ship:
    
    def __init__(self, size: int, orientation: ShipOrientation):
        self.parts = [ShipPartState.SAFE for _ in range(size)]
        self.orientation = orientation

    def hit(i: int):
        self.parts[i] = ShipPartState.HIT


# Define an 'empty' ship to serve as an empty square
NONE_SHIP = Ship(1, ShipOrientation.HORIZONTAL)
NONE_SHIP.parts[0] = ShipPartState.NONE
