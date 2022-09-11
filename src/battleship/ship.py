"""Class for a (Battle)Ship"""


from enum import IntEnum


class ShipPartState(IntEnum):
    NONE = 0
    SAFE = 1
    HIT = 2


class Ship:
    
    def __init__(self, size):
        self.parts = [ShipPartState.SAFE for _ in range(size)]
        

# Define an 'empty' ship to serve as an empty square
NONE_SHIP = Ship(1)
NONE_SHIP.parts[0] = ShipPartState.NONE
