"""Class for a (Battle)Ship"""


from enum import IntEnum


class ShipPartState(IntEnum):
    NONE = 0
    SAFE = 1
    HIT = 2
    SUNK = 3
    MISS = 4


class ShipOrientation(IntEnum):
    HORIZONTAL = 0
    VERTICAL = 1


class Ship:
    
    def __init__(self, size: int, orientation: ShipOrientation):
        self.parts = [ShipPartState.SAFE for _ in range(size)]
        self.orientation = orientation
        self.sunk = False

    @property
    def size(self):
        return len(self.parts)

    def hit(self, i: int):
        self.parts[i] = ShipPartState.HIT
        if all(p == ShipPartState.HIT for p in self.parts):
            self.parts = [ShipPartState.SUNK for _ in range(self.size)]
            self.sunk = True


# Define an 'empty' ship to serve as an empty square
NONE_SHIP = Ship(1, ShipOrientation.HORIZONTAL)
NONE_SHIP.parts[0] = ShipPartState.NONE

# Define a 'miss' ship to serve as a tracker for missed shots
MISS_SHIP = Ship(1, ShipOrientation.HORIZONTAL)
MISS_SHIP.parts[0] = ShipPartState.MISS
