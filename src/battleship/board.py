"""Class for a board in a game of BattleShip"""

from itertools import product

from .ship import Ship, ShipOrientation, ShipPartState, NONE_SHIP


state_print_parse_private = {
    ShipPartState.NONE: '.',
    ShipPartState.SAFE: 'O',
    ShipPartState.HIT: 'X',
    ShipPartState.SUNK: 'S',
}
state_print_parse_public = {
    ShipPartState.NONE: '.',
    ShipPartState.SAFE: '.',
    ShipPartState.HIT: 'X',
    ShipPartState.SUNK: 'S',
}


class Board:

    def __init__(self, size: int=10):
        if size < 3:
            raise ValueError("The size of a board should be at least 3.")

        self.size = size
        self.field = [
            [(NONE_SHIP, 0) for _ in range(size)]
            for _ in range(size)
        ]
        self.ships = []

    def place_ship(self, size: int, row: int, col: int, orientation: ShipOrientation):
        """Place a ship of `size` at (row,col) on the board"""
        self.check_valid_placement_args(size, row, col, orientation)
        if not self.check_non_blocking(size, row, col, orientation):
            raise ValueError('Cannot place ship here, is blocked by another already present')

        ship = Ship(size, orientation)
        self.ships.append(ship)
        for i in range(size):
            if orientation == ShipOrientation.HORIZONTAL:
                self.field[row][col+i] = (ship, i)
            else:
                self.field[row+i][col] = (ship, i)

    def check_valid_placement_args(self, size: int, row: int, col: int, orientation: ShipOrientation):
        """Check validity of arguments: does everything fit in the board?"""
        if not (0 <= row < self.size):
            raise ValueError(f"row={row} is invalid, must be 0..{self.size-1}")
        if not (0 <= col < self.size):
            raise ValueError(f"col={col} is invalid, must be 0..{self.size-1}")

        orientations = [ShipOrientation.HORIZONTAL, ShipOrientation.VERTICAL]
        if orientation not in orientations:
            raise ValueError(f"orientation={orientation} is invalid, must be any of {orientations}")

        end = col + (size-1) if orientation == ShipOrientation.HORIZONTAL else row + (size-1)
        if end >= self.size:
            raise ValueError("ship is too long for this location")

    def check_non_blocking(self, size: int, row: int, col: int, orientation: ShipOrientation):
        """Check if all cells around intended location are free"""
        startrow = row-1 if row > 0 else row
        startcol = col-1 if col > 0 else col
        if orientation == ShipOrientation.HORIZONTAL:
            endrow, endcol = row+1, col+size+1
        else:
            endrow, endcol = row+size+1, col+1

        if endrow >= self.size:
            endrow = self.size
        if endcol >= self.size:
            endcol = self.size

        for r, c in product(range(startrow, endrow), range(startcol, endcol)):
            if self.field[r][c][0] is not NONE_SHIP:
                return False
        return True  # Placement is valid if no conflict was found

    def shoot(self, row: int, col: int) -> ShipPartState:
        """Shoot a location on the board and report the result"""
        if not (0 <= row < self.size):
            raise ValueError(f"row={row} is invalid, must be 0..{self.size-1}")
        if not (0 <= col < self.size):
            raise ValueError(f"col={col} is invalid, must be 0..{self.size-1}")

        s, i = self.field[row][col]
        if s is NONE_SHIP:
            return ShipPartState.NONE
        s.hit(i)
        return s.parts[i]

    def fleet_sunk(self):
        return all(s.sunk for s in self.ships)

    def __str__(self):
        return self.display(public=False)

    def display(self, public: bool=True):
        """Display the whole board as a grid with ./O/X for empty/safe/hit"""
        parse_dict = state_print_parse_public if public else state_print_parse_private
        return '\n'.join([
            ''.join(
                [
                    parse_dict[ship.parts[i]]
                    for ship, i in row
                ]
            )
            for row in self.field
        ])
