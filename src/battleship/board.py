"""Class for a board in a game of BattleShip"""

from .ship import Ship, ShipOrientation, ShipPartState, NONE_SHIP


state_print_parse = {
    ShipPartState.NONE: '.',
    ShipPartState.SAFE: 'O',
    ShipPartState.HIT: 'X',
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

    def place_ship(self, size: int, row: int, col: int, orientation: ShipOrientation):
        """Place a ship of `size` at (row,col) on the board"""
        if not (0 <= row < self.size):
            raise ValueError(f"row={row} is invalid, must be 0..{self.size-1}")
        if not (0 <= col < self.size):
            raise ValueError(f"col={col} is invalid, must be 0..{self.size-1}")

        ship = Ship(size, orientation)
        for i in range(size):
            if orientation == ShipOrientation.HORIZONTAL:
                self.field[row][col+i] = (ship, i)
            else:
                self.field[row+i][col] = (ship, i)

    def __str__(self):
        """Display the whole board as a grid with ./O/X for empty/safe/hit"""
        return '\n'.join([
            ''.join(
                [
                    state_print_parse[ship.parts[i]]
                    for ship, i in row
                ]
            )
            for row in self.field
        ])
